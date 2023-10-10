# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from astarteplatform.msghub import astarte_message_pb2 as astarteplatform_dot_msghub_dot_astarte__message__pb2
from astarteplatform.msghub import message_hub_service_pb2 as astarteplatform_dot_msghub_dot_message__hub__service__pb2
from astarteplatform.msghub import node_pb2 as astarteplatform_dot_msghub_dot_node__pb2


class MessageHubStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Attach = channel.unary_stream(
                '/astarteplatform.msghub.MessageHub/Attach',
                request_serializer=astarteplatform_dot_msghub_dot_node__pb2.Node.SerializeToString,
                response_deserializer=astarteplatform_dot_msghub_dot_astarte__message__pb2.AstarteMessageResult.FromString,
                )
        self.Send = channel.unary_unary(
                '/astarteplatform.msghub.MessageHub/Send',
                request_serializer=astarteplatform_dot_msghub_dot_astarte__message__pb2.AstarteMessage.SerializeToString,
                response_deserializer=astarteplatform_dot_msghub_dot_message__hub__service__pb2.MessageHubResult.FromString,
                )
        self.Detach = channel.unary_unary(
                '/astarteplatform.msghub.MessageHub/Detach',
                request_serializer=astarteplatform_dot_msghub_dot_node__pb2.Node.SerializeToString,
                response_deserializer=astarteplatform_dot_msghub_dot_message__hub__service__pb2.MessageHubResult.FromString,
                )


class MessageHubServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Attach(self, request, context):
        """This function should be used to attach a node to an instance of the Astarte message hub.
        Returns a data stream from the Astarte message hub.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Send(self, request, context):
        """This function should be used to send an `AstarteMessage` to Astarte. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Detach(self, request, context):
        """This function should be used to detach a node from an instance of the Astarte message hub. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageHubServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Attach': grpc.unary_stream_rpc_method_handler(
                    servicer.Attach,
                    request_deserializer=astarteplatform_dot_msghub_dot_node__pb2.Node.FromString,
                    response_serializer=astarteplatform_dot_msghub_dot_astarte__message__pb2.AstarteMessageResult.SerializeToString,
            ),
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=astarteplatform_dot_msghub_dot_astarte__message__pb2.AstarteMessage.FromString,
                    response_serializer=astarteplatform_dot_msghub_dot_message__hub__service__pb2.MessageHubResult.SerializeToString,
            ),
            'Detach': grpc.unary_unary_rpc_method_handler(
                    servicer.Detach,
                    request_deserializer=astarteplatform_dot_msghub_dot_node__pb2.Node.FromString,
                    response_serializer=astarteplatform_dot_msghub_dot_message__hub__service__pb2.MessageHubResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'astarteplatform.msghub.MessageHub', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageHub(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Attach(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/astarteplatform.msghub.MessageHub/Attach',
            astarteplatform_dot_msghub_dot_node__pb2.Node.SerializeToString,
            astarteplatform_dot_msghub_dot_astarte__message__pb2.AstarteMessageResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/astarteplatform.msghub.MessageHub/Send',
            astarteplatform_dot_msghub_dot_astarte__message__pb2.AstarteMessage.SerializeToString,
            astarteplatform_dot_msghub_dot_message__hub__service__pb2.MessageHubResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Detach(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/astarteplatform.msghub.MessageHub/Detach',
            astarteplatform_dot_msghub_dot_node__pb2.Node.SerializeToString,
            astarteplatform_dot_msghub_dot_message__hub__service__pb2.MessageHubResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
