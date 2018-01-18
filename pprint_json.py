import json
import sys


def load_data(filepath):
    with open(filepath) as file:
        return json.loads(file.read())


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
