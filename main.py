import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import urllib.request

def extract_image_urls(query, num_images):
    # Create a new folder in downloads with name as query and space replaced by -
    folder_name = query.replace(" ", "-")
    folder_path = f"downloads/{folder_name}"
    os.makedirs(folder_path, exist_ok=True)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    page = 1
    image_count = 0

    while image_count < num_images:
        
        search_url = f"https://www.istockphoto.com/search/2/image?mediatype=photography&phrase={query}&page={page}"
        driver.get(search_url)
        time.sleep(5)
        driver.get(search_url)
        thumbnails = driver.find_elements(By.CSS_SELECTOR, "img")
        
        for thumbnail in thumbnails:
            try:
                src = thumbnail.get_attribute("src")
                if src and "http" in src and ".jpg" in src:
                    image_count += 1
                    if image_count > num_images:
                        break
                    # Download the image
                    image_path = f"downloads/{query.replace(' ', '-')}/image{image_count}.jpg"
                    try:
                        urllib.request.urlretrieve(src, image_path)
                        print(f"Image {image_count} downloaded successfully!")
                        urllib.request.urlcleanup()
                    except Exception as e:
                        print(f"Error downloading image {image_count}: {e}")
            except Exception as e:
                print(f"Error extracting image URL: {e}")
        
        page += 1

if __name__ == "__main__":
    query = "apple"  # Replace with your search query
    num_images = 50  # Number of images to extract
    extract_image_urls(query, num_images)
