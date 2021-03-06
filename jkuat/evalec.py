import argparse
from selenium import webdriver
from bs4 import BeautifulSoup
from jsonParser import load_json
#from pyvirtualdisplay import Display
import colorama
import re

CYAN=colorama.Fore.CYAN
RESET=colorama.Style.RESET_ALL
WARN=colorama.Fore.RED
GREEN=colorama.Fore.GREEN
MAGENTA=colorama.Fore.MAGENTA
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
		driver.implicitly_wait(3)	
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

		radio_tings(radios)

		#submit
		driver.find_element_by_name('answer[4]').submit()
		print CYAN+"\t\t%s\t"%(unit_code.upper())+"evaluated successfully \n"+RESET
		driver.implicitly_wait(5)
	if driver.save_screenshot('confirmation.png'):
		print MAGENTA+"Check for a screenshot of youe evaluation status in the current dir"+RESET
	driver..close()

		
	

def query_details():
	global username
	global password
	global yos
	global gender
	global program
	raw_gender=''

	while True:
		try:
			username=raw_input(CYAN+'Enter a valid username i.e john.doe@students :'+RESET+'\n')
			#match user name against a compiled regular expression
			password=raw_input(CYAN+'Enter your password i.eab123-1234/2013 if password not changed : '+RESET+'\n')
			confirm_pass=raw_input(CYAN+'Confirm password : '+RESET+'\n')
		except EOFError:
			break
		else:
			if password == confirm_pass:
				break
			else:print WARN+'\t\t\tPassword MISMATCH \n Re-enter your credentials '+RESET+'\n'

	try:
		raw_gender=raw_input(CYAN+'Input your GENDER.Type 1 for male or 2 for female:'+RESET+'\n')
		prog="Enter the digit(from above) for your programme: "
		print MAGENTA+'\t\t\tPROGRAMMES\t\t\t'+RESET
		for k,v in programmes.items():
			print GREEN+'%s -> %s'%(v,k)+RESET+'\n'
		#progSTr=' '.join(["%s ->%s"%(v,k) for k,v in programmes.items()])
		progI_P=raw_input(CYAN+prog+RESET+" \n")
		for k,v in programmes.items():
			if v== int(progI_P):
				program=v
		yos=raw_input(CYAN+'Enter your year of study ie :'+RESET+'\n')
	except EOFError:
		pass

	#casting string to integer
	g=lambda rg:True if rg == '1' else False
	gender=g(raw_gender)
	print MAGENTA+"\t\t\tLOADING...................\t\t\t"+RESET
	

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

	if username and password:
		#print "if true"
		#login()
		#evaluate()
		pass
	else:
		query_details()
		login()
		evaluate()
	



#http://evaluation.jkuat.ac.ke/student/evaluate/answer
