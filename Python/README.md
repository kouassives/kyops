# KyOps python library



[[_TOC_]]

## Overview

KyOps is a python library for performing operations on data structures in python. It provides a set of functions to manipulate structures such as a `dict`.

## Installation

KyOps is a Python3 library that you can install via `pip`

```bash
pip install kyops
```



## Usage

To date, the functionality it offers is the ability to update a nested dictionary from another dictionary. Example:

```Python
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

from kyops import Ndict
n_dict = Ndict(my_dict_to_update)
n_dict.update(new_values)

# Now my_dict.data contains updated datas



```

It possible to use `merge_nested_dict` static method:

```python
kyops.merge_nested_dict(my_dict_to_update, new_values)
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
```



## Contributing

You want to contribute to the project? Too cool, you're welcome. Please submit a pull request. Or write all your questions by opening an issue.

