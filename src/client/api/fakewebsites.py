import requests


def get_fakewebsites():
    response = requests.get('http://127.0.0.1:8000/fakewebsites_start/FakeWebsites')
    post_data = response.json()
    print(post_data)


get_fakewebsites()


def get_id_fakewebsites():
    id_fakewebsites = input("enter the ID of the fakewebsites you want to receive")
    response = requests.get(f'http://127.0.0.1:8000/fakewebsites_start/FakeWebsites/{id_fakewebsites}')
    post_data = response.json()
    print(post_data)


get_id_fakewebsites()


def post_fakewebsites():
    id_fakewebsites = input("ID")
    url = input("url")
    purpose = input("purpose")
    victim_count = input("victim_count")
    outcome = input("outcome")
    operation_id = input("operation_id")
    data = {"id": id_fakewebsites,
            "url": url,
            "purpose": purpose,
            "victim_count": victim_count,
            "outcome": outcome,
            "operation_id": operation_id}
    response = requests.post('http://127.0.0.1:8000/fakewebsites_start/new_FakeWebsites', json=data)
    print(response.json())


post_fakewebsites()


def update_fakewebsites():
    id_fakewebsites = input("enter the ID of the fakewebsites you want to update")
    url = input("url")
    purpose = input("purpose")
    data = {'url': url,
            'purpose':purpose}
    response = requests.put(f'http://127.0.0.1:8000/fakewebsites_start/FakeWebsites_url_purpose/{id_fakewebsites}', json=data)
    new_post_data = response.json()
    print(new_post_data)


update_fakewebsites()


def delete_id_fakewebsites():
    id_fakewebsites = input("enter the ID of the fakewebsites you want to delete")
    response = requests.delete(f'http://127.0.0.1:8000/fakewebsites_start/FakeWebsites/{id_fakewebsites}')
    post_data = response.json()
    print(post_data)


delete_id_fakewebsites()
