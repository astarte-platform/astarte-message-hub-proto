// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: astarteplatform/msghub/message_hub_service.proto

#include "astarteplatform/msghub/message_hub_service.pb.h"
#include "astarteplatform/msghub/message_hub_service.grpc.pb.h"

#include <functional>
#include <grpcpp/support/async_stream.h>
#include <grpcpp/support/async_unary_call.h>
#include <grpcpp/impl/channel_interface.h>
#include <grpcpp/impl/client_unary_call.h>
#include <grpcpp/support/client_callback.h>
#include <grpcpp/support/message_allocator.h>
#include <grpcpp/support/method_handler.h>
#include <grpcpp/impl/rpc_service_method.h>
#include <grpcpp/support/server_callback.h>
#include <grpcpp/impl/server_callback_handlers.h>
#include <grpcpp/server_context.h>
#include <grpcpp/impl/service_type.h>
#include <grpcpp/support/sync_stream.h>
namespace astarteplatform {
namespace msghub {

static const char* MessageHub_method_names[] = {
  "/astarteplatform.msghub.MessageHub/Attach",
  "/astarteplatform.msghub.MessageHub/Send",
  "/astarteplatform.msghub.MessageHub/Detach",
  "/astarteplatform.msghub.MessageHub/AddInterfaces",
  "/astarteplatform.msghub.MessageHub/RemoveInterfaces",
  "/astarteplatform.msghub.MessageHub/GetProperties",
  "/astarteplatform.msghub.MessageHub/GetAllProperties",
  "/astarteplatform.msghub.MessageHub/GetProperty",
};

std::unique_ptr< MessageHub::Stub> MessageHub::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< MessageHub::Stub> stub(new MessageHub::Stub(channel, options));
  return stub;
}

MessageHub::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options)
  : channel_(channel), rpcmethod_Attach_(MessageHub_method_names[0], options.suffix_for_stats(),::grpc::internal::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_Send_(MessageHub_method_names[1], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Detach_(MessageHub_method_names[2], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_AddInterfaces_(MessageHub_method_names[3], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_RemoveInterfaces_(MessageHub_method_names[4], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetProperties_(MessageHub_method_names[5], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetAllProperties_(MessageHub_method_names[6], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetProperty_(MessageHub_method_names[7], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::ClientReader< ::astarteplatform::msghub::MessageHubEvent>* MessageHub::Stub::AttachRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::Node& request) {
  return ::grpc::internal::ClientReaderFactory< ::astarteplatform::msghub::MessageHubEvent>::Create(channel_.get(), rpcmethod_Attach_, context, request);
}

void MessageHub::Stub::async::Attach(::grpc::ClientContext* context, const ::astarteplatform::msghub::Node* request, ::grpc::ClientReadReactor< ::astarteplatform::msghub::MessageHubEvent>* reactor) {
  ::grpc::internal::ClientCallbackReaderFactory< ::astarteplatform::msghub::MessageHubEvent>::Create(stub_->channel_.get(), stub_->rpcmethod_Attach_, context, request, reactor);
}

::grpc::ClientAsyncReader< ::astarteplatform::msghub::MessageHubEvent>* MessageHub::Stub::AsyncAttachRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::Node& request, ::grpc::CompletionQueue* cq, void* tag) {
  return ::grpc::internal::ClientAsyncReaderFactory< ::astarteplatform::msghub::MessageHubEvent>::Create(channel_.get(), cq, rpcmethod_Attach_, context, request, true, tag);
}

::grpc::ClientAsyncReader< ::astarteplatform::msghub::MessageHubEvent>* MessageHub::Stub::PrepareAsyncAttachRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::Node& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncReaderFactory< ::astarteplatform::msghub::MessageHubEvent>::Create(channel_.get(), cq, rpcmethod_Attach_, context, request, false, nullptr);
}

::grpc::Status MessageHub::Stub::Send(::grpc::ClientContext* context, const ::astarteplatform::msghub::AstarteMessage& request, ::google::protobuf::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::astarteplatform::msghub::AstarteMessage, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Send_, context, request, response);
}

void MessageHub::Stub::async::Send(::grpc::ClientContext* context, const ::astarteplatform::msghub::AstarteMessage* request, ::google::protobuf::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::astarteplatform::msghub::AstarteMessage, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Send_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::Send(::grpc::ClientContext* context, const ::astarteplatform::msghub::AstarteMessage* request, ::google::protobuf::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Send_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::PrepareAsyncSendRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::AstarteMessage& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::google::protobuf::Empty, ::astarteplatform::msghub::AstarteMessage, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Send_, context, request);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::AsyncSendRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::AstarteMessage& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncSendRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status MessageHub::Stub::Detach(::grpc::ClientContext* context, const ::google::protobuf::Empty& request, ::google::protobuf::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::google::protobuf::Empty, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Detach_, context, request, response);
}

void MessageHub::Stub::async::Detach(::grpc::ClientContext* context, const ::google::protobuf::Empty* request, ::google::protobuf::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::google::protobuf::Empty, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Detach_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::Detach(::grpc::ClientContext* context, const ::google::protobuf::Empty* request, ::google::protobuf::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Detach_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::PrepareAsyncDetachRaw(::grpc::ClientContext* context, const ::google::protobuf::Empty& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::google::protobuf::Empty, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Detach_, context, request);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::AsyncDetachRaw(::grpc::ClientContext* context, const ::google::protobuf::Empty& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncDetachRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status MessageHub::Stub::AddInterfaces(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesJson& request, ::google::protobuf::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::astarteplatform::msghub::InterfacesJson, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_AddInterfaces_, context, request, response);
}

void MessageHub::Stub::async::AddInterfaces(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesJson* request, ::google::protobuf::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::astarteplatform::msghub::InterfacesJson, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_AddInterfaces_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::AddInterfaces(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesJson* request, ::google::protobuf::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_AddInterfaces_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::PrepareAsyncAddInterfacesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesJson& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::google::protobuf::Empty, ::astarteplatform::msghub::InterfacesJson, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_AddInterfaces_, context, request);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::AsyncAddInterfacesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesJson& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncAddInterfacesRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status MessageHub::Stub::RemoveInterfaces(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesName& request, ::google::protobuf::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::astarteplatform::msghub::InterfacesName, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_RemoveInterfaces_, context, request, response);
}

void MessageHub::Stub::async::RemoveInterfaces(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesName* request, ::google::protobuf::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::astarteplatform::msghub::InterfacesName, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_RemoveInterfaces_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::RemoveInterfaces(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesName* request, ::google::protobuf::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_RemoveInterfaces_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::PrepareAsyncRemoveInterfacesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesName& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::google::protobuf::Empty, ::astarteplatform::msghub::InterfacesName, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_RemoveInterfaces_, context, request);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* MessageHub::Stub::AsyncRemoveInterfacesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfacesName& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncRemoveInterfacesRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status MessageHub::Stub::GetProperties(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfaceName& request, ::astarteplatform::msghub::StoredProperties* response) {
  return ::grpc::internal::BlockingUnaryCall< ::astarteplatform::msghub::InterfaceName, ::astarteplatform::msghub::StoredProperties, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_GetProperties_, context, request, response);
}

void MessageHub::Stub::async::GetProperties(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfaceName* request, ::astarteplatform::msghub::StoredProperties* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::astarteplatform::msghub::InterfaceName, ::astarteplatform::msghub::StoredProperties, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetProperties_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::GetProperties(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfaceName* request, ::astarteplatform::msghub::StoredProperties* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetProperties_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::astarteplatform::msghub::StoredProperties>* MessageHub::Stub::PrepareAsyncGetPropertiesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfaceName& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::astarteplatform::msghub::StoredProperties, ::astarteplatform::msghub::InterfaceName, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_GetProperties_, context, request);
}

::grpc::ClientAsyncResponseReader< ::astarteplatform::msghub::StoredProperties>* MessageHub::Stub::AsyncGetPropertiesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::InterfaceName& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncGetPropertiesRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status MessageHub::Stub::GetAllProperties(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyFilter& request, ::astarteplatform::msghub::StoredProperties* response) {
  return ::grpc::internal::BlockingUnaryCall< ::astarteplatform::msghub::PropertyFilter, ::astarteplatform::msghub::StoredProperties, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_GetAllProperties_, context, request, response);
}

void MessageHub::Stub::async::GetAllProperties(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyFilter* request, ::astarteplatform::msghub::StoredProperties* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::astarteplatform::msghub::PropertyFilter, ::astarteplatform::msghub::StoredProperties, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetAllProperties_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::GetAllProperties(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyFilter* request, ::astarteplatform::msghub::StoredProperties* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetAllProperties_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::astarteplatform::msghub::StoredProperties>* MessageHub::Stub::PrepareAsyncGetAllPropertiesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyFilter& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::astarteplatform::msghub::StoredProperties, ::astarteplatform::msghub::PropertyFilter, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_GetAllProperties_, context, request);
}

::grpc::ClientAsyncResponseReader< ::astarteplatform::msghub::StoredProperties>* MessageHub::Stub::AsyncGetAllPropertiesRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyFilter& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncGetAllPropertiesRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status MessageHub::Stub::GetProperty(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyIdentifier& request, ::astarteplatform::msghub::AstartePropertyIndividual* response) {
  return ::grpc::internal::BlockingUnaryCall< ::astarteplatform::msghub::PropertyIdentifier, ::astarteplatform::msghub::AstartePropertyIndividual, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_GetProperty_, context, request, response);
}

void MessageHub::Stub::async::GetProperty(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyIdentifier* request, ::astarteplatform::msghub::AstartePropertyIndividual* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::astarteplatform::msghub::PropertyIdentifier, ::astarteplatform::msghub::AstartePropertyIndividual, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetProperty_, context, request, response, std::move(f));
}

void MessageHub::Stub::async::GetProperty(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyIdentifier* request, ::astarteplatform::msghub::AstartePropertyIndividual* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetProperty_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::astarteplatform::msghub::AstartePropertyIndividual>* MessageHub::Stub::PrepareAsyncGetPropertyRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyIdentifier& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::astarteplatform::msghub::AstartePropertyIndividual, ::astarteplatform::msghub::PropertyIdentifier, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_GetProperty_, context, request);
}

::grpc::ClientAsyncResponseReader< ::astarteplatform::msghub::AstartePropertyIndividual>* MessageHub::Stub::AsyncGetPropertyRaw(::grpc::ClientContext* context, const ::astarteplatform::msghub::PropertyIdentifier& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncGetPropertyRaw(context, request, cq);
  result->StartCall();
  return result;
}

MessageHub::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[0],
      ::grpc::internal::RpcMethod::SERVER_STREAMING,
      new ::grpc::internal::ServerStreamingHandler< MessageHub::Service, ::astarteplatform::msghub::Node, ::astarteplatform::msghub::MessageHubEvent>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::Node* req,
             ::grpc::ServerWriter<::astarteplatform::msghub::MessageHubEvent>* writer) {
               return service->Attach(ctx, req, writer);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[1],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::astarteplatform::msghub::AstarteMessage, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::AstarteMessage* req,
             ::google::protobuf::Empty* resp) {
               return service->Send(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[2],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::google::protobuf::Empty, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::google::protobuf::Empty* req,
             ::google::protobuf::Empty* resp) {
               return service->Detach(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[3],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::astarteplatform::msghub::InterfacesJson, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::InterfacesJson* req,
             ::google::protobuf::Empty* resp) {
               return service->AddInterfaces(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[4],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::astarteplatform::msghub::InterfacesName, ::google::protobuf::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::InterfacesName* req,
             ::google::protobuf::Empty* resp) {
               return service->RemoveInterfaces(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[5],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::astarteplatform::msghub::InterfaceName, ::astarteplatform::msghub::StoredProperties, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::InterfaceName* req,
             ::astarteplatform::msghub::StoredProperties* resp) {
               return service->GetProperties(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[6],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::astarteplatform::msghub::PropertyFilter, ::astarteplatform::msghub::StoredProperties, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::PropertyFilter* req,
             ::astarteplatform::msghub::StoredProperties* resp) {
               return service->GetAllProperties(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      MessageHub_method_names[7],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< MessageHub::Service, ::astarteplatform::msghub::PropertyIdentifier, ::astarteplatform::msghub::AstartePropertyIndividual, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](MessageHub::Service* service,
             ::grpc::ServerContext* ctx,
             const ::astarteplatform::msghub::PropertyIdentifier* req,
             ::astarteplatform::msghub::AstartePropertyIndividual* resp) {
               return service->GetProperty(ctx, req, resp);
             }, this)));
}

MessageHub::Service::~Service() {
}

::grpc::Status MessageHub::Service::Attach(::grpc::ServerContext* context, const ::astarteplatform::msghub::Node* request, ::grpc::ServerWriter< ::astarteplatform::msghub::MessageHubEvent>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::Send(::grpc::ServerContext* context, const ::astarteplatform::msghub::AstarteMessage* request, ::google::protobuf::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::Detach(::grpc::ServerContext* context, const ::google::protobuf::Empty* request, ::google::protobuf::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::AddInterfaces(::grpc::ServerContext* context, const ::astarteplatform::msghub::InterfacesJson* request, ::google::protobuf::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::RemoveInterfaces(::grpc::ServerContext* context, const ::astarteplatform::msghub::InterfacesName* request, ::google::protobuf::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::GetProperties(::grpc::ServerContext* context, const ::astarteplatform::msghub::InterfaceName* request, ::astarteplatform::msghub::StoredProperties* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::GetAllProperties(::grpc::ServerContext* context, const ::astarteplatform::msghub::PropertyFilter* request, ::astarteplatform::msghub::StoredProperties* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status MessageHub::Service::GetProperty(::grpc::ServerContext* context, const ::astarteplatform::msghub::PropertyIdentifier* request, ::astarteplatform::msghub::AstartePropertyIndividual* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace astarteplatform
}  // namespace msghub

