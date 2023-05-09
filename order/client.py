import grpc
from bali.utils import MessageToDict

from protos import user_pb2 as pb2
from protos import user_pb2_grpc as pb2_grpc


class UserClient(object):

    def get_users(self, kwargs):
        with grpc.insecure_channel('localhost:9080') as channel:
            stub = pb2_grpc.UserStub(channel)
            response = stub.ListUsers(pb2.ListRequest(**kwargs))
        return MessageToDict(response)

    def get_user_by_id(self, pk):
        with grpc.insecure_channel('localhost:9080') as channel:
            stub = pb2_grpc.UserStub(channel)
            response = stub.GetUser(pb2.GetRequest(id=pk))
        return MessageToDict(response)


user_client = UserClient()
