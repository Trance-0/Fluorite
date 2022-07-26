#!/usr/bin/python
#encoding='utf-8'

from operator import index
import sys
from lxml import etree
import requests
import csv

header = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Cookie: ll="108258"; bid=CBW2kf0J4Cw; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25902; dbcl2="259025636:/hHA+InalG8"; ck=GEj7; __utmc=30149280; __utmz=30149280.1658808027.4.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1658824687%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_id.100001.8cb4=496654c901cf3417.1658173027.5.1658824687.1658808024.; _pk_ses.100001.8cb4=*; __utma=30149280.82923040.1658173030.1658808027.1658824690.5; __utmt=1; __utmb=30149280.2.10.1658824690
Host: www.douban.com
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'''
# 将浏览器复制来的headers转为字典
headers = {}
for i in header.split('\n'):
    headers[i.split(': ')[0]]=i.split(': ')[1]
headers['Accept-Encoding'] = 'gzip'

def get_page(url):
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    print(response)
    return url, page_text

def parse_title(page_text):
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('//*[@id="content"]/div/div[1]/div[2]/table//tr')
    titles = []
    detail_urls = []
    for tr in tr_list[1:]:
        item = {}
        item['title'] = tr.xpath('./td[1]/a/@title')[0]
        item['user_link'] = tr.xpath('./td[2]/a/@href')[0]
        item['user_name'] = tr.xpath('./td[2]/a/text()')[0]
        item['comments'] = tr.xpath('./td[3]/text()')
        if item['comments']:
            item['comments'] = item['comments'][0]
        else:
            item['comments'] = '0'
        item['latest_time'] = tr.xpath('./td[4]/text()')[0]
        item['id'] = tr.xpath('./td[1]/a/@href')[0].split('/')[-2]
        titles.append(item)
        detail_url = tr.xpath('./td[1]/a/@href')[0]
        detail_urls.append(detail_url)
    return titles, detail_urls

def parse_details(url, page_text):
    item = {}
    tree = etree.HTML(page_text)
    item['create_time'] = tree.xpath('//*[@id="topic-content"]/div[2]/h3/span[2]/text()')[0]
    body = tree.xpath('//*[@id="link-report"]/div/div//text()')  # //text()表示div下的所有文本
    item['body'] = ''.join(body).strip()
    item['id'] = url.split('/')[-2]
    return item

def parse_members(n, page_text):
    members = []
    tree = etree.HTML(page_text)
    if n == 0:
        li_list = tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]//li')
    else:
        li_list = tree.xpath('//*[@id="content"]/div/div[1]/div[1]/div[1]//li')
    for li in li_list:
        item = {}
        item['user_name'] = li.xpath('./div[2]/a/text()')[0]
        item['user_link'] = li.xpath('./div[2]/a/@href')[0]
        city = li.xpath('./div[2]/span/text()')
        if city:
            item['city'] = city[0][1:-1]
        else:
            item['city'] = ''
        members.append(item)
    return members

def parse_member_details(page_text):
    item = {}
    tree = etree.HTML(page_text)
    item['join_time'] = tree.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/div/text()')[1].strip()
    city = tree.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a/text()')
    if city:
        item['city'] = city[0]
    else:
        item['city'] = ''
    item['id'] = tree.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/div/text()')[0].strip()
    group_lists = tree.xpath('//*[@id="group"]/dl')
    groups = []
    for group in group_lists:
        groups.append(group.xpath('./dd/a/@href')[0].split('/')[-2])
    item['groups'] = '/'.join(groups)
    return item


def progressbar(it, prefix="", size=29, file=sys.stdout):
    # This def is made by: https://stackoverflow.com/users/1207193/iambr
    # it is the list you are going to iterate
    # prefix is the title of your progress bar
    # size is the length of your progress bar
    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s%s] %i/%i\r" %
                   (prefix, "="*x, ">", "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
    
# 获取组员url
#,'choudongxi',236793 too large to process
groups_number=['curleyg','688259','668072','690472','712833','Kegel','708014']
groups_maximum_num=[9844,5854,22921,35308,12386,32338,19357]
groups_break_num=2448
groups_break_index=4
goups_index =groups_break_index
n=groups_break_num
while goups_index<7:
    while n<groups_maximum_num[goups_index]:
        print('Grabing page of {} progress={}/{}'.format(groups_number[goups_index],n,groups_maximum_num[goups_index]))
        url = 'https://www.douban.com/group/{}/members?start={}'.format(groups_number[goups_index],n)
        u, page_text = get_page(url)
        members = parse_members(n, page_text)
        with open('members_of_{}.csv'.format(groups_number[goups_index]), 'a', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            for member in members:
                w.writerow(member.values())
        n += 36
    n = 0
    goups_index+=1