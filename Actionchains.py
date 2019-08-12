'''
Created on Jul 14, 2019

@author: Kevin Steven Moreno
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Using firefox
driver = webdriver.Firefox()
driver.get('http://demo.guru99.com/test/drag_drop.html')

#To run test need full size window
driver.maximize_window()

#Bank button dragged to Debit Account
bank_button = driver.find_element_by_id('credit2')
debit_account = driver.find_element_by_id('bank')
ActionChains(driver).drag_and_drop(bank_button, debit_account).perform()

#Sales button dragged to Credit Account
sales_button = driver.find_element_by_id('credit1')
credit_account = driver.find_element_by_id('loan')
ActionChains(driver).drag_and_drop(sales_button, credit_account).perform()


#5000 amount buttons to Debit and Credit Amounts
button_5000_right = driver.find_element_by_xpath('//*[@id="fourth"][2]')
debit_amount = driver.find_element_by_id('amt7')
ActionChains(driver).drag_and_drop(button_5000_right, debit_amount).perform()
button_5000_left = driver.find_element_by_xpath('//*[@id="fourth"]')
credit_amount = driver.find_element_by_id("amt8")
ActionChains(driver).drag_and_drop(button_5000_left, credit_amount).perform()
