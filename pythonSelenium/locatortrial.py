from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.vmtours.net/contact-us.html")
# we are using this as it is one of the attributes present in inspect element
driver.find_element_by_name("name").send_keys("John")
# driver.find_element_by_css_selector("input[name='name']").send_keys("John")
driver.find_element_by_name("email").send_keys("John123@asi.com")
driver.find_element_by_id("phone").send_keys("99887766")
# driver.find_element_by_xpath("//input[@type=submit]").click()