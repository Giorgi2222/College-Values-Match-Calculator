from pathlib import Path
import requests
from bs4 import BeautifulSoup
import queue
import re


def scrap(base_url, n):
    start_anchor = '/'
    search_anchors = queue.Queue()
    urls = []
    texts =[]
    for _ in range (n):
        if not start_anchor:
            start_anchor = '/'
        try:
            if start_anchor.startswith("http"):
                response = requests.request('GET', start_anchor)
            else:
                response = requests.request('GET', base_url + start_anchor)
            
            soup = BeautifulSoup(response.text, 'lxml')
            text = soup.get_text()
            texts.append(text)
            anchors = find_local_anchors(soup, start_anchor, base_url)
        except:
            pass
        
        try:
            if anchors:
                for a in anchors:
                    if a.startswith("http"):
                        url = a
                    else:
                        url = base_url + a
                    if url in urls:
                        continue
                    if not Path(a).suffix:
                        search_anchors.put(a)
                    urls.append(url)
                    print(url)
        except:
            pass
        if search_anchors.empty():
            break
        start_anchor = search_anchors.get()
    return texts

def find_local_anchors(soup, start_anchor, base_url):
    anchors = []
    for link in soup.find_all('a'):
        anchor = link.attrs['href'] if "href" in link.attrs else ''
    
        if re.search('20[0-1]{1}[0-9]{1}', anchor):
            continue
        elif re.search('archive', anchor):
            continue
        elif re.search('department', anchor):
            continue
        elif re.search('login', anchor):
            continue
        elif re.search('password', anchor):
            continue
        elif re.search('register', anchor):
            continue
        elif anchor.startswith(start_anchor):
            anchors.append(anchor)
        elif anchor.startswith(base_url):
            anchors.append(anchor)
        elif match := re.search('[a-z]+.edu', str(anchor)):
            if match.group() == re.search('[a-z]+.edu', base_url).group():
                anchors.append(anchor)

    return anchors

