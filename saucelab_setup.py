from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = ChromeOptions()


options.browser_version = 'latest'
options.platform_name = 'Windows 11'
# Sauce Labs credentials
sauce_options = {
   'username': 'oauth-abhisheksharma.hipl-ed503',
   'accessKey': '1b7e393f-2b7d-442d-a6de-a527c73264cc',
   'build': 'Python-Selenium-Build',
   'name': 'Sample Test'
}
options.set_capability('sauce:options', sauce_options)


# Connect to Sauce Labs
driver = webdriver.Remote(
   command_executor='https://oauth-abhisheksharma.hipl-ed503:1b7e393f-2b7d-442d-a6de-a527c73264cc@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
   options=options
)
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com")
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("python with selenium")
print("Setup completed!")
driver.quit()
