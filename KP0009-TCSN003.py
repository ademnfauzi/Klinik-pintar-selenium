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
switch_menu("RAWAT JALAN")
wait(5)
switch_sub_menu("RESERVASI", saveWord, saveImage)
wait(5)
driver.find_element(switch_case("id"), "rawat-jalan_reservasi_dibatalkan_tab_click").click()
wait(5)
call_screenshoot(saveWord,saveImage,"Menampilkan Semua Data Dibatalkan Untuk Reservasi")

end(saveImage,saveWord,'KP0009-TCSN003')