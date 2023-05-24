import pytest
import json

from rest_framework.test import APIClient, APITestCase

from component import ClientRequest, created_data

class RetrieveTestView(APITestCase) :

    def setUp(self) :

        self.client = APIClient()
        self.c = ClientRequest(self.client)

    def test_retrieve_api(self) -> "Res Code, JSON Data" :

        # url = "/shop/products/"

        # res = self.client.post(
        #     url, 
        #     data = json.dumps(created_data),
        #     content_type = "application/json"
        # )

        # assert res.status_code == 201

        url = "/shop/products/"

        res = self.client.get(
            url,
            content_type = "application/json"
        )

        assert res.status_code == 200


        url = "/shop/products/1/"

        res = self.client.get(
            url,
            content_type = "application/json"
        )

        assert res.status_code == 200



    # def test_get_success(self) :

    #     url = "/shop/products/"

    #     res = self.client.get(
    #         url,
    #         content_type = "application/json"
    #     )

    #     assert res.status_code == 200