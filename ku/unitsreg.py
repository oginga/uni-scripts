#! /usr/bin/env python

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import codecs

driver=webdriver.Firefox()
#driver=webdriver.PhantomJS('./phantomjs')
driver.get("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwiNqsKDse_KAhXDrxoKHQnpAzgQFggdMAA&url=https%3A%2F%2Fportal.ku.ac.ke%2Fsecure%2Fstudent%2Fstudent.aspx&usg=AFQjCNFoQwE9mOBEDxkyt4S-rBRPGF7QTg&cad=rja")
#driver.maximize_window()
if EC.alert_is_present:
    print "Alert Exists"
    driver.switch_to_alert().dismiss()
    print "Alert Dismissed"
else:
    print "No alert exists"

#login
driver.find_element_by_id('_ctl0_PlaceHolderMain_Loginstu1_txtLoginUsername').send_keys("username")
#elem = driver.find_element_by_xpath("//*")
#source_code = elem.get_attribute("outerHTML")

driver.find_element_by_id('_ctl0_PlaceHolderMain_Loginstu1_txtLoginPassword').send_keys("passwd")
driver.find_element_by_id('_ctl0_PlaceHolderMain_Loginstu1_btnLoginLogin').click()	



if EC.alert_is_present:
    print "Alert Exists"
    driver.switch_to_alert().dismiss()
    print "Alert Dismissed"
else:
    print "No alert exists"

#driver.find_element_by_id()
if driver.find_element_by_id('Academics'):
	driver.find_element_by_id('Academics').click()
	driver.find_element_by_link_text('Online Registration').click()
	
	driver.find_element_by_id('_ctl0_PlaceHolderMain_lnkAvailablesubhead').click()


	# wait to make sure there are two windows open
	if WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2):
		print 'Windows =2'
		# switch windows

		if driver.switch_to_window(driver.window_handles[1]):
			print 'switched to window 1'
			url = driver.execute_script("return window.location;")
			print url


	# wait to make sure the new window is loaded
			WebDriverWait(driver, 10).until(lambda d: d.title != "")

			soup=BeautifulSoup(driver.page_source)
			print soup

	register()


	print 'id found'


else:
	print 'class NOT found'

def register():

	driver.find_element_by_id('txtQuickAddCourseCode').send_keys("THAT")
	driver.find_element_by_id('txtQuickAddSection').send_keys("")


#driver.find_element_by_link_text('Online Registration').click()



#soup=BeautifulSoup(driver.page_source)







