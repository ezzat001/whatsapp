from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
driver = webdriver.Firefox()
driver.get("http://web.whatsapp.com")
input("Scan the Code Then Press Enter..")
contact = "FBI"

inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
html = driver.page_source
# soup = BeautifulSoup(html)
#//a[contains(@href, '/mathscinet/search/mscdoc.html')]
#get_button = driver.find_elements_by_xpath("//span[contains(@title, 'You')]")
get_button = driver.find_elements_by_xpath("//span[@title='"+contact+"']")
    
get_button[-1].click()
time.sleep(6)
driver.find_element_by_xpath("//div[contains(text(), 'more')]").click() #_3H4MS
noopart = driver.find_element_by_xpath("//span[contains(text(), 'participants')]")
print(noopart.text)
#transition: none 0s ease 0s; height: 72px; transform: translateY
participants = driver.find_elements_by_xpath("//div[contains(@style,'transition: none 0s ease 0s; height: 72px; transform: translateY')]")
for i in participants:
    print(i.text)
input("enter to break")
driver.close()
