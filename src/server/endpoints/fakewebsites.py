from fastapi import APIRouter
from server.endpoints.models import FakeWebsites, FakeWebsites_url_purpose
from server.db.DB_manager import base_manager
router = APIRouter()


def get_FakeWebsites_id(id: int):
    res = base_manager.execute("SELECT * FROM fakewebsites WHERE websiteid=?", args=(id,), many=False)
    return FakeWebsites(id=res[0], url=res[1], purpose=res[2], victim_count=res[3], outcome=res[4], operation_id=res[5])


def get_FakeWebsites():
    res = base_manager.execute("select * from fakewebsites", args=(), many=True)
    fakewebsites = []
    for us in res:
        fakewebsites.append(FakeWebsites(id=us[0], url=us[1], purpose=us[2], victim_count=us[3], outcome=us[4], operation_id=us[5]))
    return res


def post_FakeWebsites(fake: FakeWebsites):
    res = base_manager.execute("insert into FakeWebsites (websiteid,url,purpose,victimcount,outcome,operationid) values(?,?,?,?,?,?)", args=(fake.id, fake.url, fake.purpose, fake.victim_count, fake.outcome,fake.operation_id))
    return res


def put_FakeWebsites(id: int, fake_update: FakeWebsites_url_purpose):
    res = base_manager.execute("update FakeWebsites set url=?,purpose=? where websiteid=?", args=(fake_update.url, fake_update.purpose, id))
    return res


def delete_FakeWebsites(id: int):
    res = base_manager.execute("delete from FakeWebsites where websiteid=?", args=(id,))
    return res
# Endpoints


@router.get('/FakeWebsites/{id}')
def get_FakeWebsites_endpoint(id: int):
    return get_FakeWebsites_id(id)


@router.get('/FakeWebsites')
def get_FakeWebsites_endpoint():
    return get_FakeWebsites()


@router.post('/new_FakeWebsites')
def new_FakeWebsites(fake: FakeWebsites):
    return post_FakeWebsites(fake)


@router.put('/FakeWebsites_url_purpose/{id}')
def put_FakeWebsites_param(id: int, fake_update: FakeWebsites_url_purpose):
    return put_FakeWebsites(id, fake_update)


@router.delete('/FakeWebsites/{id}')
def delete_FakeWebsites_id(id: int):
    return delete_FakeWebsites(id)
