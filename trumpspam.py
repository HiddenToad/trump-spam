print("configuring selenium and launching geckodriver, please wait a moment...\n")
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import random as rand
import string
import time

alphabet = string.ascii_lowercase

def randstr(a, b):
    return ''.join(rand.choice(alphabet) for i in range(rand.randint(a, b)))

pref = webdriver.FirefoxOptions()

pref.set_preference("browser.link.open_newwindow", 1)
pref.add_argument('--headless')
pref.add_argument('--disable-gpu')
driver = webdriver.Firefox(options=pref)
del pref

try:
    print("done!\nrunning script...\n")
    for i in range(100_000):
        driver.get("http://truthsocial.com")

        first_name = randstr(4,8)
        last_name = randstr(4,8)
        email = (randstr(5,10) + rand.choice(["@gmail.com", "@icloud.com", "@me.com", "@hotmail.com", "@yahoo.com", "@hotmail.net", "@outlook.com"]))

        driver.find_element(By.ID, "first_name").send_keys(first_name)
        driver.find_element(By.ID, "Last_name").send_keys(last_name)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "offers").click()
        driver.find_element(By.CLASS_NAME, "space-y-6").submit()

        print(f"falsly registered with name {first_name} {last_name} and email {email}")

except:
    print("interrupted. safely aborting program, please do not interrupt again...")
    driver.quit()
    print("program aborted.")
    sys.exit(0)

driver.quit()
