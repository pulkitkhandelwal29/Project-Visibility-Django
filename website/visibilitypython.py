import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from gtts import gTTS
import urllib


def text_to_speech(text):
    ''' Text to Speech function, also saves audio file '''
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=True)
    myobj.save("media/sample.mp3")
    source_path = 'media/sample.mp3'
    return source_path


def scrape(urls):
    ''' Scrapes links '''
    grab = requests.get(urls)
    soup = BeautifulSoup(grab.text, 'html.parser')

    websites = set()# traverse paragraphs from soup
    for link in soup.find_all('a'):
        data = link.get('href')
        websites.add(data)

    links = dict()
    links['home'] = urls

    for site in websites:
        if len(site) > 1:
            if site[0] != '/':
                site = '/' + site
            links[site.split('/')[-1].lower()] = urls + site
    return links




def find_link(links,speech_text):
    ''' Finds link to open from input sentence '''
    s = speech_text
    s = re.sub('[^a-zA-Z]','',s)
    s = s.lower()
    for key in links:
        # 'find' function returns index. If for any key, we find a non negative index, it means the key is present in our string
        if s.find(key) != -1:
            return links[key] if key != 'home' else links['home']
    return 'stop'



def program(urls,speech_text):
    links = scrape(urls)
    input_speech = find_link(links,speech_text)
    print(input_speech)
    if input_speech == 'stop':
        source_path = 'stop'
        temp_input='stop'
    else:
        temp_input = input_speech.split('/')[-1]
        if temp_input != '/':
            urls = input_speech
        page = urllib.request.urlopen(urls)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        text = text.replace('\n',' ').split('Technologies')[-1]
        source_path = text_to_speech(text)
        if temp_input == 'localhost:8000':
            temp_input = 'home'
    return source_path,temp_input
