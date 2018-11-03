from selenium import webdriver
from config import keys
import time

def order(k):
	driver = webdriver.Chrome('./chromedriver')

	driver.get(k['product_url'])

# BYPASSS NEEDED
	driver.find_element_by_xpath('//*[@id="container"]/article[6]/div').click()

	time.sleep(1)

	# size
	driver.find_element_by_xpath('//*[@id="s"]/option[1]').click()

	# add to card
	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

	time.sleep(1)

	# checkout now
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

	# name - billing
	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])

	# email - billing
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])

	# tel - billing
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["tel"])

	# address - billing
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])

	# zip - billing
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])

	# card number - billing
	driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(k["card"])

	# year card
	driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()

	# CVV
	driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])

	# agree
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

	# month card
	driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[11]').click()


	
	

if __name__ == '__main__':
	order(keys)