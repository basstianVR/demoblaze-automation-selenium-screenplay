from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def create_user():
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    return Actor.named("Sebas").who_can(BrowseTheWeb.using(driver))
