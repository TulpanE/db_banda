import requests


def get_all_staffs():
    response = requests.get('http://127.0.0.1:8000/staff_start/staffs')
    post_data = response.json()
    print(post_data)


get_all_staffs()


def get_id_staff():
    id_staff = input("enter the ID of the staff you want to receive")
    response = requests.get(f'http://127.0.0.1:8000/staff_start/staff/{id_staff}')
    post_data = response.json()
    print(post_data)


get_id_staff()


def post_staff():
    id_staff = input("ID")
    name = input("name")
    surname = input("surname")
    post_id = input("post_id")
    user_id = input("user_id")
    data = {"id": id_staff,
            "name": name,
            "surname": surname,
            "post_id": post_id,
            "user_id": user_id}
    response = requests.post('http://127.0.0.1:8000/staff_start/new_staff', json=data)
    print(response.json())


post_staff()


def update_staff():
    id_staff = input("enter the ID of the staff you want to update")
    name = input("Name")
    surname = input("Surname")
    data = {'name': name,
            'surname': surname}
    response = requests.put(f'http://127.0.0.1:8000/staff_start/staff_name_surname/{id_staff}', json=data)
    new_post_data = response.json()
    print(new_post_data)


update_staff()


def delete_id_staff():
    id_staff = input("enter the ID of the staff you want to dlete")
    response = requests.delete(f'http://127.0.0.1:8000/staff_start/staff/{id_staff}')
    post_data = response.json()
    print(post_data)


delete_id_staff()
