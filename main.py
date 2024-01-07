import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import string

from functions import season_scrapper
base_url='https://www.transfermarkt.pl/uefa-champions-league/teilnehmer/pokalwettbewerb/CL/saison_id/'
driver = webdriver.Chrome()

season_scrapper(base_url, driver)