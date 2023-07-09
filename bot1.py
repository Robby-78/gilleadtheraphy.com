import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import random

iterations = 5  # Number of iterations to repeat the process
url_list = [
"https://gileadtherapy.com/blog/",
"https://gileadtherapy.com/natural-remedies-for-hormonal-imbalance-in-females/",
"https://gileadtherapy.com/natural-remedies-for-hormonal-imbalance-in-females/",
'https://gileadtherapy.com/13-home-remedies-for-abscess/',
"https://gileadtherapy.com/best-heartburn-relief/",
'https://gileadtherapy.com/9-causes-of-heartburn-in-the-morning/',
'https://gileadtherapy.com/11-home-remedies-for-premature-ejaculation/',
'https://gileadtherapy.com/what-causes-low-breast-milk-supply/',
'https://gileadtherapy.com/what-triggers-migraines-12-science-backed-causes/',
'https://gileadtherapy.com/17-home-remedies-for-fungal-infection/',
'https://gileadtherapy.com/12-home-remedies-for-gout-pain/',
'https://gileadtherapy.com/13-home-remedies-for-indigestion-a-review/',
'https://gileadtherapy.com/heartburn-home-remedies/',
'https://gileadtherapy.com/dry-eyes-home-remedy/',
'https://gileadtherapy.com/19-ways-to-improve-your-nights-sleep/',
'https://gileadtherapy.com/toothache-home-remedies/',
'https://gileadtherapy.com/home-remedies-for-tonsils/',
'https://gileadtherapy.com/trichomoniasis-symptoms-diagnosis-and-cure/',
'https://gileadtherapy.com/home-remedies-for-irregular-periods/',
'https://gileadtherapy.com/how-to-overcome-irregular-periods-naturally/',
'https://gileadtherapy.com/home-remedies-for-excessive-gas/',
"https://gileadtherapy.com/blog/page/2/natural-remedies-for-hormonal-imbalance-in-females/",
"https://gileadtherapy.com/blog/page/2/5-tips-for-a-healthy-lifestyle/",
"https://gileadtherapy.com/blog/page/2/benefits-of-exercise/",
"https://gileadtherapy.com/blog/page/2/understanding-mental-health/",
"https://gileadtherapy.com/blog/page/3/the-power-of-mindfulness/",
"https://gileadtherapy.com/blog/page/3/taking-care-of-your-emotional-well-being/",
"https://gileadtherapy.com/blog/page/3/importance-of-sleep-for-well-being/",
"https://gileadtherapy.com/blog/page/4/strategies-for-managing-stress/",
"https://gileadtherapy.com/blog/page/4/nutrition-and-mental-health/",
] 

# Read the list of proxies from the JSON file
proxy_url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
try:
    response = requests.get(proxy_url)
    proxy_lines = response.text.split('\n')
    proxy_list = [line.split()[0] for line in proxy_lines if line.strip() and not line.startswith('#')]
except:
    print("Failed to fetch proxy list from the URL.")
    exit()

# Create a DataFrame to store the proxies
proxies_df = pd.DataFrame({'http': proxy_list})

# Remove any duplicates and reset the index of the final DataFrame
proxies_df.drop_duplicates(subset='http', inplace=True)
proxies_df.reset_index(drop=True, inplace=True)
df = proxies_df

# Configure Chrome to open URLs in new tabs
chrome_options = Options()
chrome_options.add_argument("--new-tab")

# Define a list of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    # Add more user agents
]

# Define a list of devices to emulate
emulated_devices = [
    {"width": 360, "height": 640, "pixelRatio": 2.0, "deviceScaleFactor": 2.0, "mobile": True},
    {"width": 1024, "height": 768, "pixelRatio": 1.0, "deviceScaleFactor": 1.0, "mobile": False},
    # Add more devices
]
#Repeat the process for the specified number of iterations
# Repeat the process for the specified number of iterations
for _ in range(iterations):
    # Loop through each proxy in the list
    for index, row in df.iterrows():
        pro = row['http']

        # Check the validity of the proxy
        try:
            requests.get("https://www.google.com/", proxies={"https": pro}, timeout=3)
        except:
            print(f"Skipping proxy {pro} (not working)")
            continue

        # Configure Chrome to use the proxy
        chrome_options.add_argument('--proxy-server=%s' % pro)

        # Randomly select a user agent and device
        user_agent = random.choice(user_agents)
        device = random.choice(emulated_devices)
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_experimental_option('mobileEmulation', device)

        with webdriver.Chrome(options=chrome_options) as driver:
            # Enable session persistence
            driver.implicitly_wait(5)  # Adjust the wait time as needed

            # Visit the first URL to start from the homepage
            first_url = url_list[0]
            driver.get(first_url)
            time.sleep(random.uniform(3, 6))  # Randomize the delay between actions

            # Set referrer spoofing
            headers = {
                'Referer': 'https://www.google.com/'  # Spoof the referrer to appear as if coming from Google
            }
            for url in url_list[1:]:
                # Spoof the referrer in the request headers
                driver.execute_script(f"window.open('{url}', '_blank', 'noopener,noreferrer', false, {headers})")
                time.sleep(random.uniform(3, 6))  # Randomize the delay between actions
               

            time.sleep(70)  # Wait for a longer period before 