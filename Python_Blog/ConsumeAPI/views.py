from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views import generic
import config_reader.config as config
import requests
from django.http import HttpResponse, HttpResponseRedirect
import logging

# Create your views here.

def consume_api(request):
    HEADERS = ({'User-Agent':config.read_config('Header','user_agent'),'Accept-Language':config.read_config('Header','accept_language')})    
    
    try:
           
        # Reading url from Config file(config.toml)
        page = requests.get(config.read_config("API","nowrunning_movie_url"), headers=HEADERS)

        soup =  BeautifulSoup(page.content, "html.parser")     
           
        links = soup.find_all('div',attrs={'class':'movie_s'}) 
        
        data = []
                            
        for link in links:
                                
            '''item_page = requests.get(config.read_config("API","amazon_url") + link.get('href') ,headers=HEADERS)         
            item_soup =  BeautifulSoup(item_page.content, "html.parser")          
        
            title = item_soup.find('span',attrs={'id':'productTitle'}).text      
            url = config.read_config("API","amazon_url") + link.get('href') 
            image = item_soup.find('div',attrs={'id':'imgTagWrapperId'}).find('img').get('src')         
            offer_price = item_soup.find('span', attrs={'class':'a-price-whole'}).text.replace('.','')
            original_price = item_soup.find('span',attrs={'class':'a-price a-text-price'}).find('span', attrs={'class':'a-offscreen'}).text.replace('₹','').replace('.00','')
            rating= item_soup.find('span', attrs={'class':'a-icon-alt'}).text '''       
           
            #breakpoint()
             
            title = link.find('a', attrs={'class':'list_title strong'}).text  
            url = config.read_config("API","nowrunning_url") + link.find('a', attrs={'class':'list_title strong'}).get('href')  
            img = link.find('amp-img').get('src')                     
           
            value = {   
                'title' : title,
                'website' : "NowRunning",
                'url' : url,
                'year' : '2023',
                'image' : img
            }
            
            data.append(value)   
                        
        return render(request,'ConsumeAPI\movie-list.html',{'data':data})
    except Exception as e:      
        error_message = 'user:' + str(request.user) + ', error:'+ str(e)     
        logging.getLogger("error_logger").error(error_message)
    