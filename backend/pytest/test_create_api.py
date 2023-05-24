import pytest
import json

from rest_framework.test import APIClient, APITestCase

from component import ClientRequest, created_data

class CreatedTestView(APITestCase) :

    def setUp(self) :

        self.client = APIClient()
        self.c = ClientRequest(self.client)

    def test_post_api(self) -> "Res Code, JSON Data" :

        url = "/shop/products/"

        res = self.client.post(
            url, 
            data = json.dumps(created_data),
            content_type = "application/json"
        )

        assert res.status_code == 201


    # def test_get_success(self) :

    #     url = "/shop/products/"


    #     res = self.client.get(
    #         url,
    #         content_type = "application/json"
    #     )
        
    #     print("---------------- Retrieve Test Result")
    #     print(res.data)

    #     assert res.status_code == 200