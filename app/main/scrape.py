from bs4 import BeautifulSoup
import requests
from .. import db
import requests
from ..models import Article

from datetime import datetime


HEADERS =  {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def get_story_thenews(url,curr_user):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('div',class_="story-detail")
    story_date = soup.find('div',class_="category-date").text
    heading = soup.find('div',class_='detail-heading').find('h1').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text

    text = heading + story

    res = requests.post('http://127.0.0.1:5001/',json = {"news":text})
    res = not(res.json())

    a = Article(body=story,
                    url = url,
                    title = heading,
                    subject = "News",
                    published = story_date,
                    fake = res,
                    searched_by = curr_user.id)

    db.session.add(a)
    db.session.commit()



def get_story_express(url,curr_user):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('span',class_="story-text")
    story_date = soup.find('div',class_="left-authorbox").find_all('span')[1].text
    heading = soup.find('div',class_='maincontent-customwidth storypage').find('h1').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
    

    text = heading + story

    res = requests.post('http://127.0.0.1:5001/',json = {"news":text})
    res = not(res.json())

    a = Article(body=story,
                    url = url,
                    title = heading,
                    subject = "News",
                    published = story_date,
                    fake = res,
                    searched_by = curr_user.id)

    db.session.add(a)
    db.session.commit()





def get_story_dawn(url,curr_user):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('article',class_="story")
    story_date = soup.find('span',class_="story__time").text
    heading = soup.find('h2',class_='story__title').find('a').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
 
    text = heading + story

    res = requests.post('http://127.0.0.1:5001/',json = {"news":text})
    res = not(res.json())


    a = Article(body=story,
                    url = url,
                    title = heading,
                    subject = "News",
                    published = story_date,
                    fake = res,
                    searched_by = curr_user.id)

    db.session.add(a)
    db.session.commit()


def get_story_dependent(url,curr_user):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('div',class_="entry-content")
    story_date = soup.find('div',class_="entry-meta capital").text
    heading = soup.find('h1',class_='entry-title').text
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
 
    text = heading + story

    res = requests.post('http://127.0.0.1:5001/',json = {"news":text})
    res = not(res.json())


    a = Article(body=story,
                    url = url,
                    title = heading,
                    subject = "News",
                    published = story_date,
                    fake = res,
                    searched_by = curr_user.id)

    db.session.add(a)
    db.session.commit()




def get_text(text,curr_user):

    text = text


    res = requests.post('http://127.0.0.1:5001/',json = {"news":text})
    res = not(res.json())


    a = Article(body=text,
                    url = "This is cutom Text so no URL",
                    title = "Custom Text",
                    subject = "Random Text",
                    published = datetime.now(),
                    fake = res,
                    searched_by = curr_user.id)

    db.session.add(a)
    db.session.commit()