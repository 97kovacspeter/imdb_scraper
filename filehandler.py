
from encodings import utf_8
import json


def write_file(data, file_name):
    file_name += '.json'
    with open(file_name, "w", encoding='utf8') as write_file:
        json.dump(data, write_file, sort_keys=True,
                  indent=4, ensure_ascii=False)
