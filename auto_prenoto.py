import schedule
import time
import datetime as dt
from pytz import timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import random as rn


############################ Start INPUTS ############################

first_name = "Victor"
last_name = "Hakim"

sender_email = "hakim.victor@gmail.com"
recipient_email = "hakim.victor@gmail.com"
app_pw = "chxkfhflgwitjycx"
test_email_sending = False
emails_desired = True

send_monday    = True
send_tuesday   = True
send_wednesday = True
send_thursday  = True
send_friday    = True

send_time = "07:0"+str(rn.randint(0,9))
send_timezone = "Europe/Rome"

# Select slot time ordering, in order of preference.
# 1=12:00, 2=12:30, 3=13:00, 4=13:30, 5=14:00
slot_preferences = [3, 1, 2, 4, 5]

############################# End INPUTS #############################


def email_error_msg(error=""):
	try:
		msg = MIMEMultipart()
		msg['From'] = sender_email
		msg['To'] = recipient_email
		msg['Subject'] = "Failure in auto_prenoto.py"
		body = "An error has occured in running auto_prenoto.py. Check Terminal."
		msg.attach(MIMEText(body, 'plain'))
		smtp_server = 'smtp.gmail.com'
		smtp_port = 587
		with smtplib.SMTP(smtp_server, smtp_port) as server:
		    server.starttls()  # Secure connection
		    server.login(sender_email, app_pw)
		    server.sendmail(sender_email, recipient_email, msg.as_string())
		print("Email message sent on: ", dt.datetime.now())
		print(f"{error}")
	except Exception as err:
		print(f"An error occurred in email sending: {err}")

def job():
	if test_email_sending:
		email_error_msg()
		return
	try:
		driver = webdriver.Chrome()
		driver.get("https://eu.jotform.com/app/213344089067357?utm_source=jotform_pwa")
		time.sleep(20)
		iframe = driver.find_element(By.XPATH, '//*[@id="213342187764358"]/div[2]/iframe')
		driver.switch_to.frame(iframe)
		name1 = driver.find_element(By.NAME, "q25_nameSurname[first]")
		name1.clear()
		name1.send_keys(first_name)
		name2 = driver.find_element(By.NAME, "q25_nameSurname[last]")
		name2.clear()
		name2.send_keys(last_name)
		email = driver.find_element(By.NAME, "q21_email21")
		email.clear()
		email.send_keys(recipient_email)
		driver.find_element(By.ID, "label_input_82_0").click()  # Employee or Guest?
		driver.find_element(By.ID, "label_input_70_0").click()  # Where will you work today?
		driver.find_element(By.ID, "label_input_38_0").click()  # I will be at ARG and ...
		time.sleep(5)
		for ii in slot_preferences:
			driver.find_element(By.XPATH, '/html/body/form/div[2]/ul/li[18]/div/div/div/div/div/div[2]/div[2]/div/div['+str(ii)+']').click()
			time.sleep(1)
			driver.find_element(By.XPATH, '/html/body/form/div[2]/ul/li[25]/div/div[1]/button[2]').click()  # Send Form
			time.sleep(3)
			if not ("Fill your daily certification" in driver.page_source):
				break
			if ii == len(slot_preferences):
				assert False, "Failure: all given time slots were attempted; none were successful..."
		driver.close()
		print("Form was filled correctly on: ", dt.datetime.now())
	except Exception as err:
		if emails_desired:
			email_error_msg(err)


if test_email_sending:
	schedule.every(5).seconds.do(job)
if send_monday:
	schedule.every().monday.at(send_time, timezone(send_timezone)).do(job)
if send_tuesday:
	schedule.every().tuesday.at(send_time, timezone(send_timezone)).do(job)
if send_wednesday:
	schedule.every().wednesday.at(send_time, timezone(send_timezone)).do(job)
if send_thursday:
	schedule.every().thursday.at(send_time, timezone(send_timezone)).do(job)
if send_friday:
	schedule.every().friday.at(send_time, timezone(send_timezone)).do(job)


while True:
    schedule.run_pending()
    time.sleep(1)



