import requests
import resources.urls as urls



data = {}
data["name"] = "Sbercat"
data["photoUrls"] = ["Photosberkot"]
data["category"] = {}
data["category"]["name"] = "cats"
data["status"] = "pending"
print(data)

def test_pet_post():
    response = requests.post(urls.main_url, json=data)
    response_body = response.json()
    print()
    print("result =", response_body)
    assert response_body["id"] is not None

def test_pet_put():
    url = "https://petstore.swagger.io/v2/pet/"
    data["name"] = "Iveta"
    data["id"] = 19
    response = requests.put(url, json=data)
    response_body = response.json()
    print(response_body)
    assert response_body["name"] == "Iveta"

def test_pet_post2():
    url = "https://petstore.swagger.io/v2/pet/19/"
 #   data["status"] = "sold"
    response = requests.post(url, data = {"name":"Sberdog", "status": "sold"})
    response_body = response.json()
    print(response_body)
    assert response_body["code"] == 200

def test_pet_get():
    url = "https://petstore.swagger.io/v2/pet/19/"
    response = requests.get(url)
    response_body = response.json()
    print(response_body)
    assert response_body["name"] == "Sberdog"

def test_pet_get2():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=pending"
    response = requests.get(url)
    response_body = response.json()
    print()
    print(response_body)

def test_pet_delete():
    url = "https://petstore.swagger.io/v2/pet/19"
    response = requests.delete(url)
    response_body = response.json()
    print(response_body)


def test_pet_post3():
    url = "https://petstore.swagger.io/v2/pet/19/uploadImage"
