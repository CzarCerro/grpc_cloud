# server

from concurrent import futures
import logging
import grpc
import tracetogether_pb2
import tracetogether_pb2_grpc
import time
from storagehandler import StorageHandler
from tabulate import tabulate


class TraceTogether(tracetogether_pb2_grpc.TraceTogetherServicer):

    def Register(self, request, context):
        """Register new user"""
        status = StorageHandler().register(request.name, request.nric)
        reply = tracetogether_pb2.Reply()

        if status == 1:
            reply.message = 'Successfully registered {}, {}.'.format(request.name, request.nric)
            reply.status = 200

        elif status == 2:
            reply.message = 'NRIC {} already exist.'.format(request.nric)
            reply.status = 401
        
        elif status == 3:
            reply.message = 'Invalid NRIC format.'
            reply.status = 401

        return reply

    def Login(self, request, context):
        """Login with name and NRIC"""
        status, errorMsg = StorageHandler().verify(request.name, request.nric)
        reply = tracetogether_pb2.Reply()
        if status:
            StorageHandler().login(request.nric)
            reply.message = 'Successfully logged in as {}, {}.'.format(request.name, request.nric)
            reply.status = 200
        else:
            reply.message = 'Failed to log in. {}'.format(errorMsg)
            reply.status = 401

        return reply

    def Logout(self, request, context):
        """Logout with name and NRIC"""
        reply = tracetogether_pb2.Reply()

        StorageHandler().logout(request.nric)
        reply.message = 'Successfully logged out.'

        return reply

    def CheckIn(self, request, context):
        """Check in"""
        reply = tracetogether_pb2.Reply()
        names = request.name.split(',')
        nrics = request.nric.split(',')

        #Verify each of the entered names first
        for i in range(len(names)):
            status, errorMsg = StorageHandler().verify(names[i].upper().strip(), nrics[i].strip())
            if not status:
                reply.message = errorMsg
                reply.status = 401
                break

        if status:
            for i in range(len(names)):
                StorageHandler().checkIn(nrics[i].strip(), request.location, request.time)
            reply.message = 'Successfully checked in at {} on {}'.format(request.location,
                                                                         request.time)
            reply.status = 200

        return reply


    def CheckOut(self, request, context):
        """Check out"""
        nrics = request.nric.split(',')
        reply = tracetogether_pb2.Reply()
        for i in range(len(nrics)):
            StorageHandler().checkOut(nrics[i].strip(), request.time)
        reply.message = 'Successfully checked out'

        return reply

    def GetLocations(self, request, context):
        """Get SafeEntry location history"""
        history = StorageHandler().getLocations(request.nric)
        history = tabulate(history, headers=['Location', 'Check-in time', 'Check-out time'],tablefmt="pretty" )
        reply = tracetogether_pb2.Reply()
        reply.message = history + '\n'

        return reply

    def GetStatus(self, request, context):
        """Get Covid19 exposure status"""
        locations, release_date = StorageHandler().checkAffected(request.nric)
        reply = tracetogether_pb2.Reply()

        if locations is not None:
            locations = tabulate(locations, showindex=False, headers=['Location', 'Check-in time', 'Check-out time'],tablefmt="pretty" )
            reply.message = '\nDear {}, You have been identified to have some risk of exposure to COVID-19 cases over the past 14 days in the ' \
                            'following locations: \n'.format(request.nric)
            reply.message = reply.message + locations + '\n'
            reply.message = reply.message + 'You are strongly encouraged to monitor your health until {}.\n'.format(release_date)


        else:
            reply.message = 'No exposure alerts'

        return reply

    def AddCovidLocation(self, request, context):
        """Add Covid-19 location"""
        StorageHandler().addCovidLocation(request.location, request.time)
        return tracetogether_pb2.Reply(
            message='{} on {}, successfully added to list of affected locations'.format(request.location,
                                                                                        request.time))

    # Test concurrency
    def Test(self, request, context):
        for i in range(10):
            yield tracetogether_pb2.Reply(message='Message {}'.format(i))
            time.sleep(1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tracetogether_pb2_grpc.add_TraceTogetherServicer_to_server(TraceTogether(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    try:
        serve()
    except:
        print("The server cannot be started. Port is currently in use.")
