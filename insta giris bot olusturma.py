from instabilgi import kullaniciadi,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options=Options()
options.add_experimental_option("excludeSwitches",["enable-logging"])


driver=webdriver.Chrome(executable_path=r"C:/Users/yesim/OneDrive/Masaüstü/chromedriver.exe",chrome_options=options)
url="https://www.instagram.com/accounts/login/?hl=tr"
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(4)
ka=driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
ka.send_keys(kullaniciadi)

sif=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
sif.send_keys(sifre)
sif.send_keys(Keys.ENTER)
time.sleep(3)







