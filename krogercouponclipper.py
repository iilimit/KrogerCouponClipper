from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, init
import time
import creds
import platform

#start up commands
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
wait = WebDriverWait(driver, 10)
driver.get("https://www.kroger.com/savings/cl/mycoupons/")
time.sleep(5)

#logins to account if not already
if(driver.current_url == 'https://www.kroger.com/signin?redirectUrl=/savings/cl/mycoupons/'):
    email_box = driver.find_element(By.ID, 'SignIn-emailInput')
    email_box.click()
    time.sleep(2)
    email_box.send_keys(Keys.chord(Keys.CONTROL,"a", Keys.DELETE))
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

#Clicks ALL COUPONS button
# time.sleep(3)
try:
    all_coupons_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@id, 'Tabs-tab-')]")))
    all_coupons_tab.click()
    time.sleep(3)
except NoSuchElementException:
    print("Element cannot be found")

#gets elements
search_bar = driver.find_element(By.XPATH, '//*[@id="content"]/section/div/section[2]/section/section/div/div[1]/div/div[2]/div[1]/div/input')
coupon_value_str = driver.find_element(By.XPATH, '//*[@id="content"]/section/div/section[2]/section/section/div/div[2]/div[2]/span').text
amount_of_coupons = [int(x) for x in coupon_value_str.split() if x.isdigit()] 

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

#scrolls back to top of page
driver.execute_script("arguments[0].scrollIntoView();", search_bar)
time.sleep(3)

# clicks 'clip' buttons
for j in range(1,int(amount_of_coupons[0])):
    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH,f'//*[@id="content"]/section/div/section[2]/section/section/div/div[2]/div[2]/div/div/div/ul/li[{j}]/div/div/div/div[2]/div[3]/button[2]').click()
        max_coupon_label = driver.find_element(By.XPATH, f'//*[@id="content"]/section/div/section[2]/section/section/div/div[2]/div[2]/div/div/div/ul/li[{j}]/div/div/div/div[2]/div[2]/span')
        if(max_coupon_label.is_displayed()):
            print(Fore.GREEN + 'The max clipped coupons has been reached')        
            break
    except NoSuchElementException:
        continue


    