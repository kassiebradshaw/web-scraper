import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def web_scraper(url):
  """This will invokes both of the other functions
  Input <-- URL
  Output <-- returns from required functions
  """
  get_citations_needed_count(url)
  get_citations_needed_report(url)

def get_citations_needed_count(url):
  """ 
  Input <-- URL
  Output <-- Integer representing number of citations needed
  """
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  citations_needed = soup.find_all(class_="noprint Inline-Template Template-Fact")
  
  print(len(citations_needed))

def get_citations_needed_report(url):
  """
  Input <-- URL
  Output <-- string, formatted with each citation on own line in order found
  """
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  citations_needed = soup.find_all(class_="noprint Inline-Template Template-Fact")

  for cite in citations_needed:
    print(cite.parent.text)
  
# --------- STRETCH GOAL ----------

# def get_citations_needed_by_section(url):
#   """
#   Input <-- URL
#   Output <-- Organizes the needed citations by section (i.e. the parent heading tag)
#   """
#   page = requests.get(url)
#   soup = BeautifulSoup(page.content, 'html.parser')
#   headings = soup.find_all(class_="mw-headline")

# -------- TESTING MY FUNCTIONS -------------

# get_citations_needed_count(URL) # <-- works

# get_citations_needed_report(URL) # <-- works

# get_citations_needed_by_section(URL) # <-- didn't get it figured out

web_scraper(URL)