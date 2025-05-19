from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class ContactPage:
    BUTTON_X = Target.the("x button to close the contact section").located_by((By.XPATH, '//*[@id="exampleModal"]/div/div/div[1]/button/span'))
    EMAIL_FIELD = Target.the("email field").located_by((By.ID, "recipient-email"))
    NAME_FIELD = Target.the("name_field").located_by((By.ID, "recipient-name"))
    MESSAGE_FIELD = Target.the("message field").located_by((By.ID, "message-text"))
    BUTTON_CLOSE = Target.the("button to close contact section").located_by((By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[1]'))
    BUTTON_SEND_MESSAGE = Target.the("button to send the message").located_by((By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[2]'))