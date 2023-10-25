from fastapi import APIRouter
from server.endpoints.models import Operations,Operations_update
from server.db.DB_manager import base_manager
router = APIRouter()


def get_Operations_id(id: int):
    res = base_manager.execute("SELECT * FROM Operations WHERE Operationid=?", args=(id,), many=False)
    return Operations(id=res[0], name=res[1], type=res[2], success=res[3])


def get_Operations():
    res = base_manager.execute("select * from Operations", args=(), many=True)
    operations = []
    for us in res:
        operations.append(Operations(id=us[0], name=us[1], type=us[2], success=us[3]))
    return res


def post_Operations(operations: Operations):
    res = base_manager.execute("insert into Operations (Operationid,name,type,success) values(?,?,?,?)", args=(operations.id, operations.name, operations.type, operations.success))
    return res


def put_Operations(id: int, operations_update: Operations_update):
    res = base_manager.execute("update Operations set name=?,type=? where Operationid=?", args=(operations_update.name, operations_update.type, id))
    return res


def delete_Operations(id: int):
    res = base_manager.execute("delete from Operations where Operationid=?", args=(id,))
    return res
# Endpoints


@router.get('/Operations/{id}')
def get_Operations_endpoint(id: int):
    return get_Operations_id(id)


@router.get('/Operations')
def get_Operations_endpoint():
    return get_Operations()


@router.post('/new_Operations')
def new_Operations(operations: Operations):
    return post_Operations(operations)


@router.put('/Operations_name_type/{id}')
def put_Operations_param(id: int, fake_update: Operations_update):
    return put_Operations(id, fake_update)


@router.delete('/Operations/{id}')
def delete_Operations_id(id: int):
    return delete_Operations(id)