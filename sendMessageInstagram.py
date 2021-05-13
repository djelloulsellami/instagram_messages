import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='/home/Desktop/pythonProjects/geckodriver')	

def login(username, password):
    driver.get("http://www.instagram.com")
    username_input = None
    password_input = None
    while username_input is None:
        try:
            username_input = driver.find_element(By.NAME, "username")
            password_input = driver.find_element(By.NAME, "password")
        except NoSuchElementException:
            pass

    username_input.send_keys(username)
    time.sleep(1)
    password_input.send_keys(password)
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()

    ("Logged in")

    save_info = None
    btn_hide_notification = None
    while save_info is None:
        try:
            save_info = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
            save_info.click()
        except NoSuchElementException:
            pass

    btn_hide_notification = None
    while btn_hide_notification is None:
        try:
            btn_hide_notification = driver.find_element(By.CSS_SELECTOR, "button.aOOlW:nth-child(2)")
            btn_hide_notification.click()
        except NoSuchElementException:
            pass

def openConversation(username):
    driver.get('https://www.instagram.com/direct/new/')
    query_input = None
    while query_input is None:
        try:
            query_input = driver.find_element(By.NAME, "queryBox")
            query_input.send_keys(username)
        except NoSuchElementException:
            pass

    time.sleep(5)

    select_user = None
    while select_user is None:
        try:
            select_user = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div[2]/div")
        except:
            pass
    select_user.click()


    next_button = None
    while next_button is None:
        try:
            next_button = driver.find_element(By.XPATH, "//*[text()='Next']")
        except:
            pass
    next_button.click()

    print("Conversation with " + username + " Opened")

def sendMessage(message, delay):
    message_textarea = None
    while message_textarea is None:
        try:
            message_textarea = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Message...']")
        except:
            pass

    for c in message:
        message_textarea.send_keys(c)
        time.sleep(delay / len(message))
    message_textarea.send_keys('\n')
    time.sleep(1)

def sendImage():
    upload = "D:\\PycharmProjects\\pythonProject\\Get data instagram\\1.png"
    image_input = driver.find_element(By.CLASS_NAME, "tb_sK")
    image_input.send_keys(upload)
    upload = "D:\\PycharmProjects\\pythonProject\\Get data instagram\\2.png"
    image_input = driver.find_element(By.CLASS_NAME, "tb_sK")
    image_input.send_keys(upload)

def deleteMessage():
    btn = None
    while btn is None:
        try:
            btn = driver.find_element(By.XPATH, "//html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button")
            btn.click()
        except:
            pass

    message_textarea = None
    while message_textarea is None:
        try:
            message_textarea = driver.find_element(By.XPATH, "//*[text()='Supprimer la discussion']")
            message_textarea.click()
        except NoSuchElementException:
            pass
#dzyri promotion, algeria big project,
    message_textarea = None
    while message_textarea is None:
        try:
            message_textarea = driver.find_element(By.XPATH, "//html/body/div[5]/div/div/div/div[2]/button[1]")
            message_textarea.click()
        except NoSuchElementException:
            pass
if __name__ == "__main__":
    # Login to your account
    login("your_username", "your_password")


    # Go To Messages Page
    usernames = ['user1', 'user2', 'user3', 'user4']
    for username in usernames:
        # Open Conversation with username
        try:
            openConversation(username)
            sendMessage("السلام عليكم", 2)
            sendMessage("عيدكم مبارك، غفر الله لنا ولكم وتقبل الله منا ومنكم وكل عام وأنتم إلى الله أقرب", 6)
            print("Message Sent.")
            time.sleep(2)
        except:
            pass
