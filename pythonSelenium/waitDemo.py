import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

veglist = []
veglist2 = []
sum = 0
sums = 0
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
# wait until 5 secs till object is displayed
# global wait
# resumes execution if object loads earlier
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ap")
time.sleep(4)
print(len(driver.find_elements_by_xpath("//div[@class='products']/div")))
sel = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for i in sel:
    veglist.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()
print(veglist)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# explicit wait
w = WebDriverWait(driver, 6)
w.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[class='promoCode']")))

list2 = driver.find_elements_by_xpath("//p[@class='product-name']")
for j in list2:
    veglist2.append(j.text)
    prices = (j.find_element_by_xpath("parent::td/parent::tr/td[5]/p")).text
    sums += int(prices)
print(veglist2)
print(sums)

assert veglist == veglist2

driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
originalamt = driver.find_element_by_class_name("discountAmt").text
driver.find_element_by_css_selector(".promoBtn").click()
w.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
discountamt = driver.find_element_by_class_name("discountAmt").text

assert float(discountamt) < int(originalamt)
print(driver.find_element_by_class_name("promoInfo").text)

prices = driver.find_elements_by_xpath("//tr/td[5]/p")
for p in prices:
    sum = sum + int(p.text)
print(sum)
# similar one is present in the for loop above

pricefinal = driver.find_element_by_class_name("totAmt").text

assert sum == int(pricefinal)
