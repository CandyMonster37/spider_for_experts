# -*- coding:utf-8 -*-
from g_utils import get_1_page
import time
import random
from utils import load_file, save_file


def main():
    name_list = ['Samuel Absher', 'Noha Abdel-Karim']
    # Samuel Absher
    # Noha Abdel-Karim
    # Christopher Scott Adams

    data = {}
    for person in name_list:
        info = []
        tag = 10
        start = 0
        while tag >= 10:  # Determine whether it is the last page
            tag = get_1_page(name=person, info=info, start=start)
            start += 10

        stop = random.randint(1, 10)
        time.sleep(stop)

        print('experts:', person, 'total: ', len(info))
        data[person] = info
    save_file(obj=data, filename='./papers.json')
    # data = load_file('./papers.json')


if __name__ == '__main__':
    main()
