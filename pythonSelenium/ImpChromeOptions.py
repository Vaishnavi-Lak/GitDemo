from selenium import webdriver

chromeopts = webdriver.ChromeOptions()
chromeopts.add_argument("--start-maximized")
chromeopts.add_argument("headless") #browser wont be displayed
chromeopts.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chromeopts)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)