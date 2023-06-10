import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from webdriver_manager.chrome import ChromeDriverManager

accountNumber = 1
email = input("Your email sir : ")


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]
user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100
)
user_agent = user_agent_rotator.get_random_user_agent()

webdriverOptions = webdriver.ChromeOptions()
webdriverOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
webdriverOptions.add_argument("--disable-infobars")
webdriverOptions.add_argument("--disable-popup-blocking")
webdriverOptions.add_argument(f"--user-agent=" "Mozilla/5.0")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=webdriverOptions
)


def randomEmail(sa_email):
    return "".join(email)


def randomUsername(sa_username):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(sa_username))


def randomPassword(sa_password):
    return "".join(
        random.choice(string.digits + string.ascii_letters) for _ in range(sa_password)
    )


def blackMan():
    timeout = 3
    Username = randomUsername(14)
    Password = randomPassword(17)
    print(f"UserName Is : {Username}")
    print(f"Password Is : {Password}")
    DateOfWhite = (
        random.choice(
            [
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
            ]
        )
        + "/"
        + random.choice(
            ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        )
        + "/"
        + random.choice(
            [
                "1980",
                "1981",
                "1982",
                "1983",
                "1984",
                "1985",
                "1986",
                "1987",
                "1988",
                "1989",
                "1990",
                "1991",
                "1992",
                "1993",
                "1994",
                "1996",
                "1997",
                "1998",
                "1999",
                "2000",
            ]
        )
    )

    driver.get("https://account.riotgames.com/")
    f = open("accountsforwhitepeople.txt", "a")

    signINCheck = EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/h5")
    )  # check for Sign In text
    WebDriverWait(driver, timeout).until(signINCheck)
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )  # scroll down
    driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[3]/a[2]"
    ).click()  # click Create Account

    signUPCheck = EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/h5")
    )  # check for What's your email?
    WebDriverWait(driver, timeout).until(signUPCheck)
    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input",
    ).send_keys(
        email
    )  # fill random E-Mail
    f.write("E-mail: " + email + "\n")  # write e-mail to file
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )  # scroll down
    driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button"
    ).click()  # click red arrow

    dobUPCheck = EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/h5[1]")
    )  # check for When were you born? text
    WebDriverWait(driver, timeout).until(dobUPCheck)
    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input",
    ).send_keys(
        DateOfWhite
    )  # fill random date of birth
    f.write("DOB: " + DateOfWhite + "\n")
    driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button"
    ).click()  # click red arrow again

    usernameCheck = EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/h5[1]")
    )  # check for Choose a username text
    WebDriverWait(driver, timeout).until(usernameCheck)
    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input",
    ).send_keys(Username)
    f.write("Username: " + Username + "\n")
    driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button"
    ).click()  # click red arrow again

    passwordCheck = EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/h5[1]")
    )  # check for Choose a password text
    WebDriverWait(driver, timeout).until(passwordCheck)
    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input",
    ).send_keys(Password)
    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/input",
    ).send_keys(Password)
    f.write("Password: " + Password + "\n")
    f.write("/////////////////////////////////" + "\n")
    f.close()
    driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button"
    ).click()  # click red arrow again

    if EC.alert_is_present():
        # TODO: wait for hcaptcha solver to solve.
        print("Waiting for u to solve captcha.")
    else:
        print("No captcha.")


blackMan()
