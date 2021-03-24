import json
import requests #pip install requests
import xmltodict #pip install xmltodict, remove the xmltodict.py in this directory if you have problems importing this
import dateparser
import markdownify #pip install markdownify

from bs4 import BeautifulSoup

def format_discord(text):
    '''Format a text so it's easily readable on Discord (optimized for Discord message embeds!).'''
    if not text:
        text = ''

    replacer = {
        '<strong>': '**',
        '</strong>': '**',
        '<li>': 'x',
        '</li>': 'y',
        '<ul>': '',
        '</ul>': '',
        '<br>': '\n',
        '<a href="': '(',
        '">': ')[',
        '</a>': ']',
        '<ol>': '',
        '</ol>': '',
        '<div>': '',
        '</div>': '',
        '<mark>': '__',
        '</mark>': '__',
        '<em>': '',
        '</em>': '',
        # '• ': '',
        # '•\n': '',
        '\n\n': '',
        '\n\n\n': '',

    }

    # for item in replacer.keys():
    #     text = text.replace(item, replacer[item])

    text = markdownify.markdownify(text).replace('\n\n', '\n').replace('\n\n\n', '\n')

    return text

def getpadlet(url, discord=False):
    '''Get data about a padlet.'''
    '''discord (bol): If the output should be formatted/optimized for discord.'''
    html = requests.get(url).text
    padlet_id = html.split('/exports/print.html')[0].split('https://padlet.com/padlets/')[1].split('/exports/feed.xml')[0]

    feed_url = f'https://padlet.com/padlets/{padlet_id}/exports/feed.xml'
    feed_xml = requests.get(feed_url).text

    dict_data = xmltodict.parse(feed_xml)
    padlet_data = json.loads(json.dumps(dict_data))

    padlet = {}
    padlet['id'] = padlet_id
    padlet['icon'] = padlet_data['rss']['channel']['image']['url']
    padlet['title'] = padlet_data['rss']['channel']['title']
    padlet['author'] = url.replace('//', '').split('/')[1]
    padlet['last_edit'] = dateparser.parse(' '.join(padlet_data['rss']['channel']['lastBuildDate'].split()[:2]))
    padlet['description'] = padlet_data['rss']['channel']['description']

    padlet['posts'] = []
    for row_data in padlet_data['rss']['channel']['item']:
        row = {}
        if not discord:
            row['title'] = row_data['title']
            row['items'] = row_data['description']
        else:
            try:
                row['title'] = f'\n\n**__{row_data["title"].upper()}__**\n'
            except:
                row['title'] = ''
            row['items'] = format_discord(row_data['description'])

        padlet['posts'].append(row)

    return padlet

if __name__ == '__main__':
    data = getpadlet('https://padlet.com/onlix/ha', discord=True)
    print(data)
    # for post in data['posts']:
    #     print(post['title'] + post['items'])
    # print(getpadlet('https://padlet.com/onlix/ha'))7