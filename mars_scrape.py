import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests

def scrape():
    
    mars_dict = {}
    
    # ### NASA Mars News
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    results = soup.find_all('li', class_='slide')

    news_title = soup.find('div', class_='content_title').find('a').text
    p = news_title


    # ### JPL Mars Space Images - Featured Image
    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_root = 'https://www.jpl.nasa.gov/'
    response_soup = requests.get(url_2)
    image_soup = bs(response_soup.text, 'html.parser')
    image = image_soup.find('a', attrs={'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
    image_url = url_root + image
    print(image_url)
    img_data = requests.get(image_url).content
    with open('featured_image.jpg', 'wb') as handler:
        handler.write(img_data)


    # ### Mars Weather
    url_3 = 'https://twitter.com/marswxreport?lang=en'
    response_3 = requests.get(url_3)
    soup_3 = bs(response_3.text, 'html.parser')
    tweet = soup_3.find('div', class_='js-tweet-text-container').find('p').text
    print(tweet)


    # ### Mars Facts
    table_url = 'http://space-facts.com/mars/'
    tables = pd.read_html(table_url)
    mars_df = tables[0]
    mars_df.columns = ['Description', 'Value']
    mars_df.set_index('Description', inplace=True)
    mars_table = mars_df.to_dict()
    mars_table


    # ### Mars Hemisperes
    url_4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(url_4)
    response_4 = requests.get(url_4)
    soup_4 = bs(response_4.text, 'html.parser')
    results = soup.find_all('div', class_='item')
    cer_link = 'https://astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    sch_link = 'https://astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    syr_link = 'https://astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    val_link = 'https://astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    image_urls = [cer_link, sch_link, syr_link, val_link]
    titles = soup_4.find_all('h3')
    titles = [h3.text for h3 in titles]
    titles
    images = [{'title': titles, 'image_url': image_urls} for titles, image_urls in zip(titles, image_urls)]
    images
    
    mars_dict = {'new_title':news_title,
                 'news_text': p,
                 'featured_image': image_url,
                 'weather': tweet, 
                 'facts': mars_table,
                 'hemisphere_images': images}
    
    return mars_dict

scrape