from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time  

driver = webdriver.Chrome('path/chromedriver.exe')

# Set up the Chrome webdriver
driver = webdriver.Chrome()

#maximize the window size 
driver.maximize_window() 

# Navigate to the login page
driver.get("https://os.staging.klinikpintar.id/login")

username = driver.find_element(By.ID, "username")
username.send_keys('kprendy')

password = driver.find_element(By.ID,"password")
password.send_keys("123456")

button_login = driver.find_element(By.ID,"login_btn_click").click()

time.sleep(10)

cek_dashboard = driver.find_element(By.PARTIAL_LINK_TEXT,"Dashboard")

if cek_dashboard:
    print("masuk")
    rawat_jalan_link = driver.find_element(By.ID,"headlessui-disclosure-button-1").click()
    time.sleep(20)
else:
    print("gamasuk")


