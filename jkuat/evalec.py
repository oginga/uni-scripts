import argparse
from selenium import webdriver
from bs4 import BeautifulSoup
from jsonParser import load_json
from pyvirtualdisplay import Display
import re
username=''
password=''
yos=None
gender=''
program=None
programmes={"Certificate":3,"Diploma":4,"Postgraduate_Diploma":5,"Bachelors":6,"Masters":7,"Phd":8}
driver=None


def login():
#create a new firefox session



	global driver
	#Headless browsing

	#display=Display(visible=0,size=(800,600))
	#display.start()
	
	driver=webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.maximize_window()

#navigate to portal page
	driver.get("http://portal.jkuat.ac.ke/")

#interact with portal's login form
	driver.find_element_by_name('LoginForm[username]').send_keys(username)
	driver.find_element_by_name('LoginForm[password]').send_keys(password)
	driver.find_element_by_name('yt0').click()

#click onto your Evaluation link
#<li><a href='/Api/evaluation'>Evaluation</a></li>
	driver.find_element_by_link_text('Evaluation').click()

def evaluate():
	'''evaluation tings'''
	global driver
	#driver.find_element_by_link_text('Evaluation').click()

	soup=BeautifulSoup(driver.page_source)
	eval_link=soup.find('a',attrs={'href':re.compile("^http://evaluation.jkuat.ac.ke/student/evaluate/start")})
	href=eval_link.get('href')
	driver.find_element_by_xpath('//a[@href="'+href+'"]').click()

	
	act_data=load_json()

	units=act_data['units']

	for unit_code,details in units.items():

		#course details
		driver.find_element_by_name('unit').send_keys(unit_code)
		driver.find_element_by_name('lecture').send_keys(units[unit_code]['lecturer'])
		driver.find_element_by_name('lecture').submit()

		#sleep
		#School/Faculty
		driver.find_element_by_name('answer[1]').send_keys(act_data['faculty'])

		#Department
		driver.find_element_by_name('answer[2]').send_keys(act_data['department'])

		#Gender
		if gender:
			driver.find_element_by_xpath("//input[@value='1']").click()
		else:driver.find_element_by_xpath("//input[@value='2']").click()
		#driver.assertTrue(gendeRadio.is_selected())

		#Year of study
		driver.find_element_by_name('answer[4]').send_keys(str(yos))

		#improvements to course
		driver.find_element_by_name('answer[18]').send_keys("None")

		#first class week
		driver.find_element_by_name('answer[6]').send_keys("Week "+str(units[unit_code]['week']))

		#Programme
		programmeRadio=driver.find_element_by_xpath("//input[@value='"+str(program)+"']").click()

		radios={}
		week=None
		radios=units[unit_code]['radios']
		week=units[unit_code]['week']
		print '\n\n\n'
		

		radio_tings(radios)

		#submit
		driver.find_element_by_name('answer[4]').submit()
	driver.save_screenshot('confirmation.png')

		
	

def query_details():
	global username
	global password
	global yos
	global gender
	global program
	raw_gender=''

	while True:
		try:
			username=raw_input('Enter a valid username i.e john.doe@students : \n')
			#match user name against a compiled regular expression
			password=raw_input('Enter your password i.eab123-1234/2013 if password not changed : \n')
			confirm_pass=raw_input('Confirm password : \n')
		except EOFError:
			break
		else:
			if password == confirm_pass:
				break
			else:print 'Password MISMATCH \n Re-enter your credentials \n'

	try:
		raw_gender=raw_input('Input your GENDER.Type 1 for male or 2 for female: \n')
		prog="Enter the digits to choose your programme: "
		progSTr=' '.join(["%s ->%s"%(v,k) for k,v in programmes.items()])
		progI_P=raw_input(prog+progSTr+" \n")
		for k,v in programmes.items():
			if v== int(progI_P):
				program=v
		yos=raw_input('Enter your year of study ie : \n')
	except EOFError:
		pass

	#casting string to integer
	g=lambda rg:True if rg == '1' else False
	gender=g(raw_gender)
	print gender
	print type(gender)
	#yos=raw_input('Enter year of study')
	


def radio_tings(radios):
	radio_objects={}
	global driver
	for k,v in  radios.items():
		if v ==True:
			driver.find_element_by_xpath("//input[@value='"+ k.split('_')[1]+"']").click()
		else:driver.find_element_by_xpath("//input[@value='"+ k.split('_')[2]+"']").click()
		
	return True	


if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('-u','--user',help='Enter a valid username i.e john.doe@students',dest='username')
	parser.add_argument('-p','--passwd',help='Enter your password i.eab123-1234/2013',dest='password')
	args=parser.parse_args()

	username=args.username
	password=args.password

	query_details()
	login()
	evaluate()
	#eof 1146



#http://evaluation.jkuat.ac.ke/student/evaluate/answer