# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import tasc_pb2 as tasc__pb2


class TascStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartTransaction = channel.unary_unary(
                '/tasc.Tasc/StartTransaction',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=tasc__pb2.TransactionTag.FromString,
                )
        self.Read = channel.unary_unary(
                '/tasc.Tasc/Read',
                request_serializer=tasc__pb2.TascRequest.SerializeToString,
                response_deserializer=tasc__pb2.TascRequest.FromString,
                )
        self.Write = channel.unary_unary(
                '/tasc.Tasc/Write',
                request_serializer=tasc__pb2.TascRequest.SerializeToString,
                response_deserializer=tasc__pb2.TascRequest.FromString,
                )
        self.CommitTransaction = channel.unary_unary(
                '/tasc.Tasc/CommitTransaction',
                request_serializer=tasc__pb2.TransactionTag.SerializeToString,
                response_deserializer=tasc__pb2.TransactionTag.FromString,
                )
        self.AbortTransaction = channel.unary_unary(
                '/tasc.Tasc/AbortTransaction',
                request_serializer=tasc__pb2.TransactionTag.SerializeToString,
                response_deserializer=tasc__pb2.TransactionTag.FromString,
                )


class TascServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartTransaction(self, request, context):
        """Starts a new transaction in the system and returns a unique
        transaction ID. Updates made in the context of this transaction
        will not be persisted until CommitTransaction is called.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Fetch a value from the storage engine.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Tentatively write a value or batch of values to the storage engine.
        The writes are not committed until CommitTransaction is called.
        Calling AbortTransaction will drop these writes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitTransaction(self, request, context):
        """Commits the buffered writes to the storage engine. Commit
        will only happen if there are no concurrent write conflicts
        under snapshot isolation semantics.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AbortTransaction(self, request, context):
        """Aborts all of the updates by this transaction and the transaction
        is ended.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TascServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTransaction,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=tasc__pb2.TransactionTag.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=tasc__pb2.TascRequest.FromString,
                    response_serializer=tasc__pb2.TascRequest.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=tasc__pb2.TascRequest.FromString,
                    response_serializer=tasc__pb2.TascRequest.SerializeToString,
            ),
            'CommitTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.CommitTransaction,
                    request_deserializer=tasc__pb2.TransactionTag.FromString,
                    response_serializer=tasc__pb2.TransactionTag.SerializeToString,
            ),
            'AbortTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.AbortTransaction,
                    request_deserializer=tasc__pb2.TransactionTag.FromString,
                    response_serializer=tasc__pb2.TransactionTag.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tasc.Tasc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Tasc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasc.Tasc/StartTransaction',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            tasc__pb2.TransactionTag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasc.Tasc/Read',
            tasc__pb2.TascRequest.SerializeToString,
            tasc__pb2.TascRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasc.Tasc/Write',
            tasc__pb2.TascRequest.SerializeToString,
            tasc__pb2.TascRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasc.Tasc/CommitTransaction',
            tasc__pb2.TransactionTag.SerializeToString,
            tasc__pb2.TransactionTag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AbortTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasc.Tasc/AbortTransaction',
            tasc__pb2.TransactionTag.SerializeToString,
            tasc__pb2.TransactionTag.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
