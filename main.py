#importing webdriver from selenium
import time
import autoit
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
driver = webdriver.Firefox(executable_path = './geckodriver.exe')
   
#URL of the website 
url = "https://www.remove.bg/upload"
   
driver.get(url)

time.sleep(5)

button = driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[1]/div/div[1]/div[2]/button")
handles = driver.window_handles

ActionChains(driver).move_to_element(button).click().perform()

curr = driver.switch_to.window(handles.pop());

autoit.control_set_text(curr, "Edit1", "F:\Workspace\img_project\img.jpeg")
autoit.control_click(curr, "Button1")
print("File is Uploaded Successfully")

time.sleep(5)
uri = "https://o.remove.bg/downloads/fc812a94-fada-4877-b526-8bb2753427eb/img-removebg-preview.png"

r = requests.get(uri, allow_redirects=True)

down = driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[1]")
#handles = driver.window_handles

#ActionChains(driver).move_to_element(down).click().perform()

#curr = driver.switch_to.window(handles.pop());
#time.sleep(7)
#autoit.control_click(curr, "Button1")
open('F:/Workspace/img_project/bg_r/img_bg_r.png', 'wb').write(r.content)

print("File opened succesfully!")