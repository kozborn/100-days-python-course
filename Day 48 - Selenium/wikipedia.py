from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

stats = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(stats.text)

driver.find_element(By.LINK_TEXT, value="Untitled Goose Game").click()

search_input = driver.find_element(By.NAME, value='search')
search_input.clear()

search_input.send_keys("money")
search_input.send_keys(Keys.RETURN)
