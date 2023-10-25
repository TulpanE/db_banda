from fastapi import APIRouter
from server.endpoints.models import User, User_login, User_form
from server.db.DB_manager import base_manager
router = APIRouter()


def get_user_id(id: int):
    user = base_manager.execute("SELECT * FROM user WHERE id=?", args=(id,), many=False)
    return User(id=user[0], login=user[1], password=user[2])


def get_user():
    res = base_manager.execute("select * from user", args=(), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2]))
    return res


def get_login_user(user: User_form):
    res = base_manager.execute("select * from user where login=?", args=(user.login,), many=True)
    return res


def post_user(user: User):
    res = base_manager.execute("insert into user(id,login,password) values(?,?,?)", args=(user.id, user.login, user.password))
    return res


def put_user(id: int, user_update: User_login):
    res = base_manager.execute("update user set login=? where id=?", args=(user_update.login, id))
    return res


def delete_user(id: int):
    res = base_manager.execute("delete from user where id=?", args=(id,))
    return res


# Endpoints
@router.get('/users/{id}')
def get_user_endpoint(id: int):
    return get_user_id(id)


@router.get('/users')
def get_user_endpoint():
    return get_user()


@router.get('/users_login')
def user_login(user: User_form):
    return get_login_user(user)


@router.post('/new_user')
def new_user(user: User):
    return post_user(user)


@router.put('/user_login/{id}')
def put_user_name(id: int, user_update: User_login):
    return put_user(id, user_update)


@router.delete('/user/{id}')
def delete_user_id(id: int):
    return delete_user(id)










