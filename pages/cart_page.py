from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class CartPage:
    ITEM_BY_NAME = lambda item_name: Target.the(f"item named {item_name}").located_by(
    (By.XPATH, f"//td[normalize-space()='{item_name}']"))
    LAST_ITEM_ADDED = Target.the("last item added to the cart").located_by((By.XPATH, "//tbody[@id='tbodyid']/tr[1]/td[2]"))
    DELETE_BUTTON = Target.the("button to delete items").located_by((By.XPATH, "//a[normalize-space()='Delete']"))
    