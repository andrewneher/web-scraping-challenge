#!/usr/bin/env python
# coding: utf-8

# Dependancies
import os
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #run ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # initial url
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    type(soup)
    # Retrieve all elements that contain mars article information
    result1 = soup.find('div', class_='content_title')
    result2 = soup.find('div', class_='article_teaser_body')
    mars_article = result1.text.strip()
    mars_body_text = result2.text.strip()
    
    print(mars_article)
    print('-----------')
    print(mars_body_text)


    # visit the url for JPL Featured Space Image
    url_2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url_2)



    # Iterate through all pages

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    type(soup)
    # Retrieve all elements that contain image information
    mars_image = soup.find('img', class_='headerimage fade-in')

    print('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/')
    print('-----------')
    print(mars_image)
    print('-----------')
            


    # featured image url
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'




    # getting the table
    url_3 = 'https://space-facts.com/mars/'
    mars_tables = pd.read_html(url_3)
    mars_tables





    type(mars_tables)



    # pandas table
    mars_df = mars_tables[0]
    mars_df.head()

    # html mars table
    mars_html_table = mars_df.to_html()
    mars_html_table


    # clean html table
    clean_mars_html_table = mars_html_table.replace('\n', '')
    clean_mars_html_table

    # exported html table
    mars_df.to_html('mars_html_table.html')

    # for clarity
    #Cerberus_Hemisphere = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    #Schiaparelli_Hemisphere = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    #Syrtis_Major_Hemisphere = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    #Valles_Marineris_Hemisphere = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    # hemisphere urls dictionary
    mars_hemisphere_image_urls = [
        {"title":"Cerberus Hemisphere","img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title":"Schiaparelli Hemisphere","img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title":"Syrtis Major Hemisphere","img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title":"Valles Marineris Hemisphere","img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
    ]


    browser.quit()

    # Return results
    return mars_hemisphere_image_urls







