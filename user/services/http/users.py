from typing import List

from bali import APIRouter
from bali.db.operators import get_filters_expr
from fastapi import Header

from models import User
from schemas import UserSchema

ROUTER = APIRouter()


@ROUTER.get('/users', response_model=UserSchema)
def get_users(*, channel: str = Header(None)) -> List[UserSchema]:
    """"""
    filters = {
        'offset': 0,
        'limit': 10
    }
    return User.query().filter(*get_filters_expr(User, **filters)).all()
