from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

casenumber = "00011317"
chromeopts = webdriver.ChromeOptions()
chromeopts.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://kydph--ctsit.my.salesforce.com")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("sit_ct_dsinv_01@mailinator.com.kydph.ctsit")
driver.find_element_by_id("password").send_keys("Pa$$w0rd.1")
driver.find_element_by_name("Login").click()
driver.find_element_by_id("159:0;p").send_keys(casenumber)
w = WebDriverWait(driver, 5)
w.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a[class*='MRU_GLOBAL']")))
driver.find_element_by_css_selector("a[class*='MRU_GLOBAL']").click()
# driver.find_element_by_link_text(casenumber).click()
texts = driver.find_element_by_css_selector("div[class*='flexipageRichText").text
print(texts)
w = WebDriverWait(driver, 7)
w.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@title='Accept']")))
driver.find_element_by_xpath("//a[@title='Accept']").click()
driver.find_element_by_xpath("//button[@type='button']").click()

