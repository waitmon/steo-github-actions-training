import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


@allure.title('Simple page')
def test_button_exist(browser):
    with allure.step('Check button is displayed'):
        browser.get('https://www.qa-practice.com/elements/button/simple')
        allure.attach(browser.get_screenshot_as_png(), name="simple", attachment_type=AttachmentType.PNG)
        assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()


@allure.title('Like a button page')
def test_button_exist_2(browser):
    with allure.step('Check button is displayed'):
        browser.get('https://www.qa-practice.com/elements/button/like_a_button')
        allure.attach(browser.get_screenshot_as_png(), name="like_a_button", attachment_type=AttachmentType.PNG)
        assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()


# test_branch_commit for 100th time
def test_me():
    assert 1 == 1
