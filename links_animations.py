'''
Created on Jul 17, 2019

@author: Kevin Steven Moreno
'''
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://demo.guru99.com/test/yahoo.html')

#To run test need full size window
driver.maximize_window()



#Checking links in 'car_paging' div
its_game = driver.find_element_by_id('pager2').click()
#Time for animation
time.sleep(2)
print("Bursting with Fun link is working.")
driver.back()

burst_fun = driver.find_element_by_id('pager1').click()
#Time for animation
time.sleep(2)
print("It's Game link is working.  ")
driver.back()

its_facebook = driver.find_element_by_id('pager3').click()
#Time for animation
time.sleep(2)
print("Facebook link is working.")
driver.back()

its_social = driver.find_element_by_id('pager4').click()
#Time for animation
time.sleep(2)
print("It's Social link is working.")
driver.back()

its_mobile = driver.find_element_by_id('pager5').click()
#Time for animation
time.sleep(2)
print("Its Mobile link is working.")
driver.back()

its_always_on = driver.find_element_by_id('pager6').click()
#Time for animation
time.sleep(2)
print("It's always on link is working")
driver.back()

its_all_one = driver.find_element_by_id('pager7').click()
#Time for sleep
time.sleep(2)
print("All-in-one link is working")
driver.back()


driver.close()
