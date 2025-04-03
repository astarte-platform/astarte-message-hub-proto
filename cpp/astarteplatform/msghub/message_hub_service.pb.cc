// Generated by the protocol buffer compiler.  DO NOT EDIT!
// NO CHECKED-IN PROTOBUF GENCODE
// source: astarteplatform/msghub/message_hub_service.proto
// Protobuf C++ Version: 5.29.0

#include "astarteplatform/msghub/message_hub_service.pb.h"

#include <algorithm>
#include <type_traits>
#include "google/protobuf/io/coded_stream.h"
#include "google/protobuf/generated_message_tctable_impl.h"
#include "google/protobuf/extension_set.h"
#include "google/protobuf/generated_message_util.h"
#include "google/protobuf/wire_format_lite.h"
#include "google/protobuf/descriptor.h"
#include "google/protobuf/generated_message_reflection.h"
#include "google/protobuf/reflection_ops.h"
#include "google/protobuf/wire_format.h"
// @@protoc_insertion_point(includes)

// Must be included last.
#include "google/protobuf/port_def.inc"
PROTOBUF_PRAGMA_INIT_SEG
namespace _pb = ::google::protobuf;
namespace _pbi = ::google::protobuf::internal;
namespace _fl = ::google::protobuf::internal::field_layout;
namespace astarteplatform {
namespace msghub {
}  // namespace msghub
}  // namespace astarteplatform
static constexpr const ::_pb::EnumDescriptor**
    file_level_enum_descriptors_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto = nullptr;
static constexpr const ::_pb::ServiceDescriptor**
    file_level_service_descriptors_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto = nullptr;
const ::uint32_t TableStruct_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto::offsets[1] = {};
static constexpr ::_pbi::MigrationSchema* schemas = nullptr;
static constexpr ::_pb::Message* const* file_default_instances = nullptr;
const char descriptor_table_protodef_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto[] ABSL_ATTRIBUTE_SECTION_VARIABLE(
    protodesc_cold) = {
    "\n0astarteplatform/msghub/message_hub_ser"
    "vice.proto\022\026astarteplatform.msghub\032\033goog"
    "le/protobuf/empty.proto\032,astarteplatform"
    "/msghub/astarte_message.proto\032!astartepl"
    "atform/msghub/node.proto\032&astarteplatfor"
    "m/msghub/interface.proto\032%astarteplatfor"
    "m/msghub/property.proto2\300\005\n\nMessageHub\022S"
    "\n\006Attach\022\034.astarteplatform.msghub.Node\032\'"
    ".astarteplatform.msghub.MessageHubEvent\""
    "\0000\001\022H\n\004Send\022&.astarteplatform.msghub.Ast"
    "arteMessage\032\026.google.protobuf.Empty\"\000\022:\n"
    "\006Detach\022\026.google.protobuf.Empty\032\026.google"
    ".protobuf.Empty\"\000\022Q\n\rAddInterfaces\022&.ast"
    "arteplatform.msghub.InterfacesJson\032\026.goo"
    "gle.protobuf.Empty\"\000\022T\n\020RemoveInterfaces"
    "\022&.astarteplatform.msghub.InterfacesName"
    "\032\026.google.protobuf.Empty\"\000\022c\n\rGetPropert"
    "ies\022&.astarteplatform.msghub.InterfacesN"
    "ame\032(.astarteplatform.msghub.StoredPrope"
    "rties\"\000\022f\n\020GetAllProperties\022&.astartepla"
    "tform.msghub.PropertyFilter\032(.astartepla"
    "tform.msghub.StoredProperties\"\000\022a\n\013GetPr"
    "operty\022*.astarteplatform.msghub.Property"
    "Identifier\032$.astarteplatform.msghub.Prop"
    "ertyData\"\000b\006proto3"
};
static const ::_pbi::DescriptorTable* const descriptor_table_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto_deps[5] =
    {
        &::descriptor_table_astarteplatform_2fmsghub_2fastarte_5fmessage_2eproto,
        &::descriptor_table_astarteplatform_2fmsghub_2finterface_2eproto,
        &::descriptor_table_astarteplatform_2fmsghub_2fnode_2eproto,
        &::descriptor_table_astarteplatform_2fmsghub_2fproperty_2eproto,
        &::descriptor_table_google_2fprotobuf_2fempty_2eproto,
};
static ::absl::once_flag descriptor_table_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto_once;
PROTOBUF_CONSTINIT const ::_pbi::DescriptorTable descriptor_table_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto = {
    false,
    false,
    978,
    descriptor_table_protodef_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto,
    "astarteplatform/msghub/message_hub_service.proto",
    &descriptor_table_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto_once,
    descriptor_table_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto_deps,
    5,
    0,
    schemas,
    file_default_instances,
    TableStruct_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto::offsets,
    file_level_enum_descriptors_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto,
    file_level_service_descriptors_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto,
};
namespace astarteplatform {
namespace msghub {
// @@protoc_insertion_point(namespace_scope)
}  // namespace msghub
}  // namespace astarteplatform
namespace google {
namespace protobuf {
}  // namespace protobuf
}  // namespace google
// @@protoc_insertion_point(global_scope)
PROTOBUF_ATTRIBUTE_INIT_PRIORITY2 static ::std::false_type
    _static_init2_ PROTOBUF_UNUSED =
        (::_pbi::AddDescriptors(&descriptor_table_astarteplatform_2fmsghub_2fmessage_5fhub_5fservice_2eproto),
         ::std::false_type{});
#include "google/protobuf/port_undef.inc"
