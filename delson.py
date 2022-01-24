import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM

f = open('accounts.json',)
datas = json.load(f)

def main(data):
    options = webdriver.ChromeOptions()

    mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19" }

    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--log-level=3")

    bot = webdriver.Chrome(options=options, executable_path=CM().install())
    bot.get('https://www.instagram.com/')

    #number addimng
    time.sleep(2)

    username_field = bot.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username_field.send_keys('ni.sar2514')

    time.sleep(1)

    password_field = bot.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_field.send_keys('hiR6789@')

    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

    time.sleep(1)

    bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()

    time.sleep(5)

    bot.close()

for data in datas:
    main(data)  