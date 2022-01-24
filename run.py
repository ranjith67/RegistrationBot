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

    bot.get('https://www.king567.com/invite/500b550174b169a1ae19ef7b57f6b0c0d8bd3830')

    #number addimng
    time.sleep(1)

    firstname_field = bot.find_element_by_xpath('//*[@id="user_first_name"]')
    firstname_field.send_keys(data["firstname"])

    time.sleep(0.5)

    lastname_field = bot.find_element_by_xpath('//*[@id="user_last_name"]')
    lastname_field.send_keys(data["lastname"])

    time.sleep(0.5)

    username_field = bot.find_element_by_xpath('//*[@id="user_username"]')
    username_field.send_keys(data["username"])

    time.sleep(0.5)

    email_field = bot.find_element_by_xpath('//*[@id="user_email"]')
    email_field.send_keys(data["email"])

    time.sleep(0.5)

    password_field = bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/form/div[2]/div[6]/div/input')
    password_field.send_keys(data["password"])

    time.sleep(0.5)

    conpassword_field = bot.find_element_by_xpath('//*[@id="user_password_confirmation"]')
    conpassword_field.send_keys(data["conpassword"])

    time.sleep(0.5)

    number_field = bot.find_element_by_xpath('//*[@id="user_phone_number"]')
    number_field.send_keys(data["number"])

    time.sleep(0.5)

    city_field = bot.find_element_by_xpath('//*[@id="user_city"]')
    city_field.send_keys('Mangalore')

    time.sleep(0.5)

    country_field = bot.find_element_by_xpath('//*[@id="user_country"]')
    country_field.send_keys('India')

    time.sleep(0.5)

    zipcode_field = bot.find_element_by_xpath('//*[@id="user_zipcode"]')
    zipcode_field.send_keys('576117')

    time.sleep(0.5)

    bot.find_element_by_xpath('//*[@id="sign_up"]/div[2]/label/span[1]').click()

    time.sleep(0.5)

    bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/form/div[3]/input').click()

    time.sleep(1)


for data in datas:
    main(data)  