from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://www.familysearch.org/en/")
# driver.maximize_window()
# driver.find_element_by_xpath("//button[@aria-controls='search']").click()
# driver.find_element_by_xpath("//a[@data-test='records']").click()
# ActionChains
# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_id("search")).perform()
# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.close()
# double click is used to double click on an item
# content click is used to right click on an item

