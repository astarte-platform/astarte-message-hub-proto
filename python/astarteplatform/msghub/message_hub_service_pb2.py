# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: astarteplatform/msghub/message_hub_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'astarteplatform/msghub/message_hub_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from astarteplatform.msghub import astarte_data_pb2 as astarteplatform_dot_msghub_dot_astarte__data__pb2
from astarteplatform.msghub import astarte_message_pb2 as astarteplatform_dot_msghub_dot_astarte__message__pb2
from astarteplatform.msghub import node_pb2 as astarteplatform_dot_msghub_dot_node__pb2
from astarteplatform.msghub import interface_pb2 as astarteplatform_dot_msghub_dot_interface__pb2
from astarteplatform.msghub import property_pb2 as astarteplatform_dot_msghub_dot_property__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0astarteplatform/msghub/message_hub_service.proto\x12\x16\x61starteplatform.msghub\x1a\x1bgoogle/protobuf/empty.proto\x1a)astarteplatform/msghub/astarte_data.proto\x1a,astarteplatform/msghub/astarte_message.proto\x1a!astarteplatform/msghub/node.proto\x1a&astarteplatform/msghub/interface.proto\x1a%astarteplatform/msghub/property.proto2\xcc\x05\n\nMessageHub\x12S\n\x06\x41ttach\x12\x1c.astarteplatform.msghub.Node\x1a\'.astarteplatform.msghub.MessageHubEvent\"\x00\x30\x01\x12H\n\x04Send\x12&.astarteplatform.msghub.AstarteMessage\x1a\x16.google.protobuf.Empty\"\x00\x12:\n\x06\x44\x65tach\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\rAddInterfaces\x12&.astarteplatform.msghub.InterfacesJson\x1a\x16.google.protobuf.Empty\"\x00\x12T\n\x10RemoveInterfaces\x12&.astarteplatform.msghub.InterfacesName\x1a\x16.google.protobuf.Empty\"\x00\x12\x62\n\rGetProperties\x12%.astarteplatform.msghub.InterfaceName\x1a(.astarteplatform.msghub.StoredProperties\"\x00\x12\x66\n\x10GetAllProperties\x12&.astarteplatform.msghub.PropertyFilter\x1a(.astarteplatform.msghub.StoredProperties\"\x00\x12n\n\x0bGetProperty\x12*.astarteplatform.msghub.PropertyIdentifier\x1a\x31.astarteplatform.msghub.AstartePropertyIndividual\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'astarteplatform.msghub.message_hub_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEHUB']._serialized_start=309
  _globals['_MESSAGEHUB']._serialized_end=1025
# @@protoc_insertion_point(module_scope)
