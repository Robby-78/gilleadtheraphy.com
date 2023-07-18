from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Provide the path to your Chrome WebDriver executable
webdriver_path = '/chromedriver'

try:
    # Create a new Chrome WebDriver instance with options
    driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

    url = "https://iconect.co.ke"

    # Load the page
    driver.get(url)

    # Get the page source
    html_content = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the <a> tags
    links = soup.find_all('a')

    # Extract the URLs
    url_list = []
    for link in links:
        url = link.get('href')
        if url and not url.startswith('#'):
            url_list.append(url)

    # Print the URLs
    for url in url_list:
        print(f'"{url}",')

except Exception as e:
    print(f'Failed to retrieve the page. Error: {str(e)}')

finally:
    # Quit the WebDriver
    webdriver.quit()
