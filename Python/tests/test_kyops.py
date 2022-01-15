from .base_test import BaseTestCase
from kyops import merge_nested_dict

class TestKeyOps(BaseTestCase):
    def test_merge_nested_dict(self):
        my_dict_to_update = dict(
            client = dict(
                username="toto",
                password= "secret",
                contact= "<default_email>"
            )
        )
        newValues = dict(
            client = dict(
                password="confidenti@lP@ssword",
                contact = dict(
                    email= "email@gmail.com"
                )
            )
        )
        merge_nested_dict(my_dict_to_update, newValues)
        
        assert(my_dict_to_update.get("client").get("password") == "confidenti@lP@ssword")
        assert(type(my_dict_to_update.get("client").get("contact")) == dict)
