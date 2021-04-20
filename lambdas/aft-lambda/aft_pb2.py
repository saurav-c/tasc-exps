# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aft.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aft.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\taft.proto\x1a\x1bgoogle/protobuf/empty.proto\"Q\n\x0eTransactionTag\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.TransactionStatus\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\xdd\x01\n\x11TransactionRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\"\n\x06status\x18\x03 \x01(\x0e\x32\x12.TransactionStatus\x12\x11\n\treplicaId\x18\x04 \x01(\t\x12\x10\n\x08writeSet\x18\x05 \x03(\t\x12\x30\n\x07readSet\x18\x06 \x03(\x0b\x32\x1f.TransactionRecord.ReadSetEntry\x1a.\n\x0cReadSetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x0fTransactionList\x12#\n\x07records\x18\x01 \x03(\x0b\x32\x12.TransactionRecord\" \n\x11TransactionIdList\x12\x0b\n\x03ids\x18\x01 \x03(\t\"d\n\nKeyRequest\x12\x0b\n\x03tid\x18\x01 \x01(\t\x12\"\n\x05pairs\x18\x02 \x03(\x0b\x32\x13.KeyRequest.KeyPair\x1a%\n\x07KeyPair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"a\n\x0cKeyValuePair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x15\n\rcowrittenKeys\x18\x03 \x03(\t\x12\x0b\n\x03tid\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03*<\n\x11TransactionStatus\x12\x0b\n\x07RUNNING\x10\x00\x12\r\n\tCOMMITTED\x10\x01\x12\x0b\n\x07\x41\x42ORTED\x10\x02\x32\xfe\x01\n\x03\x41\x66t\x12=\n\x10StartTransaction\x12\x16.google.protobuf.Empty\x1a\x0f.TransactionTag\"\x00\x12#\n\x05Write\x12\x0b.KeyRequest\x1a\x0b.KeyRequest\"\x00\x12\"\n\x04Read\x12\x0b.KeyRequest\x1a\x0b.KeyRequest\"\x00\x12\x37\n\x11\x43ommitTransaction\x12\x0f.TransactionTag\x1a\x0f.TransactionTag\"\x00\x12\x36\n\x10\x41\x62ortTransaction\x12\x0f.TransactionTag\x1a\x0f.TransactionTag\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMITTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=640,
  serialized_end=700,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
RUNNING = 0
COMMITTED = 1
ABORTED = 2



_TRANSACTIONTAG = _descriptor.Descriptor(
  name='TransactionTag',
  full_name='TransactionTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TransactionTag.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='TransactionTag.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='TransactionTag.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=123,
)


_TRANSACTIONRECORD_READSETENTRY = _descriptor.Descriptor(
  name='ReadSetEntry',
  full_name='TransactionRecord.ReadSetEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TransactionRecord.ReadSetEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='TransactionRecord.ReadSetEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=347,
)

_TRANSACTIONRECORD = _descriptor.Descriptor(
  name='TransactionRecord',
  full_name='TransactionRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TransactionRecord.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='TransactionRecord.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='TransactionRecord.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicaId', full_name='TransactionRecord.replicaId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeSet', full_name='TransactionRecord.writeSet', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readSet', full_name='TransactionRecord.readSet', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTIONRECORD_READSETENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=347,
)


_TRANSACTIONLIST = _descriptor.Descriptor(
  name='TransactionList',
  full_name='TransactionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='TransactionList.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=403,
)


_TRANSACTIONIDLIST = _descriptor.Descriptor(
  name='TransactionIdList',
  full_name='TransactionIdList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='TransactionIdList.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=437,
)


_KEYREQUEST_KEYPAIR = _descriptor.Descriptor(
  name='KeyPair',
  full_name='KeyRequest.KeyPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyRequest.KeyPair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='KeyRequest.KeyPair.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=539,
)

_KEYREQUEST = _descriptor.Descriptor(
  name='KeyRequest',
  full_name='KeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='KeyRequest.tid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pairs', full_name='KeyRequest.pairs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_KEYREQUEST_KEYPAIR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=539,
)


_KEYVALUEPAIR = _descriptor.Descriptor(
  name='KeyValuePair',
  full_name='KeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyValuePair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='KeyValuePair.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cowrittenKeys', full_name='KeyValuePair.cowrittenKeys', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tid', full_name='KeyValuePair.tid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='KeyValuePair.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=638,
)

_TRANSACTIONTAG.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_TRANSACTIONRECORD_READSETENTRY.containing_type = _TRANSACTIONRECORD
_TRANSACTIONRECORD.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_TRANSACTIONRECORD.fields_by_name['readSet'].message_type = _TRANSACTIONRECORD_READSETENTRY
_TRANSACTIONLIST.fields_by_name['records'].message_type = _TRANSACTIONRECORD
_KEYREQUEST_KEYPAIR.containing_type = _KEYREQUEST
_KEYREQUEST.fields_by_name['pairs'].message_type = _KEYREQUEST_KEYPAIR
DESCRIPTOR.message_types_by_name['TransactionTag'] = _TRANSACTIONTAG
DESCRIPTOR.message_types_by_name['TransactionRecord'] = _TRANSACTIONRECORD
DESCRIPTOR.message_types_by_name['TransactionList'] = _TRANSACTIONLIST
DESCRIPTOR.message_types_by_name['TransactionIdList'] = _TRANSACTIONIDLIST
DESCRIPTOR.message_types_by_name['KeyRequest'] = _KEYREQUEST
DESCRIPTOR.message_types_by_name['KeyValuePair'] = _KEYVALUEPAIR
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionTag = _reflection.GeneratedProtocolMessageType('TransactionTag', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONTAG,
  '__module__' : 'aft_pb2'
  # @@protoc_insertion_point(class_scope:TransactionTag)
  })
_sym_db.RegisterMessage(TransactionTag)

TransactionRecord = _reflection.GeneratedProtocolMessageType('TransactionRecord', (_message.Message,), {

  'ReadSetEntry' : _reflection.GeneratedProtocolMessageType('ReadSetEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTIONRECORD_READSETENTRY,
    '__module__' : 'aft_pb2'
    # @@protoc_insertion_point(class_scope:TransactionRecord.ReadSetEntry)
    })
  ,
  'DESCRIPTOR' : _TRANSACTIONRECORD,
  '__module__' : 'aft_pb2'
  # @@protoc_insertion_point(class_scope:TransactionRecord)
  })
_sym_db.RegisterMessage(TransactionRecord)
_sym_db.RegisterMessage(TransactionRecord.ReadSetEntry)

TransactionList = _reflection.GeneratedProtocolMessageType('TransactionList', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONLIST,
  '__module__' : 'aft_pb2'
  # @@protoc_insertion_point(class_scope:TransactionList)
  })
_sym_db.RegisterMessage(TransactionList)

TransactionIdList = _reflection.GeneratedProtocolMessageType('TransactionIdList', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONIDLIST,
  '__module__' : 'aft_pb2'
  # @@protoc_insertion_point(class_scope:TransactionIdList)
  })
_sym_db.RegisterMessage(TransactionIdList)

KeyRequest = _reflection.GeneratedProtocolMessageType('KeyRequest', (_message.Message,), {

  'KeyPair' : _reflection.GeneratedProtocolMessageType('KeyPair', (_message.Message,), {
    'DESCRIPTOR' : _KEYREQUEST_KEYPAIR,
    '__module__' : 'aft_pb2'
    # @@protoc_insertion_point(class_scope:KeyRequest.KeyPair)
    })
  ,
  'DESCRIPTOR' : _KEYREQUEST,
  '__module__' : 'aft_pb2'
  # @@protoc_insertion_point(class_scope:KeyRequest)
  })
_sym_db.RegisterMessage(KeyRequest)
_sym_db.RegisterMessage(KeyRequest.KeyPair)

KeyValuePair = _reflection.GeneratedProtocolMessageType('KeyValuePair', (_message.Message,), {
  'DESCRIPTOR' : _KEYVALUEPAIR,
  '__module__' : 'aft_pb2'
  # @@protoc_insertion_point(class_scope:KeyValuePair)
  })
_sym_db.RegisterMessage(KeyValuePair)


_TRANSACTIONRECORD_READSETENTRY._options = None

_AFT = _descriptor.ServiceDescriptor(
  name='Aft',
  full_name='Aft',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=703,
  serialized_end=957,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartTransaction',
    full_name='Aft.StartTransaction',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_TRANSACTIONTAG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='Aft.Write',
    index=1,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_KEYREQUEST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='Aft.Read',
    index=2,
    containing_service=None,
    input_type=_KEYREQUEST,
    output_type=_KEYREQUEST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CommitTransaction',
    full_name='Aft.CommitTransaction',
    index=3,
    containing_service=None,
    input_type=_TRANSACTIONTAG,
    output_type=_TRANSACTIONTAG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AbortTransaction',
    full_name='Aft.AbortTransaction',
    index=4,
    containing_service=None,
    input_type=_TRANSACTIONTAG,
    output_type=_TRANSACTIONTAG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AFT)

DESCRIPTOR.services_by_name['Aft'] = _AFT

# @@protoc_insertion_point(module_scope)