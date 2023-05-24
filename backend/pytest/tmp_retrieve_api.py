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
                json.dumps(data),
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


class RetrieveTestView(APITestCase) :

    def setUp(self) :

        self.client = APIClient()
        self.c = ClientRequest(self.client)

   

    def test_get_success(self) :

        url = "/shop/products/"

        res = self.client.get(
            url, content_type = "application/json"
        )

        print(res.data)
        assert res.status_code == 200