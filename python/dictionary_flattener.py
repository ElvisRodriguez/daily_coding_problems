'''
This problem was asked by Stripe.

Write a function to flatten a nested dictionary.
Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

import collections


def flatten(dictionary, parent_key='', seperator='.'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + seperator + key if parent_key else key
        if isinstance(value, collections.MutableMapping):
            items.extend(
                flatten(value, parent_key=new_key, seperator=seperator).items()
            )
        else:
            items.append((new_key, value))
    return dict(items)


if __name__ == '__main__':
    dictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }
    print(flatten(dictionary))
