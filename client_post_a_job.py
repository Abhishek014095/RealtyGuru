import faker
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from faker import Faker
import pyautogui

class Find_element_by_job:
    def Details(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.realtyguru.tech/")
        driver.implicitly_wait(4)
        driver.maximize_window()

        Log_in=driver.find_element(By.XPATH,"//div[@class='pl-3 hove']//button[@id='loginbtn']").click()
        time.sleep(2)
        Select_a_guru_platform=driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(2)
        username=driver.find_element(By.XPATH,"//input[@id='login_username']").send_keys("Anderson007")
        Password=driver.find_element(By.XPATH,"//input[@id='login_pass']").send_keys("Ando")
        Sign_in_button=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/button[1]").click()
        time.sleep(5)
        Post_A_Job=driver.find_element(By.XPATH,"//a[normalize-space()='Post a Job']").click()
        time.sleep(2)

        #Request for Quote form
        Job_type=driver.find_element(By.XPATH,"//select[@id='job_type']")
        dd1=Select(Job_type)
        dd1.select_by_value("1")
        time.sleep(2)

        Work_type=driver.find_element(By.XPATH,"//select[@id='work_type']")
        dd2=Select(Work_type)
        dd2.select_by_value("Residential")
        time.sleep(2)

        Job_Size = driver.find_element(By.XPATH, "//select[@id='job_size']")
        dd2 = Select(Job_Size)
        dd2.select_by_value("Small")
        time.sleep(2)

        fake=Faker()
        title=fake.name()
        Request_title=driver.find_element(By.XPATH,"//input[@id='rtitle']").send_keys(f"{"Test"} {title}")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)

        type_of_service=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[6]/span[1]/span[1]/span[1]/span[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[5]").click()
        time.sleep(2)

        address=fake.address()
        prperty_Addess=driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys(f"{address}")
        time.sleep(2)

        state=driver.find_element(By.XPATH,"//select[@id='state']")
        dd=Select(state)
        dd.select_by_value("17")
        time.sleep(3)

        suburb = driver.find_element(By.XPATH, "(//span[@id='select2-suburb-container'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//li[@role='treeitem']").click()
        time.sleep(2)
        button=driver.find_element(By.XPATH,"//button[@id='select_contractors']").click()
        time.sleep(2)
        select_contractor=driver.find_element(By.XPATH,"//label[@for='contractor35']//div[@class='card']//div//img[@alt='image']").click()
        time.sleep(1)
        deselct_admin=driver.find_element(By.XPATH,"//label[@for='refer_to_admin']//div[@class='card']//div[1]").click()
        time.sleep(2)
        save_button=driver.find_element(By.XPATH,"//button[@id='save_selected_contractors']").click()
        time.sleep(1)
        ok_button=driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()
        time.sleep(1)

        choose_a_document_file_Button=driver.find_element(By.XPATH,"//label[normalize-space()='Choose A Document File']")
        choose_a_document_file_Button.click()
        time.sleep(2)
        file_path=r"C:\Users\HIPL\Downloads\dummy.pdf"
        pyautogui.write(file_path)
        pyautogui.press('enter')
        print("file uploaded succefully")
        time.sleep(2)

        driver.execute_script("window.scrollBy(600,800);")
        time.sleep(1)
        data = fake.address()
        Comments=driver.find_element(By.XPATH,"//textarea[@id='comment']")
        Comments.click()
        Comments.send_keys(f"{data}")
        time.sleep(2)

        select_email=driver.find_element(By.XPATH,"//span[contains(text(),'Please Select Email')]").click()
        time.sleep(1)
        choose_email=driver.find_element(By.XPATH,"//span[normalize-space()='sharma.abhi14095@yopmail.com']").click()
        time.sleep(1)
        email_checkbox=driver.find_element(By.XPATH,"//input[@name='is_email_check']").click()
        time.sleep(1)

        select_contact = driver.find_element(By.XPATH, "//span[contains(text(),'Select Mobile Number')]").click()
        time.sleep(1)
        select_contact = driver.find_element(By.XPATH, "//span[normalize-space()='9587800614']").click()
        time.sleep(1)
        contact_checkbox = driver.find_element(By.XPATH, "//input[@name='is_mobile_check']").click()
        time.sleep(1)

        choose_image_file=driver.find_element(By.XPATH,"//label[normalize-space()='Choose Image File']").click()
        time.sleep(1)

        image_path=r"C:\Users\HIPL\Downloads\man.jpg"
        pyautogui.write(image_path)
        pyautogui.press("enter")
        time.sleep(2)

        submit_button=driver.find_element(By.XPATH,"//button[@type='button'][normalize-space()='Submit']").click()
        time.sleep(10)

testing =Find_element_by_job()
testing.Details()

