from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time

driver = webdriver.Firefox()

url = 'http://127.0.0.1:8000/'
username = 'username' #id
password = 'pwd' #id
btn_logar = 'logar' #name
  
def navigate():
  driver.get(url)


def login(username='qa_tester', password='abacatecomarroz2323'):
  driver.find_element_by_id(username).send_keys(username)
  driver.find_element_by_id(password).send_keys(password)
  driver.find_element_by_name(btn_logar).click()

navigate()
time.sleep(5)
login()

