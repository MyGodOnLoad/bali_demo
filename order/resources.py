from bali.decorators import action

from bali import ModelResource
from client import user_client
from models import Order
from schemas import OrderSchema


class OrderResource(ModelResource):
    model = Order
    schema = OrderSchema

    @action(methods=['GET'], detail=True)
    def get_user_by_order_id(self, pk=None):
        order = self.model.query().filter_by(id=pk).first()
        user_id = order.user_id
        user = user_client.get_user_by_id(int(user_id)).get('data')
        order.user = user
        return order
