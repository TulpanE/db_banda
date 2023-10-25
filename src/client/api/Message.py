import requests


def get_message():
    response = requests.get('http://127.0.0.1:8000/message_start/Messages')
    post_data = response.json()
    print(post_data)


get_message()


def get_id_message():
    id_message = input("enter the ID of the message you want to receive: ")
    response = requests.get(f'http://127.0.0.1:8000/message_start/Messages/{id_message}')
    post_data = response.json()
    print(post_data)


get_id_message()


def post_message():
    id = input("ID: ")
    content = input("Content: ")
    status = input("Status: ")
    operation_id = input("Operation_id: ")
    data = {"id": id,
            "content": content,
            "status": status,
            "operation_id": operation_id
            }
    response = requests.post('http://127.0.0.1:8000/message_start/new_Messages', json=data)
    print(response.json())


post_message()


def update_message():
    id_message = input("enter the ID of the message you want to update: ")
    content = input("Content: ")
    status = input("Status: ")
    data = {'content': content,
            "status":status}
    response = requests.put(f'http://127.0.0.1:8000/message_start/Messages_content_status/{id_message}', json=data)
    new_post_data = response.json()
    print(new_post_data)


update_message()


def delete_id_message():
    id_message = input("enter the ID of the message you want to delete: ")
    response = requests.delete(f'http://127.0.0.1:8000/message_start/Messages/{id_message}')
    post_data = response.json()
    print(post_data)


delete_id_message()
