from function_klinik import *
from PIL import Image
url = "https://os.staging.klinikpintar.id/login"
username = "kprendy"
password = "123456"

driver = open_browser(url)

login = form_login(username,password)
wait(10)
driver.find_element(switch_case("id"), "headlessui-disclosure-button-1").click()
wait(10)
driver.find_element(switch_case("id"), "rawat-jalan_semua-status_menu_click").click()
wait(10)