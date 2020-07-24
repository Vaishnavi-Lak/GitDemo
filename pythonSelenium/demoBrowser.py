from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke the executable file to automate the actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.vmtours.net/") # get method helps to url in browser
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.vmtours.net/tour-packages.html")
driver.get("https://www.vmtours.net/why-travel-agent.html")
# driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.close()