# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Position.proto

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
  name='Position.proto',
  package='',
  serialized_pb=_b('\n\x0ePosition.proto\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"%\n\x06PosReq\x12\x1b\n\x08position\x18\x01 \x02(\x0b\x32\t.Position\"2\n\x06PosRes\x12\x0b\n\x03uid\x18\x01 \x02(\r\x12\x1b\n\x08position\x18\x02 \x02(\x0b\x32\t.Position')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Position.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Position.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='Position.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=61,
)


_POSREQ = _descriptor.Descriptor(
  name='PosReq',
  full_name='PosReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='PosReq.position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=100,
)


_POSRES = _descriptor.Descriptor(
  name='PosRes',
  full_name='PosRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='PosRes.uid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='PosRes.position', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=152,
)

_POSREQ.fields_by_name['position'].message_type = _POSITION
_POSRES.fields_by_name['position'].message_type = _POSITION
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['PosReq'] = _POSREQ
DESCRIPTOR.message_types_by_name['PosRes'] = _POSRES

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'Position_pb2'
  # @@protoc_insertion_point(class_scope:Position)
  ))
_sym_db.RegisterMessage(Position)

PosReq = _reflection.GeneratedProtocolMessageType('PosReq', (_message.Message,), dict(
  DESCRIPTOR = _POSREQ,
  __module__ = 'Position_pb2'
  # @@protoc_insertion_point(class_scope:PosReq)
  ))
_sym_db.RegisterMessage(PosReq)

PosRes = _reflection.GeneratedProtocolMessageType('PosRes', (_message.Message,), dict(
  DESCRIPTOR = _POSRES,
  __module__ = 'Position_pb2'
  # @@protoc_insertion_point(class_scope:PosRes)
  ))
_sym_db.RegisterMessage(PosRes)


# @@protoc_insertion_point(module_scope)
