import pytest, json

from rest_framework.test import APIClient, APITestCase

class ClientRequest :
    def __init__(self, client) :
        self.client = client
    
    def __call__(self, type, url, data=None) :
        content_type = "application/json"

        if type == "get" :

            res = self.client.get(
                url,
                content_type = content_type,
            )

        elif type == "post" :
            
            res = self.client.post(
                url,
                json.dumps(data),
                content_type = content_type
            )

        elif type == "patch" :

            res = self.client.patch(
                url,
                json.dumps(data),
                content_type = content_type
            )

        else :

            pass

# class CreateTestView(APITestCase) :

#     def setUp(self) :

#         self.client = APIClient()
#         self.c = ClientRequest(self.client)

class RetrieveTestView(APITestCase) :

    def setUp(self) :

        self.client = APIClient()
        self.c = ClientRequest(self.client)

    def test_post_api(self) -> "Res Code, JSON Data" :

        url = "/shop/products/"

        data = {
            "name": "TestProduct",
            "option_set": [
                {
                    "name": "TestOption1",
                    "price": 1000
                },
                {
                    "name": "TestOption2",
                    "price": 500
                },
                {
                    "name": "TestOption3",
                    "price": 0
                }
            ],
            "tag_set": [
                {
                    "pk": 1,
                    "name": "ExistTag"
                },
                {
                    "name": "NewTag"
                }
            ]
        }

        res = self.client.post(
            url, 
            data = json.dumps(data),
            content_type = "application/json"
        )


        print("--------------- Create Test Result")
        print(res.data)
        
        assert res.status_code == 201


    def test_get_success(self) :

        url = "/shop/products/"


        res = self.client.get(
            url,
            content_type = "application/json"
        )
        
        print("---------------- Retrieve Test Result")
        print(res.data)

        assert res.status_code == 200