from starlette.routing import Route, WebSocketRoute

from bali import Bali

from resources import UserResource, LoginResource
from services.http import users


app = Bali(title='user')
app.register([UserResource, LoginResource])
# app.include_router(users.ROUTER, prefix='/user')  # 只在http中生效


@app.on_event('startup')
async def start_app():
    print('routers are:')
    for route in app.routes:
        if isinstance(route, Route):
            print('http router %s: %s %s' %
                        (route.name, route.path, route.methods))
        elif isinstance(route, WebSocketRoute):
            print('websocket router %s: %s ' %
                        (route.name, route.path))
    # middlewares
    print('middlewares are:')
    for middleware in app.user_middleware:
        print(repr(middleware))


if __name__ == '__main__':
    # app.start()
    app.launch(http=True)
