from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://kydph--ctdev.my.salesforce.com")
driver.find_element_by_css_selector("#username").send_keys("uat_ct_dsinv_02@mailinator.com.kydph.ctdev")
driver.find_element_by_css_selector("input.password").send_keys("Pa$$w0rd.1")
driver.find_element_by_id("Login").click()
driver.find_element_by_css_selector("input[id='159:0;p']").send_keys("00002014")