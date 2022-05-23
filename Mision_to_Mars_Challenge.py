#Imports
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Otional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create and absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

#scrape entire table with pandas PD function.
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Convert DF to html
df.to_html()

# Turn off automated web scraping
browser.quit()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

### Hemispheres
# Set executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for image in range(4):
    # Create empty dictionary
    hemi = {}
    # Find the relative image url
    browser.find_by_tag('h3')[image].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    # Find the title
    title = browser.find_by_css('h2.title').text
    # Store image and title in dictionary
    hemi["img_url"] = img_url
    hemi["title"] = title
    hemisphere_image_urls.append(hemi)
    browser.back()
 
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()