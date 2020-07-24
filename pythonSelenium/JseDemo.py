# JS DOM can access any element on web page just like Selenium does
# Selenium has a method to execute javascript code in it
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Mr. Parker")
# no selinium attribute can be used to display the text entered by selenium script
# hence we use JSE
print(driver.find_element_by_name("name").get_attribute("value"))
# to give control to java script completely
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
