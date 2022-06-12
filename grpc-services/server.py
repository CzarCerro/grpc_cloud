# server

from concurrent import futures
import logging
import grpc
import tracetogether_pb2
import tracetogether_pb2_grpc
import time
from storagehandler import StorageHandler


class TraceTogether(tracetogether_pb2_grpc.TraceTogetherServicer):

    def Login(self, request, context):
        """Login with name and NRIC"""
        status = StorageHandler().verify(request.name,request.nric)
        reply = tracetogether_pb2.Reply()
        if status:
            reply.message = 'Successfully logged in as {}, {}.'.format(request.name, request.nric)

        else:
            reply.message = 'User {}, {} does not exist.'.format(request.name, request.nric)

        return reply

            # Check in

    def CheckIn(self, request, context):
        """Check in"""
        return tracetogether_pb2.Reply(
            message='{}, {} successfully checked in at {} on {}'.format(request.name, request.nric, request.location,
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
    serve()
