import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="function")
def driver(request):
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 11'
    sauce_options = {
        'username': 'oauth-abhisheksharma.hipl-ed503',
        'accessKey': '1b7e393f-2b7d-442d-a6de-a527c73264cc',
        'build': 'Parallel Test Build',
        'name': 'abhishek'
    }
    options.set_capability('sauce:options', sauce_options)

    driver = webdriver.Remote(
        command_executor='https://oauth-abhisheksharma.hipl-ed503:1b7e393f-2b7d-442d-a6de-a527c73264cc@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        options=options
    )
    yield driver
    driver.quit()
