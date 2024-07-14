# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos import author_pb2 as protos_dot_author__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/author_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AuthorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAuthor = channel.unary_unary(
                '/author.AuthorService/CreateAuthor',
                request_serializer=protos_dot_author__pb2.CreateAuthorRequest.SerializeToString,
                response_deserializer=protos_dot_author__pb2.SingleAuthorResponse.FromString,
                _registered_method=True)
        self.RetrieveAuthor = channel.unary_unary(
                '/author.AuthorService/RetrieveAuthor',
                request_serializer=protos_dot_author__pb2.RetrieveAuthorRequest.SerializeToString,
                response_deserializer=protos_dot_author__pb2.SingleAuthorResponse.FromString,
                _registered_method=True)
        self.UpdateAuthor = channel.unary_unary(
                '/author.AuthorService/UpdateAuthor',
                request_serializer=protos_dot_author__pb2.UpdateAuthorRequest.SerializeToString,
                response_deserializer=protos_dot_author__pb2.SingleAuthorResponse.FromString,
                _registered_method=True)
        self.DeleteAuthor = channel.unary_unary(
                '/author.AuthorService/DeleteAuthor',
                request_serializer=protos_dot_author__pb2.DeleteAuthorRequest.SerializeToString,
                response_deserializer=protos_dot_author__pb2.SingleAuthorResponse.FromString,
                _registered_method=True)


class AuthorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAuthor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveAuthor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAuthor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAuthor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAuthor': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAuthor,
                    request_deserializer=protos_dot_author__pb2.CreateAuthorRequest.FromString,
                    response_serializer=protos_dot_author__pb2.SingleAuthorResponse.SerializeToString,
            ),
            'RetrieveAuthor': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveAuthor,
                    request_deserializer=protos_dot_author__pb2.RetrieveAuthorRequest.FromString,
                    response_serializer=protos_dot_author__pb2.SingleAuthorResponse.SerializeToString,
            ),
            'UpdateAuthor': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAuthor,
                    request_deserializer=protos_dot_author__pb2.UpdateAuthorRequest.FromString,
                    response_serializer=protos_dot_author__pb2.SingleAuthorResponse.SerializeToString,
            ),
            'DeleteAuthor': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAuthor,
                    request_deserializer=protos_dot_author__pb2.DeleteAuthorRequest.FromString,
                    response_serializer=protos_dot_author__pb2.SingleAuthorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'author.AuthorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('author.AuthorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AuthorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAuthor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/author.AuthorService/CreateAuthor',
            protos_dot_author__pb2.CreateAuthorRequest.SerializeToString,
            protos_dot_author__pb2.SingleAuthorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RetrieveAuthor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/author.AuthorService/RetrieveAuthor',
            protos_dot_author__pb2.RetrieveAuthorRequest.SerializeToString,
            protos_dot_author__pb2.SingleAuthorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateAuthor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/author.AuthorService/UpdateAuthor',
            protos_dot_author__pb2.UpdateAuthorRequest.SerializeToString,
            protos_dot_author__pb2.SingleAuthorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteAuthor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/author.AuthorService/DeleteAuthor',
            protos_dot_author__pb2.DeleteAuthorRequest.SerializeToString,
            protos_dot_author__pb2.SingleAuthorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
