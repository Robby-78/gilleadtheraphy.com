import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

visits_counter = 0
url_list = [
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
"https://gileadtherapy.com/why-am-i-always-getting-heartburn/",
"https://gileadtherapy.com/why-am-i-always-getting-heartburn/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/why-am-i-always-getting-heartburn/",
"https://gileadtherapy.com/best-heartburn-relief/",
"https://gileadtherapy.com/best-heartburn-relief/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/best-heartburn-relief/",
"https://gileadtherapy.com/9-causes-of-heartburn-in-the-morning/",
"https://gileadtherapy.com/9-causes-of-heartburn-in-the-morning/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/9-causes-of-heartburn-in-the-morning/",
"https://gileadtherapy.com/what-causes-low-breast-milk-supply/",
"https://gileadtherapy.com/what-causes-low-breast-milk-supply/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/what-causes-low-breast-milk-supply/",
"https://gileadtherapy.com/what-triggers-migraines-12-science-backed-causes/",
"https://gileadtherapy.com/what-triggers-migraines-12-science-backed-causes/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/what-triggers-migraines-12-science-backed-causes/",
"https://gileadtherapy.com/17-home-remedies-for-fungal-infection/",
"https://gileadtherapy.com/17-home-remedies-for-fungal-infection/",
"https://gileadtherapy.com/17-home-remedies-for-fungal-infection/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/17-home-remedies-for-fungal-infection/",
"https://gileadtherapy.com/12-home-remedies-for-gout-pain/",
"https://gileadtherapy.com/12-home-remedies-for-gout-pain/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/12-home-remedies-for-gout-pain/",
"https://gileadtherapy.com/13-home-remedies-for-indigestion-a-review/",
"https://gileadtherapy.com/13-home-remedies-for-indigestion-a-review/",
"https://gileadtherapy.com/13-home-remedies-for-indigestion-a-review/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/13-home-remedies-for-indigestion-a-review/",
"https://gileadtherapy.com/infectious-diseases-an-overview/",
"https://gileadtherapy.com/infectious-diseases-an-overview/",
"https://gileadtherapy.com/infectious-diseases-an-overview/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/infectious-diseases-an-overview/",
"https://gileadtherapy.com/heartburn-home-remedies/",
"https://gileadtherapy.com/heartburn-home-remedies/",
"https://gileadtherapy.com/heartburn-home-remedies/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/heartburn-home-remedies/",
"https://gileadtherapy.com/dry-eyes-home-remedy/",
"https://gileadtherapy.com/dry-eyes-home-remedy/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/dry-eyes-home-remedy/",
"https://gileadtherapy.com/19-ways-to-improve-your-nights-sleep/",
"https://gileadtherapy.com/19-ways-to-improve-your-nights-sleep/",
"https://gileadtherapy.com/19-ways-to-improve-your-nights-sleep/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/19-ways-to-improve-your-nights-sleep/",
"https://gileadtherapy.com/toothache-home-remedies/",
"https://gileadtherapy.com/toothache-home-remedies/",
"https://gileadtherapy.com/toothache-home-remedies/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/toothache-home-remedies/",
"https://gileadtherapy.com/home-remedies-for-tonsils/",
"https://gileadtherapy.com/home-remedies-for-tonsils/",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/home-remedies-for-tonsils/",
"https://gileadtherapy.com/trichomoniasis-symptoms-diagnosis-and-cure/",
"https://gileadtherapy.com/trichomoniasis-symptoms-diagnosis-and-cure/",
"https://gileadtherapy.com/trichomoniasis-symptoms-diagnosis-and-cure/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/trichomoniasis-symptoms-diagnosis-and-cure/",
"https://gileadtherapy.com/home-remedies-for-irregular-periods/",
"https://gileadtherapy.com/home-remedies-for-irregular-periods/",
"https://gileadtherapy.com/home-remedies-for-irregular-periods/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/home-remedies-for-irregular-periods/",
"https://gileadtherapy.com/how-to-overcome-irregular-periods-naturally/",
"https://gileadtherapy.com/how-to-overcome-irregular-periods-naturally/",
"https://gileadtherapy.com/how-to-overcome-irregular-periods-naturally/#comments",
"https://gileadtherapy.com/category/general-health/",
"https://gileadtherapy.com/author/opindebarrack15gmail-com/",
"https://gileadtherapy.com/how-to-overcome-irregular-periods-naturally/",
"https://gileadtherapy.com/why-am-i-always-getting-heartburn/",
"https://gileadtherapy.com/what-foods-cause-heartburn/",
"https://gileadtherapy.com/foods-that-dont-cause-heartburn/",
"https://gileadtherapy.com/best-heartburn-relief/",


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
