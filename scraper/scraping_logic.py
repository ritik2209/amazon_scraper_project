import requests
from bs4 import BeautifulSoup
from datetime import date
from .models import SearchResult, Keyword
import random

# function to generate random user agent so that amazon does not block it 
def get_ua():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
 
    return random.choice(uastrings)



#function that sends requests to the url for the keyword and generates soup
def scrape_amazon(keyword):
    url = f'https://www.amazon.co.uk/s?field-keywords={keyword}'
    user_agent=get_ua()
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except Exception as e:
        print(str(e))

#function that parses result from soup , and inserts into database for appropriate labels like price,rating
def parse_results(soup, keyword):
    search_results = []
    for result in soup.find_all('div', {'data-index': True}):
        try:
            title = result.find('span', class_='a-text-normal').text.strip()
        except AttributeError:
                title = ' '
        try:
            description = result.find('span', class_='a-text-normal').text.strip()
        except AttributeError:
            description= ' '
        try:
            price_str = result.find('span', class_='a-price-whole').text.strip()
            price_str=price_str.replace(',','')
            price_str += result.find('span', class_='a-price-fraction').text
        except (AttributeError, ValueError):
            price_str= None
        print(price_str)
        try:
            rating = result.find('span', class_='a-icon-alt').text.split()
        except (AttributeError, ValueError):
            rating=None
        is_sponsored = False
        try:
            ad_label = result.find('span', class_='a-color-secondary').text.strip()
            if ad_label and 'Sponsored' in ad_label:
                is_sponsored = True
        except :
            continue


        search_results.append(SearchResult(
            keyword=keyword,
            title=title,
            description=description,
            price=float(price_str) if price_str else 0,
            rating=float(rating[0].replace(',', '.')) if rating else 0,
            is_sponsored=bool(is_sponsored),
            search_date=date.today(),
        ))
    return search_results

#function that fetches each keyword from database and scrapes data for them
def run_scraper():
    keywords = Keyword.objects.all()
    for keyword in keywords:
        soup = scrape_amazon(keyword)
        results = parse_results(soup, keyword)
        SearchResult.objects.bulk_create(results) #inserts into db