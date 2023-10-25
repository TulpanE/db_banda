from fastapi import APIRouter
from server.endpoints.models import Location, Location_update
from server.db.DB_manager import base_manager
router = APIRouter()


def get_Location_id(id: int):
    res = base_manager.execute("SELECT * FROM Locations WHERE Locationid=?", args=(id,), many=False)
    return Location(id=res[0], address=res[1])


def get_Locations():
    res = base_manager.execute("select * from Locations", args=(), many=True)
    messages = []
    for us in res:
        messages.append(Location(id=us[0], address=us[1]))
    return res


def post_Location(location: Location):
    res = base_manager.execute("insert into Locations (Locationid,address) values(?,?)", args=(location.id, location.address))
    return res


def put_Location(id: int, location_update: Location_update):
    res = base_manager.execute("update Locations set address=? where Locationid=?", args=(location_update.address, id))
    return res


def delete_Location(id: int):
    res = base_manager.execute("delete from Locations where Locationid=?", args=(id,))
    return res
# Endpoints


@router.get('/Location/{id}')
def get_Location_endpoint(id: int):
    return get_Location_id(id)


@router.get('/Location')
def get_Location_endpoint():
    return get_Locations()


@router.post('/new_Location')
def new_Location(location: Location):
    return post_Location(location)


@router.put('/Location_address/{id}')
def put_Location_param(id: int, location_update: Location_update):
    return put_Location(id, location_update)


@router.delete('/Location/{id}')
def delete_Location_id(id: int):
    return delete_Location(id)