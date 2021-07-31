# Lab 17 - Web Scraper

*Author*: Kassie Bradshaw

[Link to code](web_scraper/scraper.py)

[Link to Pull Request]()

---

## Overview

Let's code up a web scraper that can automate the process of manually using the site.

---

## Feature Tasks & Requirements

* [ ] Scrape a Wikipedia page and record which passages need citations
  * [ ] Example: [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico) has 5 "citation needed" cases, as of this writing.
* [ ] Your web scraper should report the number of citations needed
* [ ] Your web scraper should identify those cases AND include the relevant passage.
  * [ ] Example: Citation needed for "lorem spam and impsum eggs"
  * [ ] Consider the "relevant passage" to be the parent element that contains the passage, often a paragraph element

## Implementation Notes

* [ ] Count function must be named **get_citations_needed_count**
  * get_citations_needed takes in a url and returns an integer
* [ ] Report function must be named **get_citations_needed_report**
  * get_citations_needed_report takes in a url and returns a string
  * the string should be formatted with each citation needed on own line, in order found
* [ ] Module must be named scraper.py

## Stretch Goals

* [ ] Organize the needed citations by section (i.e. the parent heading tag)
  * Name additional function **get_citations_needed_by_section**
* [ ] Automatically do a citation scan for any links from the main section of wikipedia page

## User Acceptance Tests

* [ ] Verify that the correct count of citations needed is calculated
* [ ] Verify that preceding passage