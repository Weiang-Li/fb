from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import pyautogui as gui
import re

# Chrome driver
path = Path('.') / '/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=path, options=options)
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(2)

# email
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
driver.find_element_by_xpath('//*[@id="email"]').send_keys('your email')

# password
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('your password')

# login
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="u_0_b"]')))
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()

time.sleep(10)
gui.click(x=413, y=79, duration=2)
time.sleep(5)

# click find friends
WebDriverWait(driver, 100).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span')))
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span').click()


# search bar
WebDriverWait(driver, 100).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input')))
driver.find_element_by_xpath(
    '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input').click()


pattern = '"__isProfile":"User","name":"(.*?,)'
f = open(r"C:\fb friend.txt")
raw = f.read()
allFriends = re.findall(pattern,raw)
new= []
for friend in allFriends:
    string = str(friend)
    string = string.replace('\n', '')[:-2]
    string =re.sub('[^a-zA-Z ]+', '', string)

newallfriends = new[50:]
# put name in search bar
count = 0
for friend in newallfriends:
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input')))
        driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input').send_keys(friend)
        driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input').send_keys(Keys.ENTER)
        gui.click(x=917, y=233,duration=2)

        try:
            # click on friends
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/a[3]/div[1]/span')))
            driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/a[3]/div[1]/span').click()

            ## start adding friends
            for i in range(1, 35):
                try:
                    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                   f'/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[{i}]/div[3]/div/div/div/div[1]/div/span/span')))

                    driver.find_element_by_xpath(
                        f'/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[{i}]/div[3]/div/div/div/div[1]/div/span/span').click()

                    count = count + 1
                    print(count, ' friend request sent, friend number: ', i)
                    # time.sleep(1.5)
                    try:
                        # click out people you may know
                        WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[12]/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]')))
                        driver.find_element_by_xpath(
                            '/html/body/div[12]/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]').click()
                    except:
                        continue
                except:
                    print('friend number: ', i,' not found')
        except:
            print('This friend can not be found: ', friend,' going to next friend...')
            WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span')))
            driver.find_element_by_xpath(
                '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span').click()

        print('Total Original Friend Used: ',new.index(friend),' ', friend)
    except:
        try:
            WebDriverWait(driver, 100).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span')))
            driver.find_element_by_xpath(
                '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span').click()
        except Exception as e:
            print(e)
            continue

