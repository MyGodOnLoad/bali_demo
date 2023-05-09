import grpc
import pytest
from bali.utils import MessageToDict

from protos import user_pb2 as pb2
from protos import user_pb2_grpc as pb2_grpc
from main import app


@pytest.fixture(scope='module')
def grpc_servicer():
    return app._rpc_servicer()


@pytest.fixture(scope='module')
def grpc_channel():
    channel = grpc.insecure_channel('localhost:9080')
    yield channel
    channel.close()


@pytest.fixture(scope='module')
def grpc_stub(grpc_channel):
    return pb2_grpc.UserStub(grpc_channel)


def test_list_users(grpc_stub):
    request = pb2.ListRequest(limit=3, ordering='name')
    response = grpc_stub.ListUsers(request)
    print(MessageToDict(response))
