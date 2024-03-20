import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from configparser import ConfigParser
from selenium.webdriver.common.by import By

# helper functions to check if an element exists
def check_exists_by_id(element_id):
    try:
        driver.find_element(By.ID, element_id)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_class(class_name):
    try:
        driver.find_element(By.CLASS_NAME, class_name)
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
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

print("This program will update your WG-Gesucht listings so they will be listed at the top/as new again.")
print("For help, visit the github page or read the README.")

driver.get("https://wg-gesucht.de")

# check if the prompt to accept cookies shows up and
if check_exists_by_id("cmpbntyestxt"):
    btn = driver.find_element(By.ID, "cmpbntyestxt").click()

# access login prompt
driver.find_element(By.XPATH, '//div[@class="dropdown-mini"]/a[contains(text(), "Mein Konto")]').click()
time.sleep(5)

print("Logging in..")

# login with user data from config file
username = driver.find_element(By.NAME, "login_email_username")
password = driver.find_element(By.ID, "login_password")
username.send_keys(config['account']['username'])
password.send_keys(config['account']['password'])
driver.find_element(By.ID, "login_submit").click()
time.sleep(5)

if check_exists_by_class("logout_button"):
    print("Successfully logged in!")

while True:
    # iterate through listings
    for key, url in config.items('listings'):
        print("Currently updating: {}".format(url))
        # open listing in edit mode
        driver.get(url)
        time.sleep(5)

        # hide modal if it shows up
        # $('#hard_ad_limit_modal').modal('show') is invoked by the website to show a modal
        if check_exists_by_id("hard_ad_limit_modal"):
            driver.execute_script("$('#hard_ad_limit_modal').modal('hide');")
        
        time.sleep(5)

        # and finally update the listing
        driver.find_element(By.ID, "update_offer").click()
        time.sleep(5)

    print("Updated at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
    time.sleep(float(config['setup']['interval']))