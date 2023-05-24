import pytest
import json

from rest_framework.test import APIClient, APITestCase

from component import ClientRequest, created_data, updated_data


class PatchTestView(APITestCase) :

    def setUp(self) :

        self.client = APIClient()
        self.c = ClientRequest(self.client)

    def test_update_api(self) -> "Res Code, JSON Data" :

        url = "/shop/products/"

        res = self.client.post(
            url, 
            data = json.dumps(created_data),
            content_type = "application/json"
        )

        assert res.status_code == 201
        
        url = "/shop/products/" + str(res.data['pk']) + "/"  # 테스트를 위해 설정

        combine_data = updated_data
        combine_data["pk"] = res.data["pk"]


        res = self.client.patch(
            url, 
            data = json.dumps(combine_data),
            content_type = "application/json"
        )

        assert res.status_code == 200