from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.ca')

searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbox.send_keys('srilanka')

searchButton = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
searchButton.click()
