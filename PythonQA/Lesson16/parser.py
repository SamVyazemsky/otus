import re
from collections import Counter
import json


def reader(filename):

    regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    with open(filename) as f:
        log = f.read()

        ips_list = re.findall(regexp, log)

        print(ips_list)


def count(ips_list):

    count = Counter(ips_list)
    return count


def write_json(count):
    with open('output.json', 'w') as json_file:
        json.dump(count, 'output.json')


if __name__== '__main__':
    reader('access.log')

    write_json(count(reader('access.log')))