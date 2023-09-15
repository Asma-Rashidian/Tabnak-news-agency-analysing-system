"""Get links of news from Tabnak news agency"""

import requests
from bs4 import BeautifulSoup

main_url = 'https://www.tabnak.ir'

try:
    # Make the request and get the page content
    response = requests.get(main_url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links with class 'picLink'
    links = [main_url + link.get('href') for link in soup.find_all("a" , {"class":"picLink"})]

    # Write the links to the file
    with open("links.txt", 'w') as writer:
        for link in links:
            writer.write(link + '\n')
    print("All links have been stored successfully!")

except requests.exceptions.RequestException as e:
    print("An error occurred during the HTTP request:", str(e))
except Exception as e:
    print("An error occurred:", str(e))