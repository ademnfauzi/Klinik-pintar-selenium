from function_klinik import *
from global_function import *
from selenium.webdriver.common.keys import Keys

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
switch_menu("REKAM MEDIS")
wait(5)
switch_sub_menu("RESUME", saveWord, saveImage)
wait(5)
Obj = driver.find_element(switch_case("id"), "rekam-medis_resume_semua_tab_click").click()
wait(5)
call_screenshoot(saveWord,saveImage,"Menampilkan Semua Data Resume")


end(saveImage,saveWord,'KP0018-TCSN001')