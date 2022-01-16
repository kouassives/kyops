from copy import deepcopy
import json
from operator import ne


class NDict:

    def __init__(self, data: dict = {}) -> None:
        self._data = deepcopy(data)
    
    def update(self, new_values:dict) -> None:
        """ Update data in Ndict object
        Example : 
        my_dict = NDict(my_dict_to_update)
        my_dict.update(new_values)
        # Now my_dict.data contains updated datas
        """
        cp_new_values = deepcopy(new_values)
        NDict.merge_nested_dict(self._data, cp_new_values)

    def __repr__(self) -> str:
        return json.dumps(self._data, indent=4)

    @property
    def data(self) -> dict:
        return deepcopy(self._data)

    @data.setter
    def data(self, new_values:dict) -> None:
        self.data = deepcopy(new_values)

    @staticmethod
    def merge_nested_dict(dict_result: dict, dict_to_use: dict) -> None:
        """ Merge a nested dictionaries
        In the case of an update of a dictionary from another second.
        It is possible to update AAA from BBB by updating
        only the subfields of the subdictionaries if necessary. Useful for updating yaml data
    
        Example:
        my_dict_to_update = {
            "client" : {
                "zip": "3500",
                "username" : "toto",
                "password" : "secret",
                "contacts" : {
                    "tel" : "000000",
                    "email" : "<default_email>"
                }
            }
        }
        new_values = {
            "client" : {
                "zip": {
                    "Dep":"35",
                    "code": "0000"
                },
                "password" : "confidenti@lP@ssword",
                "contacts" : {
                    "email" : "email@gmail.com"
                }
            }
        }

        NDict.merge_nested_dict(my_dict_to_update, new_values)

        print(my_dict_to_update)
        #Output
# {
#     "client": {
#         "zip": {
#             "Dep": "35",
#             "code": "0000"
#         },
#         "username": "toto",
#         "password": "confidenti@lP@ssword",
#         "contacts": {
#             "tel": "000000",
#             "email": "email@gmail.com"
#         }
#     }
# }
        """

        if (type(dict_result)==dict and type(dict_result)==dict ):
            key_to_remove =[]
            for key in dict_result.keys():
                if (dict_to_use.get(key)):
                    if (type(dict_result[key])==dict and type(dict_to_use[key])==dict):
                        NDict.merge_nested_dict(dict_result[key], dict_to_use[key])
                    else:
                        dict_result[key] = dict_to_use[key]
                    key_to_remove.append(key)
            [dict_to_use.pop(key) for key in key_to_remove]
            dict_result.update(dict_to_use)

merge_nested_dict = NDict.merge_nested_dict
