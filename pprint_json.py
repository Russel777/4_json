import json
import sys
import os


def load_data(filepath):
    with open(filepath) as file:
        return json.loads(file.read())


def pretty_print_json(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    for param in sys.argv[1:]:
        if os.path.isfile(param):
            pretty_print_json(load_data(param))
        else:
            print("File is not exist")
