from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from global_function import *
from fpdf import FPDF
import time
import os
import secrets
import string
import pyautogui


def form_login(inputUsername, inputPassword,saveWord,saveImage):
    username = driver.find_element(By.ID,"username")
    username.send_keys(inputUsername)

    password = driver.find_element(By.ID,"password")
    password.send_keys(inputPassword)

    button_login = driver.find_element(By.ID,"login_btn_click").click()

    time.sleep(10)

    try:
        driver.find_element(By.PARTIAL_LINK_TEXT,"Dashboard").is_displayed()
        print("Berhasil Login")
        call_screenshoot(saveWord,saveImage,"Berhasil Melakukan Login")
        time.sleep(5)
    except:
        pass
#        driver.execute_script("alert('Gagal Melakukan Login')")
#        alert = driver.switch_to.alert
#        time.sleep(5)
#        alert.accept()
#        time.sleep(5)
        print("Gagal Login") 
        call_screenshoot(saveWord,saveImage,"Gagal Melakukan Login")
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

def switch_menu(menu):
    if menu == "RAWAT JALAN":
        driver.find_element(switch_case("id"), "headlessui-disclosure-button-1").click()
    elif menu == "REKAM MEDIS":
        driver.find_element(switch_case("id"), "headlessui-disclosure-button-17").click()

def switch_sub_menu(menu, saveWord, saveImage):
    if menu == "SEMUA STATUS":
        driver.find_element(switch_case("id"), "rawat-jalan_semua-status_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Semua Status")
    elif menu == "RESERVASI":
        driver.find_element(switch_case("id"), "rawat-jalan_reservasi_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Reservasi")
    