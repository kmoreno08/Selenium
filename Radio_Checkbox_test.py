'''
Created on Jul 13, 2019

@author: Kevin Steven Moreno
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://demo.guru99.com/test/radio.html')

radio1 = driver.find_element_by_id('vfb-7-1')
radio2 = driver.find_element_by_id('vfb-7-2')
radio3 = driver.find_element_by_id('vfb-7-3')
checkbox1 = driver.find_element_by_id('vfb-6-0')
checkbox2 = driver.find_element_by_id('vfb-6-1')
checkbox3 = driver.find_element_by_id('vfb-6-2')

#Clicking radio buttons
radio1.click()
if radio1.is_selected():
    print("Radio 1 is toggled on.")
else:
    print("Radio 1 is toggled off.")
    
radio2.click()
if radio2.is_selected():
    print("Radio 2 is toggled on.")
else:
    print("Radio 2 is toggled off.")
    
radio3.click()
if radio3.is_selected():
    print("Radio 3 is toggled on.")
else:
    print("Radio 3 is toggled off.")

#Click all Check boxes 
checkbox1.click()
if checkbox1.is_selected():
    print("Checkbox 1 is toggled on.")
else:
    print("Checkbox 1 is toggled off.")
    
checkbox2.click()
if checkbox2.is_selected():
    print("Checkbox 2 is toggled on.")
else:
    print("Checkbox 2 is toggled off.")
    
checkbox3.click()
if checkbox3.is_selected():
    print("Checkbox 3 is toggled on.")
else:
    print("Checkbox 3 is toggled off.")
    
print("Everything has been completed")
driver.close()

