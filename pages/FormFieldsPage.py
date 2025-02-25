from typing import List
from selenium.webdriver.remote.webelement import WebElement
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class FormFieldsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.name = (By.ID, 'name-input')
        self.password = (By.XPATH, '//input[@type="password"]')
        self.milk_checkbox = (By.ID, 'drink2')
        self.coffee_checkbox = (By.CSS_SELECTOR, '[for="drink3"]')
        self.yellow_radiobutton = (By.XPATH, '//input[@value="Yellow"]')
        self.select_value = (By.ID, 'automation')
        self.option_from_list = (By.CSS_SELECTOR, '[value="yes"]')
        self.email = (By.XPATH, '//input[@name="email"]')
        self.list_tools = (By.XPATH, '//form/ul/li')
        self.message = (By.ID, 'message')
        self.btn_submit = (By.ID, 'submit-btn')

    @allure.step(r'Ввести имя')
    def input_name(self, name: str) -> None:
        self.fill_field(self.name, name)

    @allure.step(r'Ввести пароль')
    def input_password(self, password: str) -> None:
        self.fill_field(self.password, password)

    @allure.step(r'В списке "What is your favorite drink?" кликнуть на Milk')
    def click_milk_checkbox(self) -> None:
        self.click_element(self.milk_checkbox)

    @allure.step(r'В списке "What is your favorite drink?" кликнуть на Coffee')
    def click_coffee_checkbox(self) -> None:
        self.click_element(self.coffee_checkbox)

    @allure.step(r'В списке "What is your favorite color?" кликнуть на Yellow')
    def click_yellow_radiobutton(self) -> None:
        self.click_element(self.yellow_radiobutton)

    @allure.step(r'В поле Do you like automation? выбрать любой вариант')
    def click_option_list(self) -> None:
        self.select_option_from_list(self.select_value, self.option_from_list)

    @allure.step(r'Ввести почту')
    def input_email(self, email: str) -> None:
        self.fill_field(self.email, email)

    @allure.step(r'Получить список всех инструментов')
    def get_list_tools(self) -> List[WebElement]:
        return self.find_elements(*self.list_tools)

    @allure.step(r'Ввести количество инструментов и название инструмента, '
                 r'содержащее наибольшее количество символов')
    def input_message(self, message: str) -> None:
        self.fill_field(self.message, message)

    @allure.step(r'Нажать на кнопку "Submit"')
    def click_btn_submit(self) -> None:
        self.click_element(self.btn_submit)
