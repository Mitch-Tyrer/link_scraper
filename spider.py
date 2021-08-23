import requests
from bs4 import BeautifulSoup as bs
import pprint


#website = 'http://www.example.com'
website = input("What webiste do you want to scrape? Include the 'http://' :")

# Headers required for HTTPS requests
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

#Empty List to store the inital site that was scraped
starting_site_links = []

# Function to parse any website using Beautiful Soup.
def html_parser(url):
    r = requests.get(url, headers=headers)
    soup = bs(r.text, 'html.parser')
    return soup

#Function to get all the links from a given webpage
def getLinks(url):
    # List to store the scraped links
    scraped_links = []
    # Call Parser Function from above
    soup = html_parser(url)
    # Iterate through the parsed page and find all the anchor tags
    for link in soup.find_all('a'):
        # Gets the href from the anchor tag
        href = link.get('href')
        # makes sure that it isn't empty
        if href != None:
            # if a full link (includes http) append it to the list. If a relative link to same domain, prepend with the url
            if 'http' in href:
                scraped_links.append(href)
            else:
                scraped_links.append(url + href)
    #clean up the list by using set to make sure there are no duplicates, then create a new list with that cleaned up list and return it
    cleanup = set(scraped_links)
    results = list(cleanup)
    return results

# assign the results of the initial site scrape and print the results
print("Starting Websites Links: \n")
starting_site_links = getLinks(website)
pprint.pprint(starting_site_links)
print('\n')

# Iterate over the starting sites links and run the getLinks Function for each one and append it to a new list
external_links = []
for link in starting_site_links:
    external_links.append(getLinks(link))

print("External Links from Starting Site Links: \n")
pprint.pprint(external_links)
