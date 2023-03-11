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
switch_sub_menu("SEMUA STATUS", saveWord, saveImage)
wait(5)
Filter_Type_Payment()
call_screenshoot(saveWord,saveImage,"Menampilkan Hasil Filter Tipe Pembayaran")

end(saveImage,saveWord,'KP0003-TCSN002')