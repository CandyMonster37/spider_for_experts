# -*- coding:utf-8 -*-
from g_utils import get_1_page
import time
import random
import os
from utils import load_file, save_file


def get_experts():
    rela = load_file('./data/stafflist.json')
    namelist = list(rela.keys())
    fields = []
    for name in namelist:
        fields.append(rela[name])
    return namelist, fields


def main():
    # name_list = ['Samuel Absher', 'Noha Abdel-Karim']  # test data lol
    if not os.path.exists('./data/info'):
        os.mkdir('./data/info')
    name_list, fields = get_experts()

    data = {}
    for person in name_list:
        tar = './data/info/' + person
        if os.path.exists(tar):
            continue

        print('now fetching : ', person)
        info = []
        tag = 10
        start = 0
        while tag >= 10:  # Determine whether it's the last page
            tag = get_1_page(name=person, info=info, start=start)
            start += 10

        print('experts:', person, 'total: ', len(info))
        tar = './data/info/' + person
        save_file(obj=data, filename=tar)

        stop = random.randint(1, 10)
        time.sleep(stop)

    # data = load_file('./papers.json')
    print('\n\nall jobs done! See files in : ./data/info/')


if __name__ == '__main__':
    main()
