from bali.backends.filters import FilterBackend
from bali.backends.ordering import OrderingBackend
from bali.backends.search import SearchBackend
from bali.paginate import paginate
from fastapi_pagination import LimitOffsetPage

from bali.schemas import ListRequest

from bali.decorators import action

from bali import ModelResource, Resource

from models import User
from schemas import UserSchema, LoginSchema


class UserResource(ModelResource):
    model = User
    schema = UserSchema

    # permission_classes = [IsAuthenticated]
    filter_backends = (FilterBackend, OrderingBackend, SearchBackend)
    filter_fields = ('name',)
    search_fields = ('name', 'id')
    ordering_fields = ('name', 'created_time', 'updated_time')

    @action(methods=['POST'], detail=False)
    def login(self, schema_in: LoginSchema = None):
        return f'{schema_in.name} 登录成功 密码为{schema_in.password}'

    @action(methods=['GET'], detail=False, response_model=LimitOffsetPage[schema])
    async def info(self, schema_in: ListRequest):
        # user = await User.aio.first(name=schema_in.name)
        # users = User.query().filter(User.name == schema_in.name).order_by(-User.id).all()  # -User.id只能int类型字段使用
        # users = User.query().filter_by(name=schema_in.name).order_by(-User.id).all()
        # users = User.query().filter(User.name.like('%zhang%')).all()

        # async with db.async_session() as async_session:
        #     stmt = User.query().filter(*get_filters_expr(User, **schema_in.filters)).order_by(getattr(User, 'name').asc())
        #     # stmt = select(User).filter(*get_filters_expr(User, **schema_in.filters)).order_by(User.name.desc())
        #     # stmt = select(User).where(User.name == schema_in.name).order_by(User.id.desc())
        #     result = await async_session.execute(stmt)
        # users = result.scalars().all()

        users = self.get_filters(schema_in)
        return paginate(users)


class LoginResource(Resource):

    @action(methods=['POST'], detail=False)
    async def login(self, schema_in: LoginSchema = None):  # 若使用create，需指定正确的response_model
        return f'{schema_in.name} 登录成功 密码为{schema_in.password}'


# sync
# user = User.io.create(username=username)
# async
# user = await User.aio.create(username=username)

# sync
# User.query().order_by(-User.id).first()

# async with db.async_session() as session:
#     result = await session.execute(
#         select(User).where(User.username == username)
#     )
#     user = result.scalars().first()
#
# # 由于 user 是在 async_session 的 context 里面查询出来的
# # 所以 user 的自带的实例方法(save, delete 等)都自动转换成了异步方法
# await user.save()
