from function_klinik import *

url = "https://os.staging.klinikpintar.id/login"
username = "kprendy"
password = "123456"

driver = open_browser(url)

login = form_login(username,password)