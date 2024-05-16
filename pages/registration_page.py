import time

from selenium.webdriver.support.select import Select

from pages.base_page import Base_Page
from locators.locators import Locators
# from validate_email import validate_email


class Registration_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def enter_first_name(self, firstname):
        self.enter_at(self.locator.firstName, firstname)

    def enter_last_name(self, lastname):
        self.enter_at(self.locator.lastName, lastname)

    def enter_address(self, address):
        self.enter_at(self.locator.address, address)

    def enter_email(self, email):
        self.enter_at(self.locator.emailAddress, email)

    def enter_phone(self, phone):
        self.enter_at(self.locator.phone, phone)

    def enter_password(self, first_password):
        self.enter_at(self.locator.first_password, first_password)

    def enter_second_password(self, confirm_password):
        self.enter_at(self.locator.confirm_password, confirm_password)

    # def is_valid_email(self):
    #     return validate_email(self)
    #
    # email = "example@example.com"
    # if is_valid_email(email):
    #     print("Valid email address")
    # else:
    #     print("Invalid email address")

    def select_male(self):
        self.click_element(self.locator.maleRadioButton)

    def select_female(self):
        self.click_element(self.locator.feMaleRadioButton)

    def is_male_radio_button_selected(self):
        return self.is_selected(self.locator.maleRadioButton)

    def is_female_radio_button_selected(self):
        return self.is_selected(self.locator.feMaleRadioButton)

    def select_cricket(self):
        self.click_element(self.locator.cricket)

    def is_cricket_checkbox_selected(self):
        return self.is_selected(self.locator.cricket)

    def select_movies(self):
        self.click_element(self.locator.movies)

    def is_movies_checkbox_selected(self):
        return self.is_selected(self.locator.movies)

    def select_hockey(self):
        self.click_element(self.locator.hockey)

    def is_hockey_checkbox_selected(self):
        return self.is_selected(self.locator.hockey)

    def select_language(self):
        self.click_element(self.locator.language_dropdown)
        time.sleep(1)
        self.click_element(self.locator.arabic)
        time.sleep(1)
        self.click_element(self.locator.languageText)
        time.sleep(1)

    def select_skills(self):
        # element = self.get_element(self.locator.skills)
        select = Select(self.get_element(self.locator.skills))
        # select.select_by_index(1)
        # select.select_by_value("Analytics")
        select.select_by_visible_text("Android")

