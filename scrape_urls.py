import requests
from bs4 import BeautifulSoup

url = "https://gileadtherapy.com/blog"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

# Send a GET request to the website with the headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all anchor tags (links)
    all_links = soup.find_all("a")

    # Extract the href attribute from each link
    urls = [link.get("href") for link in all_links]

    # Save the URLs to urls.txt
    with open("urls.txt", "w") as file:
        for link in urls:
            file.write(f'"{link}",\n')
else:
    print(f"Error: {response.status_code}")
