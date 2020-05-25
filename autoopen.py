# Auto-opens the flask application

from selenium import webdriver
def flaskopen() :
	driver = webdriver.Firefox()
	driver.get("http://127.0.0.1:5000/")
