import re
import requests


def parse_women():
    response = requests.get('https://www.superheroapi.com/ids.html')
    html = response.text
    td_table = re.findall('<td.*/td>', html)

    parse_woman = dict()

    for i in range(0, len(td_table) - 1, 2):
        if re.match('.*woman.*', td_table[i + 1].lower()):
            id = td_table[i].replace('<td>', '').replace('</td>', '')
            name = td_table[i + 1].replace('<td>', '').replace('</td>', '')
            parse_woman[id] = name

    return parse_woman
