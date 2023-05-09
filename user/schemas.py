from typing import Optional

from bali import Schema
from bali.schemas import model_to_schema, CreateRequest

from models import User


# class UserSchema(Schema):
#     id: Optional[int]
#     name: Optional[str]
#     age: Optional[int]


# UserSchema = model_to_schema(User, partial=True)  # exclude=['id']

class UserSchema(model_to_schema(User, partial=True)):

    def validate_name(self):
        pass


class LoginSchema(Schema):
    name: str
    password: str
