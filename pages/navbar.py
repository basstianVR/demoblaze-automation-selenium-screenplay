from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class NavBar:
    LOGIN_NAV_BUTTON = Target.the("login nav button").located_by((By.ID, "login2"))
    WELCOME_FIELD = Target.the("welcome field").located_by((By.XPATH, "//a[@id='nameofuser']"))
    WELCOME_MESSAGE = Target.the("welcome message").located((By.ID, "nameofuser"))
    CART_BUTTON = Target.the("button to the cart").located_by((By.XPATH, "//a[normalize-space()='Cart']"))
    CONTACT_BUTTON = Target.the("button to the contact form").located_by((By.XPATH, "//a[normalize-space()='Contact']"))
    ABOUT_US_BUTTON = Target.the("button to display the about us section")
    LOG_OUT_BUTTON = Target.the("button to log out").located_by((By.XPATH, "//a[@id='logout2']"))
    HOME_BUTTON = Target.the("button to go to home section").located_by((By.XPATH, "//li[@class='nav-item active']//a[@class='nav-link']"))