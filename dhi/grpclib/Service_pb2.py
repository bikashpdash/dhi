# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Service.proto',
  package='grpclib',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rService.proto\x12\x07grpclib\"\x07\n\x05\x45mpty\"&\n\x04Pong\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"\x92\x01\n\x0cMatchRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0e\n\x06tokens\x18\x02 \x01(\t\x12/\n\x05level\x18\x03 \x01(\x0e\x32 .grpclib.MatchRequest.MatchLevel\"0\n\nMatchLevel\x12\n\n\x06simple\x10\x00\x12\x0b\n\x07partial\x10\x01\x12\t\n\x05token\x10\x02\"\x1e\n\rMatchResponse\x12\r\n\x05ratio\x18\x01 \x01(\x05\x32l\n\x07Service\x12\'\n\x04Ping\x12\x0e.grpclib.Empty\x1a\r.grpclib.Pong\"\x00\x12\x38\n\x05Match\x12\x15.grpclib.MatchRequest\x1a\x16.grpclib.MatchResponse\"\x00\x62\x06proto3'
)



_MATCHREQUEST_MATCHLEVEL = _descriptor.EnumDescriptor(
  name='MatchLevel',
  full_name='grpclib.MatchRequest.MatchLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='simple', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='partial', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='token', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=174,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_MATCHREQUEST_MATCHLEVEL)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpclib.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=26,
  serialized_end=33,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='grpclib.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='grpclib.Pong.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='grpclib.Pong.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=35,
  serialized_end=73,
)


_MATCHREQUEST = _descriptor.Descriptor(
  name='MatchRequest',
  full_name='grpclib.MatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='grpclib.MatchRequest.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='grpclib.MatchRequest.tokens', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='grpclib.MatchRequest.level', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MATCHREQUEST_MATCHLEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=222,
)


_MATCHRESPONSE = _descriptor.Descriptor(
  name='MatchResponse',
  full_name='grpclib.MatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ratio', full_name='grpclib.MatchResponse.ratio', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=224,
  serialized_end=254,
)

_MATCHREQUEST.fields_by_name['level'].enum_type = _MATCHREQUEST_MATCHLEVEL
_MATCHREQUEST_MATCHLEVEL.containing_type = _MATCHREQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
DESCRIPTOR.message_types_by_name['MatchRequest'] = _MATCHREQUEST
DESCRIPTOR.message_types_by_name['MatchResponse'] = _MATCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'Service_pb2'
  # @@protoc_insertion_point(class_scope:grpclib.Empty)
  })
_sym_db.RegisterMessage(Empty)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'Service_pb2'
  # @@protoc_insertion_point(class_scope:grpclib.Pong)
  })
_sym_db.RegisterMessage(Pong)

MatchRequest = _reflection.GeneratedProtocolMessageType('MatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _MATCHREQUEST,
  '__module__' : 'Service_pb2'
  # @@protoc_insertion_point(class_scope:grpclib.MatchRequest)
  })
_sym_db.RegisterMessage(MatchRequest)

MatchResponse = _reflection.GeneratedProtocolMessageType('MatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRESPONSE,
  '__module__' : 'Service_pb2'
  # @@protoc_insertion_point(class_scope:grpclib.MatchResponse)
  })
_sym_db.RegisterMessage(MatchResponse)



_SERVICE = _descriptor.ServiceDescriptor(
  name='Service',
  full_name='grpclib.Service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=256,
  serialized_end=364,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='grpclib.Service.Ping',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_PONG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Match',
    full_name='grpclib.Service.Match',
    index=1,
    containing_service=None,
    input_type=_MATCHREQUEST,
    output_type=_MATCHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['Service'] = _SERVICE

# @@protoc_insertion_point(module_scope)
