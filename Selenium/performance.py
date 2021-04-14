# -*- coding: utf-8 -*-
import time,json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/Users/caicloud/Desktop/chromedriver')

def Page_Test(Urllist):

	driver.get(Urllist[0])

	navigationStart_time = driver.execute_script("return window.performance.timing.navigationStart")
	loadEventEnd_time = driver.execute_script("return window.performance.timing.loadEventEnd")
	loadtime = loadEventEnd_time - navigationStart_time

	print(loadtime)
	
	driver.get(Urllist[1])

	navigationStart_time = driver.execute_script("return window.performance.timing.navigationStart")
	loadEventEnd_time = driver.execute_script("return window.performance.timing.loadEventEnd")
	loadtime = loadEventEnd_time - navigationStart_time

	print(loadtime)

def Set_Cookies():

	driver.get("http://192.168.129.30:6060")
	#driver.delete_all_cookies()

	with open('cookies.json', 'r') as f:
		listCookies = json.loads(f.read())

	for cookie_ in listCookies:
		driver.add_cookies({
			'domain': '.192.168.129.30',
			'name': cookie_['name'],
			'value': cookie_['value'],
			'path': '/',
			'expires': None
			})

def Get_Cookies():

    driver.get("http://192.168.129.30:6060")

    username = driver.find_element_by_id("login_username")
    password = driver.find_element_by_id("login_password")
    username.send_keys('admin')
    password.send_keys('Pwd123456')
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    try:
        Waitelement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "web-lib-tenant-back"))
            )
        dictCookies = driver.get_cookies()
        jsonCookies = json.dumps(dictCookies)
        with open('cookies.json', 'w') as f:
            f.write(jsonCookies)

    except:
        print('获取Cookie失败，请重新获取')


if __name__ == '__main__':
	env = ["http://192.168.129.30:6060/chooseTenant","http://192.168.129.30:6060/overview?cid=compass-stack"]
	Get_Cookies()
	time.sleep(1)
	Page_Test(env)
