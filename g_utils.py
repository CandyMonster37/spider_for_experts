# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import re
import random

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 "
    "OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 "
    "Safari/534.16",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 "
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 "
    "TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 "
    "LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
    "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
    "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X "
    "MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE "
    "2.X MetaSr 1.0)",
]


def set_cookie():
    ori_cookie = 'GSP=LM=1616229657:S=eFgQB0Mx-bqUCu9u; ' \
                 'CONSENT=YES+; NID=211=TzsOglX9wAfWXYpWByRZDUa' \
                 'Fmj7KZ8VMrottKaV8uaX63kCrGQKXl09y_hHvZjpz0FrVIENwK' \
                 'nIfQ6pjeslwQe36zqLW5GtGXfzueC38yKPIGSBsBl5VgLbrtVAd-3' \
                 'bUDAqcBAKkf3Gl8jY9H2U--EBwY0vH_v5ned50VkQ8LYM'

    cookie = {}  # ?????????cookies????????????
    for line in ori_cookie.split(';'):  # ?????????????????????????????????
        # ????????????1???????????????????????????2???
        name, value = line.strip().split('=', 1)
        cookie[name] = value  # ?????????cookies????????????
    return cookie


def try_anain(url, flag=True, retry=5):
    proxy = {'https': 'http://127.0.0.1:21882'}
    # cookie = set_cookie()
    headers = {'Connection': 'close', 'User-Agent': random.choice(ua_list)}
    times = 0

    while flag and times < retry:
        try:
            res = requests.get(url, headers=headers, proxies=proxy)
            flag = False
        except requests.HTTPError as e:
            print('http error! status code: ', e.response.status_code)
            print("try again")
        except requests.exceptions.RequestException as e:
            print('Connect error!')
            print(e)
            print("try again...")
        except:
            print('other error...')
            print("try again...")
        finally:
            times += 1
            stop = random.randint(4, 10)
            time.sleep(stop)

    if flag:
        return None, 0
    else:
        res.encoding = res.apparent_encoding
        html = res.text
        return html, 1


def get_1_page(name, info, start, retry):
    un_name = name.split()
    para_name = ''
    for item in un_name:
        para_name = para_name + '+' + item
    # Christopher Scott Adams => +Christopher+Scott+Adams

    part_1 = 'https://scholar.google.com/scholar?start=' + str(start)
    part_2 = '&as_q=&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=' + para_name
    part_3 = '&as_publication=&as_ylo=&as_yhi=&hl=zh-CN&as_sdt=0%2C5&as_vis=1'
    # Does not contain references
    # if u want the results contain refs, set as_vis=0

    url = part_1 + part_2 + part_3
    # url = 'https://scholar.google.com/scholar?start=10&as_q=&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=+Noha' \
    #      '+Abdel-Karim&as_publication=&as_ylo=&as_yhi=&hl=zh-CN&as_sdt=0%2C5&as_vis=1'

    proxy = {'https': 'http://127.0.0.1:21882'}
    # cookie = set_cookie()
    headers = {'Connection': 'close', 'User-Agent': random.choice(ua_list)}

    try:
        # res = requests.get(url, cookies=cookie, headers=headers, proxies=proxy)
        res = requests.get(url, headers=headers, proxies=proxy)
        print('url:', url)
        print('get response successfully! ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        again_ = False
        # print(res.status_code)
    except requests.HTTPError as e:
        print('http error! status code: ', e.response.status_code)
        again_ = True
    except requests.exceptions.RequestException as e:
        print('Connect error!')
        print(e)
        again_ = True
    except:
        print('other error')
        again_ = True

    if not again_:
        res.encoding = res.apparent_encoding
        html = res.text
        chance = 1
        # print(html)
    else:
        html, chance = try_anain(url, again_, retry)

    if chance == 0:
        # ????????????????????????
        tag = 10
        # ????????????????????????????????????
    else:
        tag = get_info(html, info)

    stop = random.randint(4, 10)
    time.sleep(stop)
    return tag


def get_info(html, person):
    """
    :param html: the html page of the target url, a BeautifulSoup object
    :param person: the author of the article, a list
    :return: the number of the answers in this page, int
    """
    titles = []  # the title of the article
    urls = []  # the url of the article
    times = []  # the number of times the article has been cited
    mag = []  # the magazine where the paper is published
    domain = []  # the domain name of the magazine
    year = []  # the paper publication year

    bf = BeautifulSoup(html, 'lxml')

    # Get the paper titles less than 10
    un_titles = bf.select('#gs_res_ccl_mid > div > div.gs_ri > h3 > a')
    # #gs_res_ccl_mid > div:nth-child(1) > div.gs_ri > h3
    # The parameters in brackets are related to the structure of the web page
    # Press F12 to find the target label name and label attributes
    for item in un_titles:
        titles.append(item.text)
        urls.append(item.get('href'))
        # print(item.text)
        # print(item.get('href'))
    flag = len(urls)

    # get the number of times the article has been cited
    un_times = bf.select('#gs_res_ccl_mid > div > div > div.gs_fl > a:nth-child(3)')
    for item in un_times:
        ans = re.compile(r'\d+').findall(item.text)
        if len(ans) == 0:
            ans.append("0")
        times.append(ans[0])

    # get the magazine where the paper is published
    # the domain name of the magazine
    # as well as # the paper publication year
    un_org = bf.select('#gs_res_ccl_mid > div > div > div.gs_a')
    mag_year = []

    for item in un_org[:len(titles)]:
        inf_text = item.text
        mid_text_list = inf_text.replace('\xa0', '').split('-')
        un_mag_year = mid_text_list[-2].strip().lstrip('???')
        tmp = un_mag_year.split(',')

        if len(tmp) != 2:
            if tmp[-1].strip().isdigit():
                padding = ["None", tmp[-1].strip()]
            else:
                padding = ["None", "None"]
            mag_year.append(padding)
        else:
            if tmp[-1].strip().isdigit():
                mag_year.append(tmp)
            else:
                padding = [tmp[-1], "None"]
                mag_year.append(padding)

        site = mid_text_list[-1].strip()
        domain.append(site)

    for item in mag_year:
        if item[0].strip().isdigit():
            item[0] = 'None'
        mag.append(item[0])
        year.append(item[-1])

    # for i in range(0, len(year)):
    #    print('magazine:', mag[i], ' ||| domain:', domain[i], ' ||| year:', year[i])

    for i in range(0, len(times)):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        tmp = {'title': titles[i], 'url': urls[i],
               'magazine': mag[i], 'domain': domain[i],
               'times': times[i], 'year': year[i],
               'Timestamp': now}
        person.append(tmp)
    return flag
