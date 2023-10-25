from fastapi import APIRouter
from server.endpoints.models import Staff, Staff_name_surname
from server.db.DB_manager import base_manager
router = APIRouter()


def get_staff_id(id: int):
    res = base_manager.execute("SELECT * FROM staff WHERE id=?", args=(id,), many=False)
    return Staff(id=res[0], name=res[1], surname=res[2], post_id=res[3], user_id=res[4])


def get_staff():
    res = base_manager.execute("select * from staff", args=(), many=True)
    staffs = []
    for us in res:
        staffs.append(Staff(id=us[0], name=us[1], surname=us[2], post_id=us[3], user_id=us[4]))
    return res


def post_staff(staff: Staff):
    res = base_manager.execute("insert into staff(id,name,surname,post_id,user_id) values(?,?,?,?,?)", args=(staff.id, staff.name, staff.surname, staff.post_id, staff.user_id))
    return res


def put_staff(id: int, staff_update: Staff_name_surname):
    res = base_manager.execute("update staff set name=?,surname=? where id=?", args=(staff_update.name, staff_update.surname, id))
    return res


def delete_staff(id: int):
    res = base_manager.execute("delete from staff where id=?", args=(id,))
    return res
# Endpoints


@router.get('/staff/{id}')
def get_staff_endpoint(id: int):
    return get_staff_id(id)


@router.get('/staffs')
def get_staff_endpoint():
    return get_staff()


@router.post('/new_staff')
def new_staff(staff: Staff):
    return post_staff(staff)


@router.put('/staff_name_surname/{id}')
def put_staff_name(id: int, staff_update: Staff_name_surname):
    return put_staff(id, staff_update)


@router.delete('/staff/{id}')
def delete_staff_id(id: int):
    return delete_staff(id)
