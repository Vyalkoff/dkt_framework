import json
from variable import FILE_STORAGE


def get_storage():
    with open(FILE_STORAGE, 'r') as f:
        data = json.load(f)
    return data
