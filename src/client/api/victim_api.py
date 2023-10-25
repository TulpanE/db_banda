import requests


def get_victims():
    response = requests.get('http://127.0.0.1:8000/victim_start/victims')
    post_data = response.json()
    print(post_data)


get_victims()


def get_id_victim():
    id_victim = input("enter the ID of the victim you want to receive")
    response = requests.get(f'http://127.0.0.1:8000/victim_start/victims/{id_victim}')
    post_data = response.json()
    print(post_data)


get_id_victim()


def post_victim():
    id = input("ID")
    name = input("name")
    location_id = input("location_id")
    loss_amount = input("loss_amount")
    incident_date = input("incident_date")
    data = {"id": id,
            "name": name,
            "location_id": location_id,
            "loss_amount": loss_amount,
            "incident_date": incident_date}
    response = requests.post('http://127.0.0.1:8000/victim_start/new_victim', json=data)
    print(response.json())


post_victim()


def update_victim():
    id_victim = input("enter the ID of the victim you want to update")
    name = input("Name")
    data = {'name': name}
    response = requests.put(f'http://127.0.0.1:8000/victim_start/victim_name/{id_victim}', json=data)
    new_post_data = response.json()
    print(new_post_data)


update_victim()


def delete_id_victim():
    id_victim = input("enter the ID of the victim you want to delete")
    response = requests.delete(f'http://127.0.0.1:8000/victim_start/victim/{id_victim}')
    post_data = response.json()
    print(post_data)


delete_id_victim()
