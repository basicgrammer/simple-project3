import pytest
import json

from rest_framework.test import APIClient, APITestCase

from component import ClientRequest, created_data, updated_data


class UpdateTestView(APITestCase) :

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
        
        print(res.data['pk'])
        assert res.status_code == 201

        url = "/shop/products/" + str(res.data['pk']) + "/"

    

        combine_data = updated_data
        combine_data["pk"] = res.data["pk"]


        res = self.client.patch(
            url, 
            data = json.dumps(combine_data),
            content_type = "application/json"
        )

        print(res.data)
        assert res.status_code == 200