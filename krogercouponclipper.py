from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import creds

options = Options()
service = Service(executable_path="B:\\Code Projects\\chromedriver.exe")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.kroger.com/savings/cl/mycoupons/")
time.sleep(5)
if(driver.current_url == 'https://www.kroger.com/signin?redirectUrl=/savings/cl/mycoupons/'):
    email_box = driver.find_element(By.ID, 'SignIn-emailInput')
    email_box.click()
    time.sleep(2)
    email_box.clear()
    time.sleep(2)
    email_box.send_keys(creds.email)
    time.sleep(2)
    password_box = driver.find_element(By.ID, 'SignIn-passwordInput')
    password_box.clear()
    password_box.send_keys(creds.password)
    
    remember_me_box = driver.find_element(By.ID, 'SignIn-rememberMe')
    time.sleep(2)
    if(remember_me_box.is_selected() == False):
        remember_me_box.click()
    driver.find_element(By.ID, 'SignIn-submitButton').click()
    # sign_in_button


# Scrolls to bottom of the page to load all coupons
for i  in range(0,6):
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

