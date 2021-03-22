# -*- coding:utf-8 -*-
# !/usr/bin/env python

# the experts page of the RAND uses asynchronous transmission
# from the response of the url: https://www.rand.org/about/people.html
# F12 -> Network -> F5 -> XHR -> Header
# then we can know that the information is stored here:
# https://www.rand.org/content/rand/about/people/_jcr_content/par/stafflist.xml
# so it's simply to get the datas and save them

from utils import save_file
import requests
import time
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom


def read_xml():
    rela = {}
    dom = xml.dom.minidom.parse('./data/stafflist.xml')
    root = dom.documentElement

    itemlist_ = root.getElementsByTagName('staff')
    for item in itemlist_:
        name = item.getAttribute("name")
        area = item.getAttribute("title")
        if name in list(rela.keys()):
            rela[name] += area
        else:
            rela[name] = area

    return rela


def get_xml():
    url = 'https://www.rand.org/content/rand/about/people/_jcr_content/par/stafflist.xml'
    headers = {'Connection': 'close',
               'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                             "AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 "}

    try:
        res = requests.get(url, headers=headers)
        print('url:', url)
        print('get response successfully! ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # print(res.status_code)
    except requests.HTTPError as e:
        print('http error: status_code', res.status_code)
        time.sleep(3)
    except Exception as e:
        print('other error:')
        print(e)

    res.encoding = 'utf-8'
    html = res.text

    root = ET.fromstring(html)
    tree = ET.ElementTree(root)
    filename = './data/stafflist.xml'
    tree.write(filename)
    print('original data has been saved here: ', filename)


def main():
    if not os.path.exists('./data/stafflist.xml'):
        print('ready to get data!')
        get_xml()
    else:
        print('data exists!')
    rela = read_xml()
    save_file(rela, './data/stafflist.json')
    print('see original data in :', './data/stafflist.xml')
    print('see selected data in : ', './data/stafflist.json')


if __name__ == '__main__':
    main()
