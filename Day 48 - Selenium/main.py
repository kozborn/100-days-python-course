from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

events_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li")
events = {}
for index, event in enumerate(events_list):
    time = event.find_element(By.TAG_NAME, "time")
    name = event.find_element(By.TAG_NAME, "a")
    events[index] = { "time": time.text, "name": name.text}

print(events)

driver.quit()




