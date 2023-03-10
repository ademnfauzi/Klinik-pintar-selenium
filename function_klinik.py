from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up the Chrome webdriver
driver = webdriver.Chrome()

def wait(waktu):
    time.sleep(waktu)

def open_browser(url):    
    #maximize the window size 
    driver.maximize_window()
    
    driver.get(url)

    driver.implicitly_wait(10)
    return driver

def form_login(inputUsername, inputPassword):
    username = driver.find_element(By.ID,"username")
    username.send_keys(inputUsername)

    password = driver.find_element(By.ID,"password")
    password.send_keys(inputPassword)

    button_login = driver.find_element(By.ID,"login_btn_click").click()

    time.sleep(10)

    try:
        driver.find_element(By.PARTIAL_LINK_TEXT,"Dashboard").is_displayed()
        print("Berhasil Login")
        time.sleep(5)
    except:
        pass
        driver.execute_script("alert('Gagal Melakukan Login')")
        alert = driver.switch_to.alert
        time.sleep(5)
        alert.accept()
        time.sleep(5)
        print("Gagal Login") 
        driver.quit()

def switch_case(element_type):
    switcher = {
        "id": By.ID,
        "name": By.NAME,
        "class": By.CLASS_NAME,
        "tag": By.TAG_NAME,
        "link": By.LINK_TEXT,
        "partial link": By.PARTIAL_LINK_TEXT,
        "css": By.CSS_SELECTOR,
        "xpath": By.XPATH
    }
    return switcher.get(element_type.lower(), None)
