from django.test import TestCase
from graphene.test import Client
from .schema import schema


class SellerInteractionTests(TestCase):
    def test_create_update_delete(self):
        client = Client(schema)
        executed = client.execute(
            """
            {
                sellers {
                    id
                }
            }
            """
        )
        assert executed == {"data": {"sellers": []}}
        executed = client.execute(
            """
            mutation {
                createSeller(shopName: "test", creationDate: "2020-09-08", photoLink: "example.com/test.png") {
                    ok
                    seller {
                        id
                    }
                }
            }
            """
        )
        assert executed == {
            "data": {"createSeller": {"ok": True, "seller": {"id": "1"}}}
        }
        executed = client.execute(
            """
            {
                sellers {
                    shopName
                    creationDate
                    photoLink
                }
            }
            """
        )
        assert executed == {
            "data": {
                "sellers": [
                    {
                        "shopName": "test",
                        "creationDate": "2020-09-08",
                        "photoLink": "example.com/test.png",
                    }
                ]
            }
        }
        executed = client.execute(
            """
            mutation {
                updateSeller(id: 1, shopName: "foobar", creationDate: "1970-08-09", photoLink: "png.com/test.example") {
                    ok
                    seller {
                        id
                    }
                }
            }
            """
        )
        assert executed == {
            "data": {"updateSeller": {"ok": True, "seller": {"id": "1"}}}
        }
        executed = client.execute(
            """
            {
                seller (id: 1) {
                    shopName
                    creationDate
                    photoLink
                }
            }
            """
        )
        assert executed == {
            "data": {
                "seller": {
                    "shopName": "foobar",
                    "creationDate": "1970-08-09",
                    "photoLink": "png.com/test.example",
                }
            }
        }
        executed = client.execute(
            """
            mutation {
                deleteSeller(id: 1) {
                    ok
                }
            }
            """
        )
        assert executed == {"data": {"deleteSeller": {"ok": True}}}
        executed = client.execute(
            """
            {
                sellers {
                    id
                }
            }
            """
        )
        assert executed == {"data": {"sellers": []}}


class CustomerInteractionTests(TestCase):
    def test_create_update_delete(self):
        client = Client(schema)
        executed = client.execute(
            """
            mutation {
                createCustomer(name: "test", email: "test@examle.com") {
                    ok
                    customer {
                        id
                    }
                }
            }
            """
        )
        assert executed == {
            "data": {"createCustomer": {"ok": True, "customer": {"id": "1"}}}
        }
        executed = client.execute(
            """
            {
                customer(id: 1) {
                    name,
                    email
                }
            }
            """
        )
        assert executed == {
            "data": {"customer": {"name": "test", "email": "test@examle.com"}}
        }
        executed = client.execute(
            """
            mutation {
                updateCustomer(id: 1, name: "barfoo", email: "barfoo@yandex.com") {
                    ok
                    customer {
                        id
                    }
                }
            }
            """
        )
        assert executed == {
            "data": {"updateCustomer": {"ok": True, "customer": {"id": "1"}}}
        }
        executed = client.execute(
            """
            {
                customer (id: 1) {
                    name,
                    email
                }
            }
            """
        )
        assert executed == {
            "data": {"customer": {"name": "barfoo", "email": "barfoo@yandex.com"}}
        }
        executed = client.execute(
            """
            mutation {
                deleteCustomer(id: 1) {
                    ok
                }
            }
            """
        )
        assert executed == {"data": {"deleteCustomer": {"ok": True}}}
        executed = client.execute(
            """
            {
                customer (id: 1) {
                    id
                }
            }
            """
        )
        assert executed == {
            "errors": [
                {
                    "message": "CustomerModel matching query does not exist.",
                    "locations": [{"line": 3, "column": 17}],
                    "path": ["customer"],
                }
            ],
            "data": {"customer": None},
        }
