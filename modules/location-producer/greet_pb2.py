# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x05greet\".\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"R\n\x16\x44\x65layedLocationMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\'\n\x07request\x18\x02 \x03(\x0b\x32\x16.greet.LocationMessage\"E\n\x0c\x44\x65layedReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12$\n\x07request\x18\x02 \x03(\x0b\x32\x13.greet.HelloRequest\"u\n\x0fLocationMessage\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x13\n\x0bperson_name\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\t\"\x07\n\x05\x45mpty\"@\n\x13LocationMessageList\x12)\n\tlocations\x18\x01 \x03(\x0b\x32\x16.greet.LocationMessage2\x99\x02\n\x08Location\x12\x37\n\x05SayHi\x12\x16.greet.LocationMessage\x1a\x16.greet.LocationMessage\x12@\n\x0cParrotSaysHi\x12\x16.greet.LocationMessage\x1a\x16.greet.LocationMessage0\x01\x12M\n\x12\x43hattyClientSaysHi\x12\x16.greet.LocationMessage\x1a\x1d.greet.DelayedLocationMessage(\x01\x12\x43\n\rInteractingHi\x12\x16.greet.LocationMessage\x1a\x16.greet.LocationMessage(\x01\x30\x01\x32\xff\x01\n\x07Greeter\x12\x32\n\x08SayHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply\x12;\n\x0fParrotSaysHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply0\x01\x12\x43\n\x15\x43hattyClientSaysHello\x12\x13.greet.HelloRequest\x1a\x13.greet.DelayedReply(\x01\x12>\n\x10InteractingHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply(\x01\x30\x01\x32|\n\x0fLocationService\x12\x38\n\x06\x43reate\x12\x16.greet.LocationMessage\x1a\x16.greet.LocationMessage\x12/\n\x03Get\x12\x0c.greet.Empty\x1a\x1a.greet.LocationMessageListb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=22
  _HELLOREQUEST._serialized_end=68
  _HELLOREPLY._serialized_start=70
  _HELLOREPLY._serialized_end=99
  _DELAYEDLOCATIONMESSAGE._serialized_start=101
  _DELAYEDLOCATIONMESSAGE._serialized_end=183
  _DELAYEDREPLY._serialized_start=185
  _DELAYEDREPLY._serialized_end=254
  _LOCATIONMESSAGE._serialized_start=256
  _LOCATIONMESSAGE._serialized_end=373
  _EMPTY._serialized_start=375
  _EMPTY._serialized_end=382
  _LOCATIONMESSAGELIST._serialized_start=384
  _LOCATIONMESSAGELIST._serialized_end=448
  _LOCATION._serialized_start=451
  _LOCATION._serialized_end=732
  _GREETER._serialized_start=735
  _GREETER._serialized_end=990
  _LOCATIONSERVICE._serialized_start=992
  _LOCATIONSERVICE._serialized_end=1116
# @@protoc_insertion_point(module_scope)