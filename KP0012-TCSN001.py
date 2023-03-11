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
switch_menu("RAWAT JALAN")
wait(5)
switch_sub_menu("REGISTRASI", saveWord, saveImage)


end(saveImage,saveWord,'KP0012-TCSN001')