import requests


def get_login_user(login, password):
    data = {"login": login,
            "password": password}
    response = requests.get('http://127.0.0.1:8000/users_start/users_login', json=data)
    post_data = response.json()
    return post_data


#def get_all_user():
#    response = requests.get('http://127.0.0.1:8000/users_start/users')
#    post_data = response.json()
#    print(post_data)
#
#
#get_all_user()
#
#
#def get_id_user():
#    id_user = input("enter the ID of the user you want to receive")
#    response = requests.get(f'http://127.0.0.1:8000/users_start/users/{id_user}')
#    post_data = response.json()
#    print(post_data)
#
#
#get_id_user()
#
#
#def post_user():
#    id_user = input("ID")
#    login = input("Login")
#    password = input("password")
#    data = {"id": id_user,
#            "login": login,
#            "password": password}
#    response = requests.post('http://127.0.0.1:8000/users_start/new_user', json=data)
#    print(response.json())
#
#
#post_user()
#
#
#def update_user():
#    id_user = input("enter the ID of the user you want to update")
#    login = input("Login")
#    data = {'login': login}
#    response = requests.put(f'http://127.0.0.1:8000/users_start/user_login/{id_user}', json=data)
#    new_post_data = response.json()
#    print(new_post_data)


#update_user()
#
#def delete_user():
#    id_user = input("enter the ID of the user you want to delete")
#    response = requests.delete(f'http://127.0.0.1:8000/users_start/user/{id_user}')
#    new_post_data = response.json()
#    print(new_post_data)
#
#
#delete_user()
