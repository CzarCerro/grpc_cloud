# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracetogether.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tracetogether.proto\x12\rtracetogether\"\x17\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t2N\n\rTraceTogether\x12=\n\x0b\x43heckStatus\x12\x16.tracetogether.Request\x1a\x14.tracetogether.Reply\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:tracetogether.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:tracetogether.Reply)
  })
_sym_db.RegisterMessage(Reply)

_TRACETOGETHER = DESCRIPTOR.services_by_name['TraceTogether']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=38
  _REQUEST._serialized_end=61
  _REPLY._serialized_start=63
  _REPLY._serialized_end=87
  _TRACETOGETHER._serialized_start=89
  _TRACETOGETHER._serialized_end=167
# @@protoc_insertion_point(module_scope)