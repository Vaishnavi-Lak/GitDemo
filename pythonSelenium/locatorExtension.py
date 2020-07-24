from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_css_selector("#username").send_keys("case worker")
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
# navigating to username from grand parent
driver.find_element_by_css_selector("input.password").send_keys("case2345")
driver.find_element_by_css_selector("input.password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
# using Xpath with any text for the field
# //tagname[text()='xxx']
driver.find_element_by_xpath("//a[text()='Cancel']").click()
# navigating password from parent using css - ("form[name='login'] label:nth-child(2)")
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)

