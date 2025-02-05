from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

name_input = driver.find_element(By.NAME, "fName")
lname_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
btn = driver.find_element(By.TAG_NAME, "button")

name_input.send_keys("<NAME>")
lname_input.send_keys("<lastname>")
email_input.send_keys("example@text.com")
btn.click()


