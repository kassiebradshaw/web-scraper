import requests
from bs4 import BeautifulSoup

# WORKING FUNCTIONS START ON LINE 28
# This top part is just my notes & attempts as I was working through and figuring things out.

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

# page = requests.get(URL)
# # print(page.content)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# look for class detail information for what we're looking for...

# <sup class="noprint Inline-Template Template-Fact">
# a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed"
# span title="This claim needs references to reliable sources. (October 2011)" -- date is different on all citations needed
# <span>citation needed</span>

# class for citations needed
# citations_needed = soup.find_all(class_="noprint Inline-Template Template-Fact")
# print(results)

# for cite in citations_needed:
#   print (cite.parent.text)

#---------- WEB SCRAPER FUNCTIONS -------------

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