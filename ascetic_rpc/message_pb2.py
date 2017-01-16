# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\x12\x07message\";\n\x07Request\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x11\n\tSignature\x18\x02 \x01(\t\x12\x0f\n\x07RawBody\x18\x03 \x01(\x0c\"i\n\x08Response\x12\x1f\n\x05\x45rror\x18\x01 \x01(\x0b\x32\x0e.message.ErrorH\x00\x12\x0f\n\x05RawOK\x18\x02 \x01(\x0cH\x00\x12\x10\n\x06Stream\x18\x04 \x01(\x08H\x00\x12\x11\n\tSignature\x18\x03 \x01(\tB\x06\n\x04\x42ody\"P\n\x05\x43hunk\x12\x1f\n\x05\x45rror\x18\x01 \x01(\x0b\x32\x0e.message.ErrorH\x00\x12\x0f\n\x05RawOK\x18\x02 \x01(\x0cH\x00\x12\r\n\x03\x45OF\x18\x03 \x01(\x08H\x00\x42\x06\n\x04\x42ody\"\xb1\x01\n\x05\x45rror\x12\x0f\n\x07Message\x18\x01 \x01(\t\x12!\n\x04Type\x18\x02 \x01(\x0e\x32\x13.message.Error.type\"t\n\x04type\x12\x0f\n\x0b\x41PPLICATION\x10\x00\x12\x11\n\rSERIALIZATION\x10\x01\x12\x0c\n\x08PROTOCOL\x10\x02\x12\x0b\n\x07NETWORK\x10\x03\x12\x10\n\x0cSERVER_PANIC\x10\x04\x12\x0b\n\x07TIMEOUT\x10\x05\x12\x0e\n\nBAD_METHOD\x10\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ERROR_TYPE = _descriptor.EnumDescriptor(
  name='type',
  full_name='message.Error.type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APPLICATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERIALIZATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOCOL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETWORK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_PANIC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_METHOD', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=338,
  serialized_end=454,
)
_sym_db.RegisterEnumDescriptor(_ERROR_TYPE)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='message.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='message.Request.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Signature', full_name='message.Request.Signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RawBody', full_name='message.Request.RawBody', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=85,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='message.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='message.Response.Error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RawOK', full_name='message.Response.RawOK', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Stream', full_name='message.Response.Stream', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Signature', full_name='message.Response.Signature', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Body', full_name='message.Response.Body',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=87,
  serialized_end=192,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='message.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='message.Chunk.Error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RawOK', full_name='message.Chunk.RawOK', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EOF', full_name='message.Chunk.EOF', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Body', full_name='message.Chunk.Body',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=194,
  serialized_end=274,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='message.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='message.Error.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='message.Error.Type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERROR_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=454,
)

_RESPONSE.fields_by_name['Error'].message_type = _ERROR
_RESPONSE.oneofs_by_name['Body'].fields.append(
  _RESPONSE.fields_by_name['Error'])
_RESPONSE.fields_by_name['Error'].containing_oneof = _RESPONSE.oneofs_by_name['Body']
_RESPONSE.oneofs_by_name['Body'].fields.append(
  _RESPONSE.fields_by_name['RawOK'])
_RESPONSE.fields_by_name['RawOK'].containing_oneof = _RESPONSE.oneofs_by_name['Body']
_RESPONSE.oneofs_by_name['Body'].fields.append(
  _RESPONSE.fields_by_name['Stream'])
_RESPONSE.fields_by_name['Stream'].containing_oneof = _RESPONSE.oneofs_by_name['Body']
_CHUNK.fields_by_name['Error'].message_type = _ERROR
_CHUNK.oneofs_by_name['Body'].fields.append(
  _CHUNK.fields_by_name['Error'])
_CHUNK.fields_by_name['Error'].containing_oneof = _CHUNK.oneofs_by_name['Body']
_CHUNK.oneofs_by_name['Body'].fields.append(
  _CHUNK.fields_by_name['RawOK'])
_CHUNK.fields_by_name['RawOK'].containing_oneof = _CHUNK.oneofs_by_name['Body']
_CHUNK.oneofs_by_name['Body'].fields.append(
  _CHUNK.fields_by_name['EOF'])
_CHUNK.fields_by_name['EOF'].containing_oneof = _CHUNK.oneofs_by_name['Body']
_ERROR.fields_by_name['Type'].enum_type = _ERROR_TYPE
_ERROR_TYPE.containing_type = _ERROR
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['Error'] = _ERROR

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Response)
  ))
_sym_db.RegisterMessage(Response)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), dict(
  DESCRIPTOR = _CHUNK,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Chunk)
  ))
_sym_db.RegisterMessage(Chunk)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Error)
  ))
_sym_db.RegisterMessage(Error)


# @@protoc_insertion_point(module_scope)
