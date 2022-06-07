from selenium import webdriver
#selenium uzerinden eristigimiz herhangi bir siteden klavyeyle islem yapmak istiyossak ayri bi modul cekmeliyiz
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


options=Options()
options.add_experimental_option("excludeSwitches",["enable-logging"])


drive=webdriver.Chrome(executable_path=r"C:/Users/yesim/OneDrive/Masaüstü/chromedriver.exe",chrome_options=options)
url="https://careers.microsoft.com/students/us/en/"
drive.get(url)
time.sleep(2)
drive.maximize_window()
time.sleep(2)




isara=drive.find_element_by_css_selector("#searchBox")
isara.click()
time.sleep(2)
isara.send_keys("Engineering")
isara.send_keys(Keys.ENTER)
