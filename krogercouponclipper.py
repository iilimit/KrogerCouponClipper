from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import creds
import platform


platform = platform.system()
service = None
options = Options()
if(platform == 'Darwin'):
    service = Service(
    executable_path="macOS/chromedriver")
elif (platform == 'Windows'):
    service = Service(executable_path="windows/chromedriver.exe")

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
    password_box.click()
    time.sleep(2)
    password_box.clear()
    time.sleep(2)
    password_box.send_keys(creds.password)

    remember_me_box = driver.find_element(By.ID, 'SignIn-rememberMe')
    time.sleep(2)
    if(remember_me_box.is_selected() == False):
        remember_me_box.click()
    driver.find_element(By.ID, 'SignIn-submitButton').click()

time.sleep(5)

#ALL COUPONS BTN
driver.find_element(By.XPATH, "//button[starts-with(@id, 'Tabs-tab-')]").click()


# Keeps scrolling until all items are loaded
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page / use a better technique like `waitforpageload` etc., if possible
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#Number of coupons
coupon_value_str = driver.find_element(By.XPATH, '//*[@id="content"]/section/div/section[2]/section/section/div/div[2]/div[2]/span').text
amount_of_coupons = [int(x) for x in coupon_value_str.split() if x.isdigit()] 

#clicks 'clip' buttons
for j in range(1,int(amount_of_coupons[0])):
    time.sleep(0.2)
    driver.find_element(By.XPATH,f'//*[@id="content"]/section/div/section[2]/section/section/div/div[2]/div[2]/div/div/div/ul/li[{j}]/div/div/div/div[2]/div[3]/button[2]')