import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from configparser import ConfigParser


# helper functions to check if an element exists
def check_exists_by_id(element_id):
    try:
        driver.find_element_by_id(element_id)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_class(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True


# read the config file
file = 'config.ini'
config = ConfigParser()
config.read(file)

# create a new chromedriver object
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(config['chromedriver']['path'], options=options)

print("This program will update your WG-Gesucht listings so they will be listed at the top/as new again.")
print("For help, visit the github page or read the README.")

driver.get("https://wg-gesucht.de")

# check if the prompt to accept cookies shows up and
if check_exists_by_id("cmpbntyestxt"):
    btn = driver.find_element_by_id("cmpbntyestxt").click()

# access login prompt
driver.find_element_by_xpath('//*[@id="headbar_wrapper"]/div[2]/a[3]').click()
time.sleep(1)

print("Logging in..")

# login with user data from config file
username = driver.find_element_by_name("login_email_username")
password = driver.find_element_by_id("login_password")
username.send_keys(config['account']['username'])
password.send_keys(config['account']['password'])
driver.find_element_by_id("login_submit").click()
time.sleep(5)

if check_exists_by_class("logout_button"):
    print("Successfully logged in!")

while True:
    # iterate through listings
    for key, url in config.items('listings'):

        if check_exists_by_id("cmpbntyestxt"):
            btn = driver.find_element_by_id("cmpbntyestxt").click()

        print("Currently updating: {}".format(url))
        # open listing
        driver.get(url)
        # open the edit section
        driver.find_element_by_xpath('//*[@id="main_column"]/div[2]/div[2]/a').click()
        time.sleep(3)
        # and finally update the listing
        driver.find_element_by_id("update_offer").click()
        time.sleep(1)

    print("Updated at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
    time.sleep(float(config['setup']['interval']))
