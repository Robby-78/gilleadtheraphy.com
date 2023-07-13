import os
import time
import random
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

visits_counter = 0

url_list = [
    'https://iconect.co.ke/modern-tanks-from-germany-and-uk-to-ukraine-against-russian-invasion',
    'https://iconect.co.ke/israeli-pm-delays-controversial-judicial-overhaul-amid-protests-and-strikes',
    'https://iconect.co.ke/373',
    'https://iconect.co.ke/how-we-can-reduce-global-warming',
    'https://iconect.co.ke/russia-test-fires-anti-ship-missiles-sea-of-japan',
    'https://iconect.co.ke/exploring-the-art-and-science-of-astrology-self-discovery-skepticism-and-personal-growth',
    'https://iconect.co.ke/amnesty-international-report-exposes-double-standards-in-human-rights-amidst-ukraine-invasion',
    'https://iconect.co.ke/coca-cola-a-legacy-of-quality-innovation-and-sustainability',
    'https://iconect.co.ke/oscars-over-the-last-decade-celebrating-the-best-in-film',
    'https://iconect.co.ke/the-rise-of-electric-cars-a-game-changer-in-the-auto-industry',
    'https://iconect.co.ke/african-spirituality-nurturing-identity-and-culture-before-christianity',
    'https://iconect.co.ke/the-rise-of-electric-cars-a-game-changer-in-the-auto-industry',
    'https://iconect.co.ke/maat-the-ancient-egyptian-concept-of-balance-justice-and-truth',
    'https://iconect.co.ke/working-in-germany-a-guide-to-employment-opportunities-culture-and-requirements',
    'https://iconect.co.ke/the-legacy-of-ancient-grinders-from-manual-labor-to-cultural-heritage',
]

# Read the list of proxies from the CSV file
# df = pd.read_csv("https://github.com/jetkai/proxy-list/raw/main/online-proxies/csv/proxies.csv")
# df =df.iloc[1200:]
proxies = [
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt"
]
proxies_df = pd.DataFrame({'http': []})

# Iterate over the proxy URLs and merge the DataFrames using 'concat()'
for proxy in proxies:
    df2 = pd.read_csv(proxy, delimiter='\t', header=None, names=['http'])
    proxies_df = pd.concat([proxies_df, df2])
# Remove any duplicates and Reset the index of the final DataFrame
proxies_df.drop_duplicates(subset='http', inplace=True)
proxies_df.reset_index(drop=True, inplace=True)
df = proxies_df

# Configure Chrome to open URLs in new tabs
chrome_options = Options()
chrome_options.add_argument("--new-tab")

# User agents for simulating organic traffic
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    # Add more user agents here
]
os.environ["webdriver.chrome.driver"] = "/home/robinson/Desktop/proxyValidator/gilleadtheraphy.com/chromedriver"

# Search engine referrer URLs
referrer_urls = [
    "https://www.google.com/search?q=your+query",
    "https://www.bing.com/search?q=your+query",
    "https://www.yahoo.com/search?p=your+query",
    # Add more search engine URLs here
]
chrome_options.add_argument(f"--referer={random.choice(referrer_urls)}")

# Loop through each proxy in the list
for pro in df["http"]:
    # Check the validity of the proxy
    try:
        requests.get("https://iconect.co.ke/", proxies={"https": pro}, timeout=3)
    except:
        print(f"Skipping proxy {pro} (not working)")
        continue

    # Configure Chrome to use the proxy
    chromedriver = '/home/robinson/Desktop/proxyValidator/gilleadtheraphy.com/chromedriver'
    chrome_options.add_argument(f'--proxy-server={pro}')
    #chrome_options.add_argument('--headless')
# Create the Chrome driver using options
    chrome = webdriver.Chrome(options=chrome_options)
    # Randomize the order of URLs
    random.shuffle(url_list)

    # Visit each website only once
    for url in url_list:
        chrome.set_script_timeout(30)  # Set the timeout value in seconds
        chrome.execute_script("window.open('{}', '_blank')".format(url))
        visits_counter += 1
        time.sleep(random.uniform(5, 15))  # Random delay between 5 to 15 seconds
        print("Visited {} pages using proxies".format(visits_counter))

    chrome.quit()