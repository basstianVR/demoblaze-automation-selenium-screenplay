from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def create_user():
    # Set up the Chrome driver correctly
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)  # Correct way

    return Actor.named("Sebas").who_can(BrowseTheWeb.using(driver))
