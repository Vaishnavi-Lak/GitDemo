from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
lists = driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in lists:
    if i.get_attribute("value") == ("option2"):
        i.click()
        assert i.is_selected()
driver.find_element_by_css_selector("input[value = 'radio1']").click()
dd = Select(driver.find_element_by_id("dropdown-class-example"))
dd.select_by_visible_text("Option2")
# checking is_displayed() methods
assert driver.find_element_by_name("show-hide").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_name("show-hide").is_displayed()
# we know that the above statement should hide the text box. But if we put normal assert, it will fail the tc.
# hence we use assert not
