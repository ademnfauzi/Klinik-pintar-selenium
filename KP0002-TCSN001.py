from function_klinik import *
from global_function import *

saveImage = []
saveWord = []
url = "https://os.staging.klinikpintar.id/login"
username = "kprendy"
password = "123456"

driver = open_browser(url)
call_screenshoot(saveWord,saveImage,"Membuka Halaman Form Login")
wait(5)
login = form_login(username,password,saveWord,saveImage)
wait(5)
driver.find_element(switch_case("id"), "headlessui-disclosure-button-1").click()
wait(5)
driver.find_element(switch_case("id"), "rawat-jalan_semua-status_menu_click").click()
wait(10)
call_screenshoot(saveWord,saveImage,"Membuka Sub Menu Semua Status")


end(saveImage,saveWord,'KP0002-TCSN001')