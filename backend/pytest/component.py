import json


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


created_data = {
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


updated_data = {
                    "pk": 1,
                    "name": "TestProduct",
                    "option_set": [
                        {
                            "pk": 1,
                            "name": "TestOption1",
                            "price": 1000
                        },
                        {
                            "pk": 2,
                            "name": "Edit TestOption2",
                            "price": 1500
                        },
                        {
                            "name": "Edit New Option",
                            "price": 300
                        }
                    ],
                    "tag_set": [
                        {
                            "name": "ExistTag2"
                        },
                        {
                            "name": "NewTag2"
                        },
                        {
                            "name": "Edit New Tag2"
                        }
                    ]
                }
