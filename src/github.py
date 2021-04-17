'''Selfmade :) Beacause I <3 scrapers'''

import requests
import dateparser
from bs4 import BeautifulSoup

def getsoup(url):
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except:
        raise Exception


def getlastcommit(url):
    soup = getsoup(url)
    lastcommit = {}
    try:
        lastcommit['time'] = dateparser.parse(str(soup.find('relative-time', class_='no-wrap')).split('datetime="')[1].split('"')[0])
    except:
        lastcommit['time'] = ''
    try:
        lastcommit['time_readable'] = str(soup.find('relative-time', class_='no-wrap')).split('">')[1].split('<')[0]
    except:
        lastcommit['time_readable'] = ''
    try:
        lastcommit['title'] = str(soup.find(class_='d-none d-sm-inline')).split('title="')[1].split('"')[0]
    except:
        lastcommit['title'] = ''
    try:
        lastcommit['number'] = str(soup.find('li', class_='ml-0 ml-md-3')).split('<strong>')[1].split('<')[0]
    except:
        lastcommit['number'] = ''
    return lastcommit

if __name__ == '__main__':
    url = 'https://github.com/nsde/neovision'
    print('Total Commits: ', getlastcommit(url)['number'])
    print('Newest commit time: ', getlastcommit(url)['time'])
    print('Newest commit time (readable): ', getlastcommit(url)['time_readable'])
    print('Newest commit title:', getlastcommit(url)['title'])