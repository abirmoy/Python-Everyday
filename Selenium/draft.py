from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://darknetdiaries.com/episode/2/')

driver.implicitly_wait(10) # seconds
driver.find_element(By.XPATH, '/html/body/div/div/div[4]/button[1]')
# driver.close()