import time
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

proxies = [
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
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

# Filter proxies to include only USA proxies
df['country'] = df['http'].apply(get_proxy_country)
df = df[df['country'] == 'United States']

# Configure Chrome to open URLs in new tabs
chrome_options = Options()
chrome_options.add_argument("--new-tab")
chrome_options.add_argument('--headless')

# Loop through each proxy in the list
for pro in df["http"]:
    # Check the validity of the proxy
    try:
        requests.get("https://iconect.co.ke/", proxies={"https": pro}, timeout=3)
        country = get_proxy_country(pro)
        print(f"Proxy: {pro} - Country: {country}")
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
            time.sleep(5)
            print("Visited {} pages using proxy {} ({})".format(visits_counter, pro, country))
        time.sleep(100)
