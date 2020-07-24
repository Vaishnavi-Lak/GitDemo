import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("http://makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder = 'From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for i in cities:
    print(i.text)
   # if i == "Del Rio, United States":
       # i.click()
