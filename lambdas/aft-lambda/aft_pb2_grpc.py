# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import aft_pb2 as aft__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AftStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartTransaction = channel.unary_unary(
        '/Aft/StartTransaction',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=aft__pb2.TransactionTag.FromString,
        )
    self.Write = channel.unary_unary(
        '/Aft/Write',
        request_serializer=aft__pb2.KeyRequest.SerializeToString,
        response_deserializer=aft__pb2.KeyRequest.FromString,
        )
    self.Read = channel.unary_unary(
        '/Aft/Read',
        request_serializer=aft__pb2.KeyRequest.SerializeToString,
        response_deserializer=aft__pb2.KeyRequest.FromString,
        )
    self.CommitTransaction = channel.unary_unary(
        '/Aft/CommitTransaction',
        request_serializer=aft__pb2.TransactionTag.SerializeToString,
        response_deserializer=aft__pb2.TransactionTag.FromString,
        )
    self.AbortTransaction = channel.unary_unary(
        '/Aft/AbortTransaction',
        request_serializer=aft__pb2.TransactionTag.SerializeToString,
        response_deserializer=aft__pb2.TransactionTag.FromString,
        )


class AftServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StartTransaction(self, request, context):
    """Starts a new transaction in the system and returns a unique transaction
    ID. The updates made in the context of this transaction will not be
    persisted until CommitTransaction is called.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Write(self, request, context):
    """Tentatively write a value or batch of values to the storage engine. These
    writes will not be committed until CommitTransaction is called. If
    AbortTransaction is called, these writes will be dropped.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    """Retrieve a value from the storage engine.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CommitTransaction(self, request, context):
    """Commits buffered writes to the storage engine. The commit is not
    guaranteed to succeed and may depend on the isolation mechanisms being
    used in order to determine whether the transactions updates and reads are
    valid.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AbortTransaction(self, request, context):
    """Aborts all of the updates made by this transaction. The buffered updates
    will be dropped, and the transaction in the underlying engine will be
    closed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AftServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.StartTransaction,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=aft__pb2.TransactionTag.SerializeToString,
      ),
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=aft__pb2.KeyRequest.FromString,
          response_serializer=aft__pb2.KeyRequest.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=aft__pb2.KeyRequest.FromString,
          response_serializer=aft__pb2.KeyRequest.SerializeToString,
      ),
      'CommitTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.CommitTransaction,
          request_deserializer=aft__pb2.TransactionTag.FromString,
          response_serializer=aft__pb2.TransactionTag.SerializeToString,
      ),
      'AbortTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.AbortTransaction,
          request_deserializer=aft__pb2.TransactionTag.FromString,
          response_serializer=aft__pb2.TransactionTag.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Aft', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
