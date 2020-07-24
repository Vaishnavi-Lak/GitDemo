from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
# we are using this as it is one of the attributes present in inspect element
# driver.find_element_by_name("name").send_keys("John")
driver.find_element_by_css_selector("input[name='name']").send_keys("John")
driver.find_element_by_name("email").send_keys("John123@asi.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("john1234")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)

# select class provides methods to handle the options in the dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value() - is used when the select tag contains options specified as values



# $x("//*[contains(@class,'alert-success')]")
# $("[class*='alert-success']")
