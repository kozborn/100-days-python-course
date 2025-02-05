from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv('../.env')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://tinder.com/")
header_links = driver.find_elements(By.CSS_SELECTOR, "header a")

login_link = None

for link in header_links:
    if "https://tinder.onelink.me" in link.get_attribute("href"):
        login_link = link

if login_link is not None:
    login_link.click()
    time.sleep(2)
    iframe = driver.find_element(By.TAG_NAME, "iframe")

    # print(driver.find_element(By.CSS_SELECTOR, value="#container > div[role='button']"))
    driver.switch_to.frame(iframe)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, value="#container > div[role='button']").click()
    time.sleep(2)

    google_login_window = driver.window_handles[1]
    driver.switch_to.window(google_login_window)
    input_email = driver.find_element(By.CSS_SELECTOR, "input[type=email]")
    input_email.send_keys(os.getenv("FAKE_EMAIL_FOR_TINDER"))
    driver.maximize_window()
    time.sleep(1)
    next_button = driver.find_elements(By.CSS_SELECTOR, "button[type=button]")
    next_button[1].click()

    # input_email = driver.find_element(By.CSS_SELECTOR, "input[type=email]")
    # input_email.send_keys(os.getenv("FAKE_EMAIL_FOR_TINDER"))
    # driver.maximize_window()
    # time.sleep(1)
    # next_button = driver.find_element(By.CSS_SELECTOR, "button[type=button]")
    # next_button.click()
    #
    # input_name = driver.find_element(By.CSS_SELECTOR, "input[name=firstName]")
    # input_name.send_keys("Piotrek")
    # next_button = driver.find_element(By.CSS_SELECTOR, "button[type=button]")
    # next_button.click()
    # body = driver.find_element(By.TAG_NAME, "body")
    # body.send_keys(Keys.TAB)
    # body.send_keys(Keys.RETURN)

    input_password = driver.find_element(By.CSS_SELECTOR, "input[type=password]")
    input_password.send_keys(os.getenv("FAKE_PASSWORD_FOR_TINDER"))
    next_button = driver.find_element(By.CSS_SELECTOR, "button[type=button]")
    next_button.click()

# driver.switch_to.default_content()
# driver.quit()



