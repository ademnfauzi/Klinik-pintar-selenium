from function_klinik import *
from global_function import *

url = "https://os.staging.klinikpintar.id/login"
username = "kprendy"
password = "123456"
saveImage = []
saveWord = []

driver = open_browser(url)
call_screenshoot(saveWord,saveImage,"Membuka Halaman Form Login")
login = form_login(username,password,saveWord,saveImage)

end(saveImage,saveWord,'KP0001-TCSN001')