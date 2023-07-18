import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

visits_counter = 0
url_list = [
"https://ipapi.co/{ip}/country",
"https://iconect.co.ke/india-surpass-china-population-growth",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/Central American Migrants Demand Justice and Better Treatment in Mexico as They March Towards Mexico City",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/from-snowden-to-teixeira-the-never-ending-battle-against-national-security-threats-posed-by-classified-information-leaks",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/kenyan-news",
"https://iconect.co.ke/idd-ul-fitr-declared-national-holiday-in-kenya-for-muslims",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/nairobi-diaries-a-look-into-the-lives-of-young-urban-kenyans-on-reality-tv",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/tahmeed-unveils-new-scania-f360-buses-for-nairobi-dar-es-salaam-and-nairobi-malindi-routes-enhancing-safety-comfort-and-sustainability-in-east-african-transportation",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/turkana-county-launches-fcdc-policy-and-act-2022-to-enhance-peacebuilding-efforts",
]

proxies = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
           "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
           "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
           "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
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
#chrome_options.add_argument('--headless')  # Enable headless mode

# Set the referrer header for requests
headers = {
    'Referer': 'https://iconect.co.ke/'
}

# Loop through each proxy in the list
for pro in df["http"]:
    # Check the validity of the proxy
    try:
        requests.get("https://iconect.co.ke/", proxies={"https": pro}, timeout=3, headers=headers)
    except:
        print(f"Skipping proxy {pro} (not working)")
        continue

    # Configure Chrome to use the proxy
    chrome_options.add_argument('--proxy-server=%s' % pro)

    # Initialize the Chrome driver with the options
    with webdriver.Chrome(options=chrome_options) as chrome:
        # Visit each website only once
        for url in url_list:
            # Open a new window
            chrome.execute_script("window.open()")

            # Switch to the newly opened window
            chrome.switch_to.window(chrome.window_handles[-1])

            chrome.get(url)
            visits_counter += 1
            time.sleep(5)
            print("Visited {} pages using proxies".format(visits_counter))
        time.sleep(100)
