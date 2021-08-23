# link_scraper

## Description
This is a small script built for SecureSet's Networks 400 Module to explore webscrapping.  This python script runs in the terminal and will gather the links for an initial site and all the external links found on each of those links.

This was tested using http://www.example.com however, it is built for users to input whatever site they want.

Note: There is currently no delays added to the site to be polite about the webscraping.

# Getting Started

## Downloading python


This needs to be Python version `3.9` or up

MacOS
   * From Python's official website [here](https://www.python.org/downloads/mac-osx/)
   * If you have [brew](https://brew.sh) installed, you can just run the coommand `brew install python3`

Linux
   * From Python's official website [here](https://www.python.org/downloads/source/)
   * Using the package manager for your system. With Ubuntu, this command is `sudo apt install python3-dev`

Windows
   * From Python's official website [here](https://www.python.org/downloads/windows/)
   * If you have the [Chocolatey package manager](https://chocolatey.org/) installed, you can run `choco install python`


# Current Dependencies

At the moment this code only requires the following dependencies to run:

```
pip install requests
pip install beautifulsoup4

```

Requests Documentation is located [here](https://docs.python-requests.org/en/master/)
BeautifulSoup Documentation is located [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)

# ToDos:

1. add sleep timers to not overun websites
2. change outputs to dictionary in order to label where links are coming from
3. add a way to export lists into external files/csv
 
