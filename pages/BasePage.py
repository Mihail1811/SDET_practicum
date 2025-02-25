from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import Union, List
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    def select_option_from_list(
        self,
        locator1: tuple,
        locator2: tuple
    ) -> None:
        """
        Выбирает опцию из выпадающего списка на основе текста нужного элемента.
        :param locator1: кортеж, указывающий на элемент <select>
        :param locator2: кортеж, указывающий на элемент с текстом опции
        """
        select = Select(self.find_element(*locator1))
        option = self.find_element(*locator2).text
        select.select_by_visible_text(option)

    def find_element(self, by: Union[By, int], value: str) -> WebElement:
        """
        Находит один элемент на странице
        :param by: Способ поиска локаторов
        :param value: Значение локатора
        :return: WebElement
        """
        return self.wait.until(
            expected_conditions.visibility_of_element_located(
                (by, value)
            ), message=f'Элемент {by, value} не найден')

    def find_elements(
        self,
        by: Union[By, int],
        value: str
    ) -> List[WebElement]:
        """
        Находит все элементы, соответствующие локатору, на странице
        :param by: Способ поиска локаторов
        :param value: Значение локатора
        :return: Список WebElement
        """
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (by, value)
            ), message=f'Элементы {by, value} не найдены')

    def click_element(self, locator: tuple) -> None:
        """
        Кликает по элементу
        :param locator: Кортеж, определяющий локатор
        """
        self.find_element(*locator).click()

    def fill_field(self, locator: tuple, info: str) -> None:
        """
        Заполняет поле текстом
        :param locator: Кортеж, определяющий локатор
        :param info: Текст для ввода
        """
        self.find_element(*locator).send_keys(info)
