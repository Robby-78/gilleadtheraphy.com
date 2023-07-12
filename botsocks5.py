import os
import time
import random
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

visits_counter = 0

url_list = [
"https://gileadtherapy.com/",
"https://gileadtherapy.com/what-foods-cause-heartburn/",
"https://gileadtherapy.com/what-foods-cause-heartburn/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/what-foods-cause-heartburn/",
"https://gileadtherapy.com/foods-that-dont-cause-heartburn/",
"https://gileadtherapy.com/foods-that-dont-cause-heartburn/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/foods-that-dont-cause-heartburn/",
"https://gileadtherapy.com/11-foods-to-eat-if-you-have-irregular-periods/",
"https://gileadtherapy.com/11-foods-to-eat-if-you-have-irregular-periods/",
"https://gileadtherapy.com/11-foods-to-eat-if-you-have-irregular-periods/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/11-foods-to-eat-if-you-have-irregular-periods/",
"https://gileadtherapy.com/natural-remedies-for-hormonal-imbalance-in-females/",
"https://gileadtherapy.com/natural-remedies-for-hormonal-imbalance-in-females/",
"https://gileadtherapy.com/natural-remedies-for-hormonal-imbalance-in-females/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/natural-remedies-for-hormonal-imbalance-in-females/",
"https://gileadtherapy.com/13-home-remedies-for-abscess/",
"https://gileadtherapy.com/13-home-remedies-for-abscess/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/13-home-remedies-for-abscess/",
"https://gileadtherapy.com/best-heartburn-relief/",
"https://gileadtherapy.com/best-heartburn-relief/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/best-heartburn-relief/",
"https://gileadtherapy.com/9-causes-of-heartburn-in-the-morning/",
"https://gileadtherapy.com/9-causes-of-heartburn-in-the-morning/",
"https://gileadtherapy.com/category/general-health/",
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
        requests.get("https://gileadtherapy.com/", proxies={"https": pro}, timeout=3)
    except:
        print(f"Skipping proxy {pro} (not working)")
        continue

    # Configure Chrome to use the proxy
    chromedriver = '/home/robinson/Desktop/proxyValidator/gilleadtheraphy.com/chromedriver'
    chrome_options.add_argument(f'--proxy-server={pro}')
    chrome_options.add_argument('--headless')
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
