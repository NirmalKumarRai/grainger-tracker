from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
import time

from backend.models import ProductResult, db  # Import your SQLAlchemy models and db instance


def scrape_grainger():
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()
    
    # Read URLs from CSV file
    df = pd.read_csv(r'data\Grainger less than 10 - Sheet1.csv')

    # Loop through each URL
    for i, url in enumerate(df['url'][1:20000]):
        print(f"Processing URL {i + 1}/{len(df)}: {url}")

        try:
            # Navigate to the website
            driver.get(url)

            # Scraping logic goes here...
            # Example: Extracting title
            title = driver.find_element(By.XPATH,'//h1[@class="lypQpT"]').text
            price = driver.find_element(By.XPATH, '''//div[@class="M5iHu4"]//span[contains(@class, 'cRcU4D')]''').text

            # Save scraped data to database
            product_result = ProductResult(
                name=title,
                url=url,
                price = price
                # Add more fields as needed based on your scraping logic
            )
            db.session.add(product_result)
            db.session.commit()
        except Exception as e:
            print('Error occurred:', e)

        # Pause for a few seconds before processing the next URL
        time.sleep(2)

    # Close the webdriver
    driver.quit()

    print('Scraping completed.')


if __name__ == '__main__':
    scrape_grainger()
