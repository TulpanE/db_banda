from fastapi import APIRouter
from server.endpoints.models import Victim, Victim_name
from server.db.DB_manager import base_manager
router = APIRouter()


def get_victim_id(id: int):
    res = base_manager.execute("SELECT * FROM Victim WHERE victimid=?", args=(id,), many=False)
    return Victim(id=res[0], name=res[1], location_id=res[2], loss_amount=res[3], incident_date=res[4])


def get_victim():
    res = base_manager.execute("select * from victim", args=(), many=True)
    victims = []
    for us in res:
        victims.append(Victim(id=us[0], name=us[1], location_id=us[2], loss_amount=us[3], incident_date=us[4]))
    return res


def post_victim(victim: Victim):
    res = base_manager.execute("insert into Victim(victimid,name,locationid,lossamount,incidentdate) values(?,?,?,?,?)", args=(victim.id, victim.name, victim.location_id, victim.loss_amount,victim.incident_date))
    return res


def put_victim(id: int, victim_update: Victim_name):
    res = base_manager.execute("update Victim set name=? where victimid=?", args=(victim_update.name, id))
    return res


def delete_victim(id: int):
    res = base_manager.execute("delete from Victim where victimid=?", args=(id,))
    return res


# Endpoints
@router.get('/victims/{id}')
def get_victim_endpoint(id: int):
    return get_victim_id(id)


@router.get('/victims')
def get_victim_endpoint():
    return get_victim()


@router.post('/new_victim')
def new_victim(victim: Victim):
    return post_victim(victim)


@router.put('/victim_name/{id}')
def patch_victim_name(id: int, victim_update: Victim_name):
    return put_victim(id, victim_update)


@router.delete('/victim/{id}')
def delete_victim_id(id: int):
    return delete_victim(id)
