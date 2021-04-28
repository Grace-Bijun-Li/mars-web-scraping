# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape():
    browser = init_browser()

    # NASA Mars News
    # scrap the News URL
    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Collect the latest News Title and Paragraph Text
    news_title = news_soup.find_all('div', class_='content_title')[1].text
    news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text

    # JPL Mars Space Images - Featured Image
    # scrap the JPL URL
    images_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(images_url)
    time.sleep(1)
    html = browser.html
    images_soup = BeautifulSoup(html, 'html.parser')

    # Find featured image URL
    relative_image_path = images_soup.find_all('a')[2]['href']
    base_jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    featured_image_url = base_jpl_url + relative_image_path
    
    # Mars Facts
    # scrap the Mars Facts URL
    facts_url  = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    facts_df = tables[0].rename(columns={0:'Facts',1:'Data'}).set_index('Facts')
    facts_table = facts_df.to_html().replace('\n','')

    # Mars Hemispheres
    # scrap the Mars hemisphere URL
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    hemi_html = browser.html
    hemi_soup = BeautifulSoup(hemi_html, 'html.parser')

    # Build the dictionary containing the title and image of each hemisphere
    mars_hemispheres = hemi_soup.find('div', class_='collapsible results')
    mars_hemi_items = mars_hemispheres.find_all('div', class_='item')
    base_hemi_url = 'https://astrogeology.usgs.gov'
    hemi_image_urls = []

    # Use for loop to extract the URL for each hemisphere
    for i in mars_hemi_items:
        # Collect Title
        hemisphere = i.find('div', class_='description')
        title = hemisphere.h3.text
        
        # Collect image URL
        hemisphere_link = hemisphere.a["href"]    
        browser.visit(base_hemi_url + hemisphere_link)
        
        image_html = browser.html
        image_soup = BeautifulSoup(image_html, 'html.parser')
        
        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']

        # Add the title and image info into a dictionary
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url
        
        hemi_image_urls.append(image_dict)

    # Create a general dictionary containing all above information
    mars_dict = {
    "news_title": news_title,
    "news_p": news_p,
    "featured_image_url": featured_image_url,
    "mars_fact": str(facts_table),
    "mars_hemisphere": hemi_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    return mars_dict