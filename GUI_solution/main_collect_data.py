from Scraper import *
from config import *
import requests
from bs4 import BeautifulSoup


DDSM_page = requests.get(DDSM_url)
DDSM_html = BeautifulSoup(DDSM_page.text)
DDSM_table = DDSM_html.find('table')
DDSM_links = DDSM_table.findAll('a')

Scraper(DDSM_links)