from fastapi import APIRouter
from server.endpoints.models import Messages, Messages_update
from server.db.DB_manager import base_manager
router = APIRouter()


def get_Messages_id(id: int):
    res = base_manager.execute("SELECT * FROM Messages WHERE Messageid=?", args=(id,), many=False)
    return Messages(id=res[0], content=res[1], status=res[2], operation_id=res[3])


def get_Messages():
    res = base_manager.execute("select * from Messages", args=(), many=True)
    messages = []
    for us in res:
        messages.append(Messages(id=us[0], content=us[1], status=us[2], operation_id=us[3]))
    return res


def post_Messages(messages: Messages):
    res = base_manager.execute("insert into Messages (Messageid,content,status,operationid) values(?,?,?,?)", args=(messages.id, messages.content, messages.status, messages.operation_id))
    return res


def put_Messages(id: int, message_update: Messages_update):
    res = base_manager.execute("update Messages set content=?,status=? where Messageid=?", args=(message_update.content, message_update.status, id))
    return res


def delete_Messages(id: int):
    res = base_manager.execute("delete from Messages where Messageid=?", args=(id,))
    return res
# Endpoints


@router.get('/Messages/{id}')
def get_Messages_endpoint(id: int):
    return get_Messages_id(id)


@router.get('/Messages')
def get_Messages_endpoint():
    return get_Messages()


@router.post('/new_Messages')
def new_Messages(message: Messages):
    return post_Messages(message)


@router.put('/Messages_content_status/{id}')
def put_Messages_param(id: int, message_update: Messages_update):
    return put_Messages(id, message_update)


@router.delete('/Messages/{id}')
def delete_Messages_id(id: int):
    return delete_Messages(id)