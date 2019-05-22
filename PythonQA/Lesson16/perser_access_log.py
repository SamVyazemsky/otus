import re
from collections import Counter
import json


def read_log(filename):

    with open(filename) as f:
        log = f.read()
        ip_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)
        return ip_list


def count_ip(ip_list):
    count = Counter(ip_list)
    return count


if __name__ == '__main__':
    res = count_ip(read_log('access2.log'))
    with open('res.json', 'w') as f:
        json.dump(res, f)
