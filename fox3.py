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
"https://iconect.co.ke/Central American Migrants Demand Justice and Better Treatment in Mexico as They March Towards Mexico City",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/from-snowden-to-teixeira-the-never-ending-battle-against-national-security-threats-posed-by-classified-information-leaks",
"https://iconect.co.ke/from-snowden-to-teixeira-the-never-ending-battle-against-national-security-threats-posed-by-classified-information-leaks",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/kenyan-news",
"https://iconect.co.ke/idd-ul-fitr-declared-national-holiday-in-kenya-for-muslims",
"https://iconect.co.ke/idd-ul-fitr-declared-national-holiday-in-kenya-for-muslims",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/nairobi-diaries-a-look-into-the-lives-of-young-urban-kenyans-on-reality-tv",
"https://iconect.co.ke/nairobi-diaries-a-look-into-the-lives-of-young-urban-kenyans-on-reality-tv",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/tahmeed-unveils-new-scania-f360-buses-for-nairobi-dar-es-salaam-and-nairobi-malindi-routes-enhancing-safety-comfort-and-sustainability-in-east-african-transportation",
"https://iconect.co.ke/tahmeed-unveils-new-scania-f360-buses-for-nairobi-dar-es-salaam-and-nairobi-malindi-routes-enhancing-safety-comfort-and-sustainability-in-east-african-transportation",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/turkana-county-launches-fcdc-policy-and-act-2022-to-enhance-peacebuilding-efforts",
"https://iconect.co.ke/turkana-county-launches-fcdc-policy-and-act-2022-to-enhance-peacebuilding-efforts",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/tragedy-in-bomet-father-kills-two-sons-in-a-fit-of-rage",
"https://iconect.co.ke/tragedy-in-bomet-father-kills-two-sons-in-a-fit-of-rage",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/african-news",
"https://iconect.co.ke/deadly-cobra-in-south-african-airways-cockpit-forces-emergency-landing",
"https://iconect.co.ke/deadly-cobra-in-south-african-airways-cockpit-forces-emergency-landing",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/zimbabwe-democratic-space-shrinking-human-rights-concerns",
"https://iconect.co.ke/zimbabwe-democratic-space-shrinking-human-rights-concerns",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/afreximbank-and-kenya-collaborate-to-boost-industrial-renaissance-and-trade-development",
"https://iconect.co.ke/afreximbank-and-kenya-collaborate-to-boost-industrial-renaissance-and-trade-development",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/lesotho-mp-demands-huge-parts-of-south-africa",
"https://iconect.co.ke/lesotho-mp-demands-huge-parts-of-south-africa",
"https://iconect.co.ke/profile/ferrary-kirui",
"https://iconect.co.ke/angelique-kidjo-wins-polar-music-prize",
"https://iconect.co.ke/angelique-kidjo-wins-polar-music-prize",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/sports-news",
"https://iconect.co.ke/inter-milan-vs-ac-milan-champions-league-semifinal-preview",
"https://iconect.co.ke/inter-milan-vs-ac-milan-champions-league-semifinal-preview",
"https://iconect.co.ke/profile/admin",
"https://iconect.co.ke/why-always-me-the-story-behind-mario-balotellis-iconic-catchphrase",
"https://iconect.co.ke/why-always-me-the-story-behind-mario-balotellis-iconic-catchphrase",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/the-thrill-of-formula-one-a-look-into-the-worlds-most-advanced-motorsport",
"https://iconect.co.ke/the-thrill-of-formula-one-a-look-into-the-worlds-most-advanced-motorsport",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/clippers-edge-suns-in-game-1-of-nba-playoffs-paul-george-leads-with-34-points",
"https://iconect.co.ke/clippers-edge-suns-in-game-1-of-nba-playoffs-paul-george-leads-with-34-points",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/ai-in-football-from-player-performance-analysis-to-club-management-is-it-ready",
"https://iconect.co.ke/ai-in-football-from-player-performance-analysis-to-club-management-is-it-ready",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/politics",
"https://iconect.co.ke/the-ongoing-conflict-in-ethiopias-tigray-region-challenges-and-implications-for-africa",
"https://iconect.co.ke/the-ongoing-conflict-in-ethiopias-tigray-region-challenges-and-implications-for-africa",
"https://iconect.co.ke/profile/ian",
"https://iconect.co.ke/east-africa-spectre-limited-attacked-security-concerns",
"https://iconect.co.ke/east-africa-spectre-limited-attacked-security-concerns",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/transport-paralysed-in-migori",
"https://iconect.co.ke/transport-paralysed-in-migori",
"https://iconect.co.ke/profile/ferrary-kirui",
"https://iconect.co.ke/how-kenyan-demonstrations-raises-costs-of-living",
"https://iconect.co.ke/how-kenyan-demonstrations-raises-costs-of-living",
"https://iconect.co.ke/profile/Rono",
"https://iconect.co.ke/opposition-mps-criticize-government-over-security-detail-withdrawal",
"https://iconect.co.ke/opposition-mps-criticize-government-over-security-detail-withdrawal",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/tech",
"https://iconect.co.ke/stoichiometric-air-fuel-ratio-basic-engineering",
"https://iconect.co.ke/stoichiometric-air-fuel-ratio-basic-engineering",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/weigh-feeders-material-handling-with-its-innovation",
"https://iconect.co.ke/weigh-feeders-material-handling-with-its-innovation",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/the-theory-of-twisting-torsion",
"https://iconect.co.ke/the-theory-of-twisting-torsion",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/thermodynamic-cycles",
"https://iconect.co.ke/thermodynamic-cycles",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/maximizing-performance-and-energy-efficiency-in-boiler-systems",
"https://iconect.co.ke/maximizing-performance-and-energy-efficiency-in-boiler-systems",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/article",
"https://iconect.co.ke/components-of-sugarcane-factory-mon",
"https://iconect.co.ke/components-of-sugarcane-factory-mon",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/the-power-of-choice-understanding-the-consequences-of-our-decisions",
"https://iconect.co.ke/the-power-of-choice-understanding-the-consequences-of-our-decisions",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/ezekiel-2517-understanding-the-power-and-purpose-of-gods-vengeance",
"https://iconect.co.ke/ezekiel-2517-understanding-the-power-and-purpose-of-gods-vengeance",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/legacy-communications-preserving-history-memories",
"https://iconect.co.ke/legacy-communications-preserving-history-memories",
"https://iconect.co.ke/profile/Patricky",
"https://iconect.co.ke/time-study-and-work-measurement-standard-times",
"https://iconect.co.ke/time-study-and-work-measurement-standard-times",
"https://iconect.co.ke/profile/agsey",
"https://iconect.co.ke/business",
"https://iconect.co.ke/the-remarkable-journey-of-john-d-rockefeller-and-the-legacy-of-standard-oil",
"https://iconect.co.ke/the-remarkable-journey-of-john-d-rockefeller-and-the-legacy-of-standard-oil",
"https://iconect.co.ke/profile/ferrary-kirui",
"https://iconect.co.ke/the-tesla-model-s-redefining-performance-range-and-design-in-electric-cars",
"https://iconect.co.ke/the-tesla-model-s-redefining-performance-range-and-design-in-electric-cars",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/china-offers-olive-branch-to-entrepreneurs-as-jack-ma-returns",
"https://iconect.co.ke/china-offers-olive-branch-to-entrepreneurs-as-jack-ma-returns",
"https://iconect.co.ke/profile/ferrary-kirui",
"https://iconect.co.ke/amazon-from-online-bookstore-to-global-powerhouse-in-e-commerce-streaming-cloud-computing-and-ai",
"https://iconect.co.ke/amazon-from-online-bookstore-to-global-powerhouse-in-e-commerce-streaming-cloud-computing-and-ai",
"https://iconect.co.ke/profile/Ghost",
"https://iconect.co.ke/former-treasury-official-warns-of-complete-economic-implosion-if-us-dollar-loses-global-reserve-currency-status",
"https://iconect.co.ke/former-treasury-official-warns-of-complete-economic-implosion-if-us-dollar-loses-global-reserve-currency-status",
"https://iconect.co.ke/profile/ferrary-kirui",


]

proxies = [  "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
           "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
           "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
           "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
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
