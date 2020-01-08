from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Firefox()
driver.get("http://web.whatsapp.com")
input("Scan the Code Then Press Enter..")
rangeenter = int(input("Range: "))
contact = "FBI"

#TODO 
text = "repetitive message id_"
#TODO
inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys("****************************" + Keys.ENTER)

for i in range(rangeenter):
    print(i, " Sent")
    input_box.send_keys(text+str(i) + Keys.ENTER)
    time.sleep(0.1)
time.sleep(2)
input("FINISHED PRESS ENTER TO QUIT")
driver.close()
