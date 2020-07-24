from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_name("enter-name").send_keys("John")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()
assert "John" in alertText
driver.find_element_by_id("confirmbtn").click()
alert2 = driver.switch_to.alert
print(alert2.text)
alert2.dismiss()


