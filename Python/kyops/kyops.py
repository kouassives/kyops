class KyOps:

    @staticmethod
    def merge_nested_dict(dict_result: dict, dict_to_use: dict):
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
        newValues = {
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
        kyops.merge_nested_dict(my_dict_to_update, newValues)

        print(my_dict_to_update)
        #Output
        {
            "client" : {
                        "username" : "toto"
                        "password" : "confidenti@lP@ssword"
            }
        }
        """

        if (type(dict_result)==dict and type(dict_result)==dict ):
            key_to_remove =[]
            for key in dict_result.keys():
                if (dict_to_use.get(key)):
                    if (type(dict_result[key])==dict and type(dict_to_use[key])==dict):
                        KyOps.merge_nested_dict(dict_result[key], dict_to_use[key])
                    else:
                        dict_result[key] = dict_to_use[key]
                    key_to_remove.append(key)
            [dict_to_use.pop(key) for key in key_to_remove]
            dict_result.update(dict_to_use)

merge_nested_dict = KyOps.merge_nested_dict