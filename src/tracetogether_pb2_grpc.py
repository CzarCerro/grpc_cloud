# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tracetogether_pb2 as tracetogether__pb2


class TraceTogetherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckStatus = channel.unary_unary(
                '/tracetogether.TraceTogether/CheckStatus',
                request_serializer=tracetogether__pb2.Request.SerializeToString,
                response_deserializer=tracetogether__pb2.Reply.FromString,
                )


class TraceTogetherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TraceTogetherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckStatus,
                    request_deserializer=tracetogether__pb2.Request.FromString,
                    response_serializer=tracetogether__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tracetogether.TraceTogether', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TraceTogether(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tracetogether.TraceTogether/CheckStatus',
            tracetogether__pb2.Request.SerializeToString,
            tracetogether__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
