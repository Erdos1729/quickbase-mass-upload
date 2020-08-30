"""
Created on Tue Aug  30 14:53:35 2020

@author: Erdos1729
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


# 1: Add correct address below
chromedriver = './chrome_driver/chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://ma.quickbase.com/")
username = driver.find_element_by_name("loginid")
password = driver.find_element_by_name("password")


# 2: Enter Username and Password here
username.send_keys("enter username")    # Enter username here
password.send_keys("enter password")    # Enter password here
driver.find_element_by_id("signin").click()

df = pd.read_csv('./doclinks.csv')

for i in range(1, len(df)):
    driver.get(df['Target'][i])
    driver.find_element_by_id("_fid_79").send_keys(df['Source'][i])  # Enter the id of "choose file" button here
    time.sleep(1)
    ActionChains(driver).key_down(Keys.CONTROL).key_down("s").key_up(Keys.CONTROL).key_up("s").perform()
    WebDriverWait(driver, 30).until(EC.url_changes)
    time.sleep(1)

driver.quit()