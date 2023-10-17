
request = {}
request["id"] = 1
request["username"] = "Ivi"
request["firstName"] = "Iveta"
request["lastName"] = "Abaeva"
request["email"] = "test1@mail.ru"
request["password"] = "test123"
request["phone"] = "89998888888"
request["userStatus"] = 1

request = {}
request["id"] = 1
request["petId"] = 12
request["quantity"] = 3
request["shipDate"] = "2023-10-10T10:45:41.661Z"
request["status"] = "placed"
request["complete"] = True


request = {}
request["document"] = {}
request["document"]["client"] = "1480369995942764573"
request["document"]["appliesOnAllProducts"] = False
request["document"]["documentProducts"] = ["6901924475947515907", "690192447594758765"]
request["document"]["documentPersons"] = [{}]
request["document"]["documentPersons"][0]["party"] = "1480370292295508038"
request["document"]["documentPersons"][0]["authorities"] = [{}]
request["document"]["documentPersons"][0]["authorities"][0]["authorityCode"] = "LOCATION_MONEY_DEP_NSO_LIMITSUM"

var_1 = [1,2,3]

def func(a):
    var_2 = []
        for i in a:
     var_2.append(i*2)

    return var_2

    var_3 = var_1

var_3.append(12)

print(func(var_1))

print(var_1)
