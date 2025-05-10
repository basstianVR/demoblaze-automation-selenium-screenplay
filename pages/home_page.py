from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class HomePage:
    BUTTON_PREVIOUS_CARRUSEL_PAGE = Target.the("button to go to previous carrusel page").located_by((By.XPATH, "//span[@class='carousel-control-prev-icon']"))
    BUTTON_NEXT_CARRUSEL_PAGE = Target.the("button to go to carrusel items page").located_by((By.XPATH, "//span[@class='carousel-control-next-icon']"))
    BUTTON_CATEGORIES_FILTER = Target.the("button to rest the any filter ").located_by((By.XPATH, "//a[@id='cat']"))
    BUTTON_PHONE_FILTER = Target.the("button to filter just phones ").located_by((By.XPATH, "//div[@id='contcont']//a[2]"))
    BUTTON_LAPTOP_FILTER = Target.the("button to filter just laptops ").located_by((By.XPATH, "//a[3]"))
    BUTTON_MONITOR_FILTER = Target.the("button to filter just monitors ").located_by((By.XPATH, "//a[4]"))
    BUTTON_PREVIOUS_ITEMS_PAGE = Target.the("button to go to previous items page").located_by((By.XPATH, "//button[@id='prev2']"))
    BUTTON_NEXT_ITEMS_PAGE = Target.the("button to go to next items page").located_by((By.XPATH, "//button[@id='next2']"))
    ITEM_BY_NAME = lambda item_name: Target.the(f"item named {item_name}").located_by(
    (By.XPATH, f"//a[normalize-space()='{item_name}']"))
