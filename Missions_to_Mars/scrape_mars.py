
# Dependancies
import os
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def scrape_info():


    #run ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://mars.nasa.gov/news'
    browser.visit(url)


    mars = {}



    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    type(soup)
    # Retrieve all elements that contain mars article information
    result1 = soup.find_all('div', class_='content_title')
    result2 = soup.find('div', class_='article_teaser_body')
        
    mars_article = result1[1].text.strip()
    mars_body_text = result2.text.strip()
        
    print(mars_article)
    print('-----------')
    print(mars_body_text)
    mars["news_title"] = mars_article
    mars["news_p"] = mars_body_text



    #visit the url for JPL Featured Space Image
    url_2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url_2)
    time.sleep(.5)
    browser.find_link_by_partial_text('FULL IMAGE').click()



    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    type(soup)

    # Retrieve all elements that contain image information
    mars_image = soup.find('img', class_='headerimage fade-in')


    print('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/')
    print(mars_image)
    print('-----------')
    mars_image["src"]


    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+ mars_image["src"]


    mars["featured_image_url"] = featured_image_url


    url_3 = 'https://space-facts.com/mars/'
    mars_tables = pd.read_html(url_3)
    mars_tables


    type(mars_tables)

    mars_df = mars_tables[0]
    mars_df

    mars2_df = mars_df.set_index(0, inplace=True)
    mars_df

    mars3_df = mars_df.rename(columns={0:' ',1:' '})
    mars3_df

    mars_html_table = mars3_df.to_html()
    mars_html_table


    clean_mars_html_table = mars_html_table.replace('\n', '')
    clean_mars_html_table



    mars["facts"]=clean_mars_html_table



    url_4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_4)
    link_list=browser.find_by_css("a.product-item h3")
    mars_hemisphere_image_urls = []
    for x in range(len(link_list)):
        hemisphere={}
        browser.find_by_css("a.product-item h3")[x].click()
        sample = browser.links.find_by_text("Sample").first
        hemisphere["img_url"]=sample["href"]
        hemisphere["title"]=browser.find_by_css("h2.title").text
        mars_hemisphere_image_urls.append(hemisphere)
        browser.back()
    mars_hemisphere_image_urls    
    mars["hemisphere"]=mars_hemisphere_image_urls 


    browser.quit()

    # Return results
    return mars

if __name__ == "__main__":
    print(scrape_info())



