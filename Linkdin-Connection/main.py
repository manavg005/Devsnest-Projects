import time
import os
from selenium import webdriver
from cred import user,pas
from webdriver_manager.chrome import ChromeDriverManager



# driver = webdriver.Chrome(ChromeDriverManager().install())
# add path for chromedriver.exe
driver = webdriver.Chrome("C:\\Users\\lenovo\\Downloads\\chromedriver_win32\\chromedriver.exe")


# Open Linkedin
driver.get("https://www.linkedin.com/login")

# Find the username & password elements & fill it with the email and password in cred file
driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("password").send_keys(pas)
# Get the submit button and click on it
driver.find_element_by_css_selector(".btn__primary--large").click()

# Open invitations page
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

# ----------------- Get all the available invitation's ACCEPT Button
acceptButtons = []
while len(acceptButtons)==0:
    acceptButtons = driver.find_elements_by_xpath("//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")

# Accept connections by clicking the buttons
for button in acceptButtons:
    button.click()
    time.sleep(5)