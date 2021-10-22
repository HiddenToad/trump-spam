from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random as rand


pref = webdriver.FirefoxOptions()
alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
def randstr(a, b):
    temp = ""
    for i in range(rand.randint(a,b)):
        temp += rand.choice(alphabet)
    return temp

pref.set_preference("browser.link.open_newwindow", 1)
pref.add_argument('--headless')
driver = webdriver.Firefox(options=pref)
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
    print("falsly registered with name " + first_name + " " + last_name + " and email " + email)
