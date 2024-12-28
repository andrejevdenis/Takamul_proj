import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach
from dotenv import load_dotenv
"""
For local run by Chrome uncomment lines 12-14 and 53-54, comment out lines 15-49
"""
# @pytest.fixture(scope='function')
# def browser_management(request):
#     browser.driver.fullscreen_window()
DEFAULT_BROWSER_VERSION = '125'
def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='125'
    )
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def browser_management(request):
    browser_version = request.config.getoption('--browser')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "firefox",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://www.takamul.net.sa/'
    options.page_load_strategy = 'eager'
    browser.driver.fullscreen_window()

    yield

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()