# -*- coding:utf-8 -*-
from g_utils import get_1_page
import time
import random
import os
from utils import load_file, save_file


def get_experts():
    if not os.path.exists('./data/stafflist.json'):
        os.system("python3 for_rand.py")
    rela = load_file('./data/stafflist.json')
    namelist = list(rela.keys())
    fields = []
    for name in namelist:
        fields.append(rela[name])
    return namelist, fields


def main():
    # name_list = ['Marcy Agmon']  # test data lol
    if not os.path.exists('./data/info'):
        os.mkdir('./data/info')
    name_list, fields = get_experts()

    guard = 0
    cont = False  # Determine whether it's continuous

    for person in name_list:
        tar = './data/info/' + person
        if os.path.exists(tar):
            continue

        print('now fetching : ', person, ' id : ', name_list.index(person))
        info = []
        tag = 10
        start = 0
        weight = 0
        while tag >= 10:  # Determine whether it's the last page
            weight += 1
            time.sleep(weight*1.3)
            tag = get_1_page(name=person, info=info, start=start)
            start += 10

        print('experts:', person, 'total: ', len(info))
        tar = './data/info/' + person
        save_file(obj=info, filename=tar)

        if len(info) == 0:
            if guard == 0:
                cont = True
            guard += 1
        elif len(info) != 0:
            guard = 0
            cont = False

        if guard == 3 and cont:
            print('Caught by Google! Check the last 3 files and change ur IP, then restart this program!')
            return

        stop = random.randint(4, 10)
        time.sleep(stop)

    # data = load_file('./papers.json')
    print('\n\nall jobs done! See files in : ./data/info/')


if __name__ == '__main__':
    main()
