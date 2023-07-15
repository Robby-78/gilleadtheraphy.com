import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define the list of search engine URLs you want to visit
url_list = [
    'https://www.google.com/',
    'https://www.bing.com/',
    'https://www.yahoo.com/'
]

# Define the list of proxy URLs
proxies = [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
]

# Set the maximum time (in seconds) to keep a window open
window_timeout = 600  # 10 minutes

# Set the maximum time (in seconds) to keep a window open if proxy location is unknown
unknown_location_timeout = 180  # 3 minutes

# Function to get the country of a proxy using IP geolocation
def get_proxy_country(proxy):
    try:
        ip = proxy.split(':')[0]
        response = requests.get(f'https://ipapi.co/{ip}/country/')
        if response.status_code == 200:
            return response.text
    except:
        pass
    return 'Unknown'

# Function to find the best proxy based on response time to iconect.co.ke
def find_best_proxy(proxies):
    best_proxy = None
    best_response_time = float('inf')

    for proxy in proxies:
        try:
            start_time = time.time()
            requests.get('https://iconect.co.ke/', proxies={'https': proxy}, timeout=3)
            response_time = time.time() - start_time
            if response_time < best_response_time:
                best_proxy = proxy
                best_response_time = response_time
        except:
            pass
    
    return best_proxy

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument('--new-window')
chrome_options.add_argument('--start-maximized')

# Read the list of proxies
proxies_df = pd.DataFrame({'http': []})
for proxy in proxies:
    df2 = pd.read_csv(proxy, delimiter='\t', header=None, names=['http'])
    proxies_df = pd.concat([proxies_df, df2])
proxies_df.drop_duplicates(subset='http', inplace=True)
proxies_df.reset_index(drop=True, inplace=True)

# Function to open a new window with the specified URL and best proxy
def open_window_with_proxy(url, proxy):
    # Configure Chrome with the best proxy
    chrome_options.add_argument(f'--proxy-server={proxy}')
    
    # Open Chrome with the configured options
    with webdriver.Chrome(options=chrome_options) as chrome:
        # Open the URL in a new window
        chrome.get(url)
        
        # Determine the timeout based on proxy location
        country = get_proxy_country(proxy)
        timeout = window_timeout if country != 'Unknown' else unknown_location_timeout
        
        # Wait for the specified timeout period
        time.sleep(timeout)

# Loop through each URL
for url in url_list:
    # Find the best proxy
    best_proxy = find_best_proxy(proxies_df['http'])
    if best_proxy is None:
        print(f"No working proxy found for URL: {url}")
        continue
    
    open_window_with_proxy(url, best_proxy)
