
import requests
import selenium
from selenium.webdriver import Keys
import threading

import time


from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def main():

    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists                                     # and if it doesn't exist, download it automatically                                    # then add chromedriver to path

    applyTesla()

def applyTesla():
    driver = webdriver.Chrome()
    teslaEngineer = "https://www.tesla.com/careers/search/?query=Engineer&country=US"
    driver.get(teslaEngineer)
    driver.maximize_window()
    time.sleep(1)

    #/ html / body / div / div / form / div / main / div / div / table / tbody / tr[1] / td[1] / a
   # / html / body / div / div / form / div / main / div / div / table / tbody / tr[2] / td[1] / a
    #/ html / body / div / div / form / div / main / div / div / table / tbody / tr[3] / td[1] / a
    #/ html / body / div / div / form / div / main / div / div / table / tbody / tr[4] / td[1] / a
    #with open('drewWebsite.txt', 'w') as f:
        #f.write(links[0].get_attribute())
    #/ html / body / div / div / form / div / main / div / div / table / tbody / tr[1391] / td[1] / a
    #time.sleep(2)

    #counter for keeping track and not double applying
    counterFile = open("counterFile.csv", "r")
    x = 457
    x = int(counterFile.read())
    print(x)

    counterFile.close()
    delay = 1
    textInput = "1. With only one python class behind me, I wrote this bot today to apply for every engineering roll at Tesla. 2. Being able to learn new skills rapidly and apply them, lately this can be seen in this code I wrote, learning to ride a motorcycle in under a week and putting 1500 miles on it, and all throughout school. I am not the smartest person in the room but I will be the person in the room the longest if I feel like I don't understand something completely. 3. Not shutting down in high stress environments, instead loving the purpose and willing learn everything I can and move on. 4. Positive attitude and communication, instead of accepting defeat of a chance to work at Tesla I am taking this hail-Mary."


    for i in range(1392):
        #try:



        runDisThang(delay, driver, teslaEngineer, textInput, x)
        x= x+1

        #except:

            # time.sleep(3)
            # driver.get(teslaEngineer)
            # time.sleep(2)
            # try:
            #     runDisThang(delay*2, driver, teslaEngineer, textInput, x)
            #     x = x + 1
            # except:
            #     time.sleep(3)
            #     driver.get(teslaEngineer)
            #     time.sleep(2)
            #     try:
            #         runDisThang(delay * 4, driver, teslaEngineer, textInput, x)
            #         x=x+1
            #     except:
            #         time.sleep(3)
            #         driver.get(teslaEngineer)
            #         time.sleep(2)
            #         try:
            #             runDisThang(delay * 8, driver, teslaEngineer, textInput, x)
            #             x=x+1
            #         except:
            #             exit(1)
        counterFile = open("counterFile.csv", "w")
        counterFile.write(str(x))
        counterFile.close()


def runDisThang(delay, driver, teslaEngineer, textInput, x):
    # edit the path for each job to work down the grid
    xPath = "/ html / body / div / div / form / div / main / div / div / table / tbody / tr[" + str(x) + "] / td[1] / a"
    # had problems scrolling at higher values
    for i in range(int(x / 50)):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(delay)
    # this makes sure the job is in view
    job = driver.find_element(By.XPATH, xPath)
    driver.execute_script("arguments[0].scrollIntoView();", job)
    time.sleep(delay)
    job.click()
    # this delay is here to let the website load might be a better function to verify when the buttons are actually ready
    time.sleep(delay)
    # this button was a doozy had to strip the link and then go there directly
    applyButton = driver.find_element(By.XPATH, "//a [@class = 'tds-btn']")
    driver.get(applyButton.get_attribute("href"))
    time.sleep(delay)
    # Personal inforamtion screen
    driver.find_element(By.XPATH, "//input [@name = '/firstName']").send_keys("Andrew")
    driver.find_element(By.XPATH, "//input [@name = '/lastName']").send_keys("Worthley")
    driver.find_element(By.XPATH, "//input [@name = '/phone']").send_keys("(720)369-6133")
    driver.find_element(By.XPATH, "//input [@name = '/email']").send_keys("apworthley@gmail.com")
    driver.find_element(By.XPATH, "//input [@name = '/profileLinks/0/link']").send_keys("https://www.drewworthley.com/")
    driver.find_element(By.XPATH, "//textarea").send_keys(textInput)
    # This Selections Menus are a little tism but need to lines
    phoneDrop = Select(driver.find_element(By.XPATH, "//select [@name = '/phoneType']"))
    phoneDrop.select_by_value('mobile')
    countryDrop = Select(driver.find_element(By.XPATH, "//select [@name = '/country']"))
    countryDrop.select_by_value('US')
    socailDrop = Select(driver.find_element(By.XPATH, "//select [@name = '/profileLinks/0/type']"))
    socailDrop.select_by_value('portfolio')
    driver.find_element(By.XPATH, "//input [@name = '/resume']").send_keys(r"C:\Users\Andrew Worthley\Downloads\Drew_Worthley_Resume.pdf")
    # only will click on buttons that are on screen
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)
    driver.find_element(By.XPATH, "//button[@data-action-type = 'next']").click()
    time.sleep(delay)
    # Second Page
    notice = Select(driver.find_element(By.XPATH, "//select [@name = '/legalNoticePeriod']"))
    notice.select_by_value("immediately")
    driver.find_element(By.XPATH, "//input [@name = '/legalImmigrationSponsorship' and @value = 'no']").click()
    driver.find_element(By.XPATH, "//input [@name = '/legalConsiderOtherPositions' and @value = 'yes']").click()
    driver.find_element(By.XPATH, "//input [@name = '/legalFormerTeslaEmployee' and @value = 'no']").click()
    driver.find_element(By.XPATH, "//input [@name = '/legalFormerTeslaInternOrContractor' and @value = 'no']").click()
    driver.find_element(By.XPATH, "//input [@name = '/legalReceiveNotifications' and @value = 'yes']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)
    driver.find_element(By.XPATH, "//input [@name = '/legalAcknowledgment' and @type = 'checkbox']").click()
    driver.find_element(By.XPATH, "//input [@name = '/legalAcknowledgmentName' ]").send_keys("Andrew Worthley")
    # time.sleep(.5)
    driver.find_element(By.XPATH, "//button [@data-action-type = 'next']").click()
    # time.sleep(.5)
    # third page
    # hardest part was figureing out how to scroll to allow for selecting a following box
    scrollPlease = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[1]/fieldset[1]/div[1]")
    ActionChains(driver).send_keys_to_element(scrollPlease, Keys.TAB, Keys.TAB).perform()
    time.sleep(delay)
    ActionChains(driver).send_keys_to_element(scrollPlease, Keys.TAB, Keys.TAB).perform()
    try:
        time.sleep(delay)
        driver.find_element(By.XPATH, "//input [@name = '/eeoAcknowledgment']").click()

    except Exception as e:
        print(e)
        ActionChains(driver).send_keys_to_element(scrollPlease, Keys.TAB, Keys.TAB).perform()
        time.sleep(delay * 2)
        driver.find_element(By.XPATH, "//input [@name = '/eeoAcknowledgment']").click()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(delay)
    gender = Select(driver.find_element(By.XPATH, "//select [@name = '/eeoGender']"))
    gender.select_by_value("male")
    veteran = Select(driver.find_element(By.XPATH, "//select [@name = '/eeoVeteranStatus']"))
    veteran.select_by_value("no")
    race = Select(driver.find_element(By.XPATH, "//select [@name = '/eeoRaceEthnicity']"))
    race.select_by_value("white")
    disability = Select(driver.find_element(By.XPATH, "//select [@name = '/eeoDisabilityStatus']"))
    disability.select_by_value("no")
    time.sleep(delay)
    driver.find_element(By.XPATH, "//input [@name = '/eeoDisabilityStatusName']").send_keys("Andrew Worthley")
    # commit this line if you want to test things
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)
    driver.find_element(By.XPATH, "//button [@data-action-type = 'submit']").click()
    time.sleep(delay * 1.5)
    print(xPath)
    print(x)
    x = x + 1
    driver.get(teslaEngineer)
    time.sleep(2)


def drewWebsite():
    driver = webdriver.Chrome()
    drewURL = "https://www.drewworthley.com"
    driver.get(drewURL)
    #clicks the first button
    contact_button = driver.find_element(By.LINK_TEXT, "Get in Contact")
    contact_button.click()
    #clicks second button

    Nextbutton = driver.find_element(By.XPATH,"//button[@class = 'lightbox-handle sqs-system-button sqs-editable-button sqs-button-element--primary']")
    Nextbutton.click()
    #Fill Name
    driver.find_element(By.XPATH, "//input[@name = 'fname']" ).send_keys("webdriver")

    driver.find_element(By.XPATH, "//input[@name = 'lname']").send_keys("webdriver")

    driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("aworthle6114@gmail.com")

    driver.find_element(By.XPATH, "//textarea[@id = 'textarea-yui_3_17_2_1_1558714154117_5168-field']").send_keys("Some shit")


    driver.find_element(By.XPATH, "//input[@class= 'button sqs-system-button sqs-button-element--primary']").click()
    time.sleep(5)
    driver.quit()

def random():
    URL = "https://realpython.github.io/fake-jobs/"

    #page = requests.get(URL)
    #page2 = requests.get(drewURL)




main()