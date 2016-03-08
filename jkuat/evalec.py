import argparse
from selenium import webdriver
from bs4 import BeautifulSoup
username=''
password=''
year=None
gender=''
driver=None


def login():
#create a new firefox session
	global driver
	driver=webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.maximize_window()

#navigate to portal page
	driver.get("http://portal.jkuat.ac.ke/")

#interact with portal's login form
#driver.find_element_by_id('login-form') 

	driver.find_element_by_name('LoginForm[username]').send_keys(username)
	driver.find_element_by_name('LoginForm[password]').send_keys(password)
	driver.find_element_by_name('yt0').click()

#click onto your Evaluation link
#<li><a href='/Api/evaluation'>Evaluation</a></li>
	driver.find_element_by_link_text('Evaluation').click()

def evaluate():
	'''evaluation tings'''
	global driver
	driver.find_element_by_link_text('Evaluation').click()

	soup=BeautifulSoup(driver.page_source)
	eval_link=soup.find('a',attrs={'href':re.compile("^http://evaluation.jkuat.ac.ke/student/evaluate/start")})
	href=lnk.get('href')
	driver.find_element_by_xpath('//a[@href="'+href+'"]').click()

	#course details
	driver.find_element_by_name('unit').send_keys('unit code')
	driver.find_element_by_name('lecture').send_keys("lecturer's name")
	driver.find_element_by_name('lecture').submit()

	#evaluation
	#School/Faculty
	driver.find_element_by_name('answer[1]').send_keys("Faculty")

	#Department
	driver.find_element_by_name('answer[2]').send_keys("Department")
	
	#Gender
	#write an if statement to check gender 
	gendeRadio=driver.find_element_by_xpath("//input[@value='1']").click()
	driver.assertTrue(gendeRadio.is_selected())


	#Year of study
	driver.find_element_by_name('answer[4]').send_keys("Year of Study")

	#improvements to course
	driver.find_element_by_name('answer[18]').send_keys("Week 1")


	#Programme
	
'''
	programmeRadio=driver.find_element_by_xpath("//input[@value='6']").click()
	driver.assertTrue(programmeRadio.is_selected())

	#first class week
	driver.find_element_by_name('answer[6]').send_keys("Week 1")

	#course outline val 9 & 10
	attRadio=driver.find_element_by_xpath("//input[@value='9']").click()
	driver.assertTrue(attRadio.is_selected())


	#lec attendance val 11 & 12
	programmeRadio=driver.find_element_by_xpath("//input[@value='6']").click()
	driver.assertTrue(programmeRadio.is_selected())

	#make ups val 13 & 14
	muRadio=driver.find_element_by_xpath("//input[@value='13']").click()
	driver.assertTrue(muRadio.is_selected())

	#lec punctuality val 15 & 16
	puncRadio=driver.find_element_by_xpath("//input[@value='15']").click()
	driver.assertTrue(puncRadio.is_selected())

	#time per lecture val 17 & 18
	timeRadio=driver.find_element_by_xpath("//input[@value='17']").click()
	driver.assertTrue(timeRadio.is_selected())

	#lec communication val 19 & 20
	commRadio=driver.find_element_by_xpath("//input[@value='19']").click()
	driver.assertTrue(commRadio.is_selected())

	#consulation val 21 & 22
	consRadio=driver.find_element_by_xpath("//input[@value='21']").click()
	driver.assertTrue(consRadio.is_selected())

	#CAT provision val 23 & 24
	catRadio=driver.find_element_by_xpath("//input[@value='23']").click()
	driver.assertTrue(catRadio.is_selected())

	#CAT results val 25 & 26
	catresRadio=driver.find_element_by_xpath("//input[@value='25']").click()
	driver.assertTrue(catresRadio.is_selected())

	#Assignment val 27 & 28
	assgRadio=driver.find_element_by_xpath("//input[@value='27']").click()
	driver.assertTrue(assgRadio.is_selected())

	#Group Work val 29 & 20
	gwRadio=driver.find_element_by_xpath("//input[@value='29']").click()
	driver.assertTrue(gw.is_selected())
'''
	

def query_details():
	global username
	global password
	global year
	global gender

	username=raw_input('Enter a valid username i.e john.doe@students')
	#match user name against a compiled regular expression
	password=raw_input('Enter your password i.eab123-1234/2013 if password not changed')
	confirm_pass=raw_input('Confirm password')
	



def radio_tings(radios):
	radio_objects={}
	global driver
	for k,v in  radios.items():
		radio_objects.[k.split('_')[0]]=lambda:= driver.find_element_by_xpath("//input[@value='"+ k.split('_')[1]+"']").click() if v ==True\
									   else driver.find_element_by_xpath("//input[@value='"+ k.split('_')[1]+"']").click()

	for key,value in radio_objects:
		if driver.assertTrue(value.is_selected()):
			pass

		else: 
			print "Radio %s not selected"%(radio_objects[key])
			return False

	return True	



if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument(help='Enter a valid username i.e john.doe@students',dest='username')
	parser.add_argument(help='Enter your password i.eab123-1234/2013',dest='password')
	args=parser.parse_args()

	username=args.username
	password=args.password
	login()





#http://evaluation.jkuat.ac.ke/student/evaluate/answer