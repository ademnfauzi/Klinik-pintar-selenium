from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from global_function import *
from fpdf import FPDF
import time


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
        driver.find_element(switch_case("id"), "headlessui-disclosure-button-3").click()

def switch_sub_menu(menu, saveWord, saveImage):
    if menu == "SEMUA STATUS":
        driver.find_element(switch_case("id"), "rawat-jalan_semua-status_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Semua Status")
    elif menu == "RESERVASI":
        driver.find_element(switch_case("id"), "rawat-jalan_reservasi_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Reservasi")
    elif menu == "REGISTRASI":
        driver.find_element(switch_case("id"), "rawat-jalan_registrasi_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Registrasi")
    elif menu == "RESUME":
        driver.find_element(switch_case("id"), "rekam-medis_resume_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Resume")
    elif menu == "RUJUKAN LABORATORIUM":
        driver.find_element(switch_case("id"), "rekam-medis_rujukan-laboratorium_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Rujukan Laboratorium")
    elif menu == "PEMERIKSAAN":
        driver.find_element(switch_case("id"), "rekam-medis_pemeriksaan_menu_click").click()
        wait(5)
        call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Pemeriksaan")


def Filter_Type_Payment(Payment=None, surety=None):
    driver.find_element(switch_case("id"), "btn_payment_filter").click()
    wait(1)
    Obj = driver.find_element(switch_case("id"), "btn_payment_filter")
    Obj.send_keys(Keys.TAB)
    Obj = driver.find_element(switch_case("id"), "dd_payment_type")
    wait(5)
    if Payment == True:
        if Payment == "Pribadi":
            print("pribadi")
            wait(5)
            Obj.send_keys(Keys.DOWN)
            wait(5)
            Obj.send_keys(Keys.ENTER)
        elif Payment == "Penjamin":
            print("penjamin")
            wait(5)
            Obj.send_keys(Keys.DOWN)
            wait(5)
            Obj.send_keys(Keys.DOWN)
            wait(5)
            Obj.send_keys(Keys.ENTER)
            wait(5)       
            #Obj.send_keys(Keys.TAB)
            wait(5)
            Obj = driver.find_element(switch_case("id"), "dd_guarantor_option")
            Obj.send_keys(surety)
            wait(5)
            Obj.send_keys(Keys.ENTER)


        driver.find_element(switch_case("id"), "btn_apply_filter").click()
    else:
        driver.find_element(switch_case("id"), "btn_reset_filter").click()
            
    
    wait(5)

def Filter_Polyclinic_Doctor(Polyclinic=None,Doctor=None):
    if Polyclinic:
        Obj = driver.find_elements(switch_case("xpath"), "//input[@class='w-full absolute inset-0 outline-none focus:ring-0 appearance-none box-border border-0 text-sm bg-white rounded pl-3.5']")
        Obj2 = Obj[0]
        Obj2.send_keys(Polyclinic)
        wait(3)
        Obj2.send_keys(Keys.ENTER)
    
    if Doctor:
        Obj = driver.find_elements(switch_case("xpath"), "//input[@class='w-full absolute inset-0 outline-none focus:ring-0 appearance-none box-border border-0 text-sm bg-white rounded pl-3.5']")
        Obj2 = Obj[1]
        Obj2.send_keys(Doctor)
        wait(3)
        Obj2.send_keys(Keys.ENTER)

def logout():
    driver.find_element(switch_case("xpath"), "//button[@class='flex items-center rounded-full text-gray-400 hover:text-gray-600 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2 focus:ring-offset-gray-100']").click()
    wait(1)
    driver.find_element(switch_case("xpath"), "//a[@href='/logout']").click()
    wait(15)
         