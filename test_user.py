import requests


# data = {}
# data["id"] = 1
# data["username"] = "Ivi"
# data["firstName"] = "Iveta"
# data["lastName"] = "Abaeva"
# data["email"] = "test1@mail.ru"
# data["password"] = "test123"
# data["phone"] = "89998888888"
# data["userStatus"] = 1

data = {
    'id': 1,
    'username': 'Ivi',
    'firstName': 'Iveta',
    'lastName': 'Abaeva',
    'email': 'test1@mail.ru',
    'password': 'test123',
    'phone': '89998888888',
    'userStatus': 1
}


def test_user_post():
    url = "https://petstore.swagger.io/v2/user"
    response = requests.post(url=url, json=data)
    response_body = response.json()
    assert response_body["code"] == 200


def test_user_put():
    url_put = "https://petstore.swagger.io/v2/user/ivi"
    data["username"] = "kivi"
    response = requests.put(url_put, json=data)
    response_body = response.json()
    assert response_body["code"] == 200


def test_user_get():
    url = "https://petstore.swagger.io/v2/user/kivi"
    response = requests.get(url)
    response_body = response.json()
    assert response_body['username'] == 'kivi'

def test_user_delete():
    url = "https://petstore.swagger.io/v2/user/kivi"
    response = requests.delete(url)
    response_body = response.json()
    assert response_body["code"] == 200
