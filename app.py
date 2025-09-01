import time
import random
import requests
import numpy as np 
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse
from scraper import parse_page
from scraper import page_headers



full_data = []
attempt = 0
page = 1445 #next time start from 1522 page

while True:
    headers = page_headers

    url = f"https://www.amazon.com/s?i=electronics&rh=n%3A172282%2Cp_n_g-101014971069111%3A119653281011&dc&page={page}&qid=1755739827&ref=sr_pg_{page}"
    
    print(f"📄 Scraping page {page}: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:
            print(f"✅ Request successful on attempt {attempt + 1}")
            soup = BeautifulSoup(response.content, 'html.parser')
            data = parse_page(soup)

            # if not data:
            #     print("✅ No more products. Stopping.")
            #     break

            full_data.extend(data)
            print(f"✅ Scraped {len(data)} products from current page (Total: {len(full_data)})")

            page += 1
            attempt = 0  # Reset after success
            time.sleep(random.uniform(8, 12))  # Human-like delay

        elif response.status_code in [429, 503]:
            wait_time = random.uniform(5, 15) * (attempt + 1)
            print(f"⚠ Bot detection triggered! Status {response.status_code}. Retrying in {wait_time:.1f}s...")
            time.sleep(wait_time)
            attempt += 1
            if attempt >= 5:
                print("❌ Max retries reached. Could not continue scraping.")
                break

        else:
            print(f"⚠ Unexpected status code: {response.status_code}")
            break

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        time.sleep(random.uniform(8, 12))
        attempt += 1
        if attempt >= 5:
            print("❌ Max retries reached. Could not continue scraping.")
            break

print(f"✅ Scraping finished. Total products collected: {len(full_data)}")

# creaye data frame and exporte

df = pd.DataFrame(full_data)
df.to_csv('amazon_data_8.csv', index=False)

print("✅ All procedures for collecting and exporting data completed successfully.")


