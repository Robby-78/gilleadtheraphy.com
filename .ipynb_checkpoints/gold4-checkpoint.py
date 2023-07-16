import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

visits_counter = 0
url_list = [
    'https://google.com/'
]

proxies = [ 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt', 
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    

]

proxies_df = pd.DataFrame({'http': []})

# Iterate over the proxy URLs and merge the DataFrames using 'concat()'
for proxy in proxies:
    df2 = pd.read_csv(proxy, delimiter='\t', header=None, names=['http'])
    proxies_df = pd.concat([proxies_df, df2])

# Remove any duplicates and reset the index of the final DataFrame
proxies_df.drop_duplicates(subset='http', inplace=True)
proxies_df.reset_index(drop=True, inplace=True)
df = proxies_df

# Configure Chrome to open URLs in new tabs
chrome_options = Options()
chrome_options.add_argument("--new-tab")
#chrome_options.add_argument('--headless')

# Loop through each proxy in the list
for pro in df["http"]:
    # Check the validity of the proxy
    try:
        requests.get("https://www.google.com/", proxies={"https": pro}, timeout=3)
    except:
        print(f"Skipping proxy {pro} (not working)")
        continue

    # Configure Chrome to use the proxy
    chrome_options.add_argument('--proxy-server=%s' % pro)

    # Initialize the Chrome driver with the options
    with webdriver.Chrome(options=chrome_options) as chrome:
        # Visit each website only once
        for url in url_list:
            chrome.execute_script("window.open('{}', '_blank')".format(url))
            visits_counter += 1
            time.sleep(50)
            print("Visited {} pages using proxies".format(visits_counter))
        time.sleep(900)
