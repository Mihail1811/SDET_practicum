import time
import allure
from pages.FormFieldsPage import FormFieldsPage
import pytest


def test_form(driver):
    form_page = FormFieldsPage(driver)
    form_page.input_name('Михаил')
    form_page.input_password('1234')
    form_page.click_milk_checkbox()
    form_page.click_coffee_checkbox()
    driver.set_window_size(1000, 2000)
    driver.execute_script("window.scrollBy(0, 900);")
    time.sleep(1)
    form_page.click_yellow_radiobutton()
    form_page.click_option_list()
    form_page.input_email("name@example.com")
    list_tools = form_page.get_list_tools()
    longest_tool = max([tool.text for tool in list_tools], key=len)
    form_page.input_message(f'{len(list_tools)}\n{longest_tool}')
    form_page.click_btn_submit()
    alert = driver.switch_to.alert
    alert_text = alert.text
    with allure.step(r'Проверить, что текст в появившемся окне '
                     r'совпадает со считанным значением'):
        assert alert_text == 'Message received!', \
            'Значения не совпадают!'
            

if __name__ == '__main__':
    pytest.main()
