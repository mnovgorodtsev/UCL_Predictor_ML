import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import string


base_url='https://www.transfermarkt.pl/uefa-champions-league/teilnehmer/pokalwettbewerb/CL/saison_id/'
season_list=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015',
             '2016','2017','2018','2019','2020','2021','2022','2023']
def season_scrapper(base_url, driver):
    for year in season_list:
        current_url=base_url+year
        driver.get(current_url)
        driver.implicitly_wait(10)
        time.sleep(10)
        driver.switch_to.frame(driver.find_element(By.ID,"sp_message_iframe_954058"))
        button=driver.find_element(By.XPATH,'//*[@id="notice"]/div[3]/div[1]/div/button')
        button.click()
        time.sleep(123)






