from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse, HttpResponseRedirect
import config_reader.config as config 

# Create your views here.

def index(request):      
        
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})    
    
    # Reading url from Config file(config.toml)
    page = requests.get(config.read_config("API","scraping_url"),headers=HEADERS)

    soup =  BeautifulSoup(page.content, "html.parser")          
    
    links = soup.find_all('a',attrs={'class':'Title__title__z5HRm Title__fixed__bJ2c2'})  
    
    data = []
        
    for link in links:
                              
        item_page = requests.get(config.read_config("API","amazon_url") + link.get('href') ,headers=HEADERS)         
        item_soup =  BeautifulSoup(item_page.content, "html.parser")          
    
        title = item_soup.find('span',attrs={'id':'productTitle'}).text      
        url = config.read_config("API","amazon_url") + link.get('href') 
        image = item_soup.find('div',attrs={'id':'imgTagWrapperId'}).find('img').get('src')         
        offer_price = item_soup.find('span', attrs={'class':'a-price-whole'}).text.replace('.','')
        original_price = item_soup.find('span',attrs={'class':'a-price a-text-price'}).find('span', attrs={'class':'a-offscreen'}).text.replace('₹','').replace('.00','')
        rating= item_soup.find('span', attrs={'class':'a-icon-alt'}).text          
              
        value = {   
            'title' : title,
            'url' : url,
            'image' : image,
            'offer_price' : offer_price,
            'original_price' : original_price,
            'rating' : rating
        }
        
        data.append(value)   
            
    return render(request,'WebScraping\scrap-data.html',{'data':data})


