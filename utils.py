# -*- coding:utf-8 -*-
import json


def save_file(obj, filename):
    data = json.dumps(obj)
    f = open(filename, 'w', encoding='utf8')
    f.write(data)
    f.close()


def load_file(filename):
    f = open(filename, 'r', encoding='utf8')
    content = f.read()
    data = json.loads(content)
    f.close()
    return data
