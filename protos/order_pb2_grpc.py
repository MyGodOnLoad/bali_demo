# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import order_pb2 as protos_dot_order__pb2


class OrderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListOrders = channel.unary_unary(
                '/order.Order/ListOrders',
                request_serializer=protos_dot_order__pb2.ListRequest.SerializeToString,
                response_deserializer=protos_dot_order__pb2.ListResponse.FromString,
                )
        self.CreateOrder = channel.unary_unary(
                '/order.Order/CreateOrder',
                request_serializer=protos_dot_order__pb2.CreateRequest.SerializeToString,
                response_deserializer=protos_dot_order__pb2.ItemResponse.FromString,
                )
        self.GetOrder = channel.unary_unary(
                '/order.Order/GetOrder',
                request_serializer=protos_dot_order__pb2.GetRequest.SerializeToString,
                response_deserializer=protos_dot_order__pb2.ItemResponse.FromString,
                )
        self.UpdateOrder = channel.unary_unary(
                '/order.Order/UpdateOrder',
                request_serializer=protos_dot_order__pb2.UpdateRequest.SerializeToString,
                response_deserializer=protos_dot_order__pb2.ItemResponse.FromString,
                )
        self.DeleteOrder = channel.unary_unary(
                '/order.Order/DeleteOrder',
                request_serializer=protos_dot_order__pb2.DeleteRequest.SerializeToString,
                response_deserializer=protos_dot_order__pb2.ResultResponse.FromString,
                )


class OrderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrders,
                    request_deserializer=protos_dot_order__pb2.ListRequest.FromString,
                    response_serializer=protos_dot_order__pb2.ListResponse.SerializeToString,
            ),
            'CreateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrder,
                    request_deserializer=protos_dot_order__pb2.CreateRequest.FromString,
                    response_serializer=protos_dot_order__pb2.ItemResponse.SerializeToString,
            ),
            'GetOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrder,
                    request_deserializer=protos_dot_order__pb2.GetRequest.FromString,
                    response_serializer=protos_dot_order__pb2.ItemResponse.SerializeToString,
            ),
            'UpdateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOrder,
                    request_deserializer=protos_dot_order__pb2.UpdateRequest.FromString,
                    response_serializer=protos_dot_order__pb2.ItemResponse.SerializeToString,
            ),
            'DeleteOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOrder,
                    request_deserializer=protos_dot_order__pb2.DeleteRequest.FromString,
                    response_serializer=protos_dot_order__pb2.ResultResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'order.Order', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Order(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.Order/ListOrders',
            protos_dot_order__pb2.ListRequest.SerializeToString,
            protos_dot_order__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.Order/CreateOrder',
            protos_dot_order__pb2.CreateRequest.SerializeToString,
            protos_dot_order__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.Order/GetOrder',
            protos_dot_order__pb2.GetRequest.SerializeToString,
            protos_dot_order__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.Order/UpdateOrder',
            protos_dot_order__pb2.UpdateRequest.SerializeToString,
            protos_dot_order__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/order.Order/DeleteOrder',
            protos_dot_order__pb2.DeleteRequest.SerializeToString,
            protos_dot_order__pb2.ResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)