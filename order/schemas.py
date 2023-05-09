from bali.schemas import model_to_schema
from models import Order

OrderSchema = model_to_schema(Order, partial=True)
