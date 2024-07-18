from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException

###########################################################################################################################
def setup_driver():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Create a Chrome WebDriver instance and maximize the window
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def navigate_to_login(driver):
    # Navigate to the login page
    driver.get("https://beta.peerprofiler.com/login")
    time.sleep(5)

def fill_login_credentials(driver):
    # Fill in the username and password fields
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    username_field.send_keys("devanand@kolspeers.com")
    password_field.send_keys("KnP@121New2024")
    
    # Click the login button
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    time.sleep(20)
    
def Interactions_menu(driver):
    click_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[12]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(1)
    GraphicalView = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'GRAPHICAL VIEW')])[1]")))
    GraphicalView.click()
    time.sleep(5)
#########################################################################################################################################################################

def Mode_of_Interaction(driver):
    
    # Validate the title "Mode of Interaction"
    title_validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//label[normalize-space()='Mode of Interaction'])[1]")))
    if title_validation:
        print("Title 'Mode of Interaction' Tab present")
    else:
        print("Title 'Mode of Interaction' Tab not open")
        return
      
    # Locate all bars in the bar graph
    vertical_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']"
    bars_list = driver.find_elements(By.XPATH, vertical_xpath)
    print(f"Total bars: {len(bars_list)}")

    actions = ActionChains(driver)
    for bar in bars_list:
        actions.move_to_element(bar).click().perform()
        time.sleep(1) 
        
        while True:
            try:
                tab_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']"
                clicked_tab = driver.find_elements(By.XPATH, tab_xpath)
                print("************************************************************************************************")
                print(f"Total contain data count: {len(clicked_tab)}")
                
                for tab in clicked_tab:
                    print("Present data on bar -->", tab.text)
                    
                time.sleep(1)
                break

            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered, retrying...") 
                time.sleep(2) 
    
#################################################################################################################################################################            
    
def Top_10Doctors_by_Interaction(driver):
    
    # Validate the title "Mode of Interaction"
    title_validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//label[normalize-space()='Top 10 Doctors by Interaction'])[1]")))
    if title_validation:
        print("Title 'Top 10 Doctors by Interaction' Tab present")
    else:
        print("Title 'Top 10 Doctors by Interaction' Tab not open")
        return
      
    # Locate all bars in the bar graph
    vertical_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']"
    bars_list = driver.find_elements(By.XPATH, vertical_xpath)
    print(f"Total bars: {len(bars_list)}")

    actions = ActionChains(driver)
    for bar in bars_list:
        actions.move_to_element(bar).click().perform()
        time.sleep(1) 
        
        try:
                tooltip_xpath = "//div[@id='TopDoctorsByInteractionId']//div//*[name()='svg']//*[name()='g']//*[name()='g']//*[name()='g']//*[name()='g']//*[name()='g' and contains(@role,'tooltip')]//*[name()='g']//*[name()='g' and contains(@fill,'#000000')]//*[name()='g' and contains(@transform,'translate(')]//*[name()='text' and contains(@x,'0')]/*[name()='tspan']"
                tooltip_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, tooltip_xpath)))
                print("Tooltip Data:", tooltip_element.text)
        except TimeoutException:
                print("Tooltip not found for this bar")    
##################################################################################################################################################################            
    
def Noof_Interactions_By_Category(driver):
    
    # Validate the title "Mode of Interaction"
    title_validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//label[normalize-space()='No. of Interactions By Category'])[1]")))
    if title_validation:
        print("Title 'No. of Interactions By Category' Tab present")
    else:
        print("Title 'No. of Interactions By Category' Tab not open")
        return
      
    # Locate all bars in the bar graph
    vertical_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']"
    bars_list = driver.find_elements(By.XPATH, vertical_xpath)
    print(f"Total bars: {len(bars_list)}")

    actions = ActionChains(driver) 
    for bar in bars_list:
        actions.move_to_element(bar).click().perform()
        time.sleep(1) 
        
        try:
                tooltip_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='text']/*[name()='tspan']"
                tooltip_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, tooltip_xpath)))
                print("Tooltip Data:", tooltip_element.text)
                
                tooltip_data = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='text']/*[name()='tspan'][2]"
                tooltip_data1= WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, tooltip_data)))
                print("Tooltip Data:", tooltip_data1.text)
        except TimeoutException:
                print("Tooltip not found for this bar")  

##################################################################################################################################################################            
    
def Noof_Interactions_By_SubCategory(driver):
    
    # Validate the title "Mode of Interaction"
    title_validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='No. of Interactions By Sub-Category']")))
    if title_validation:
        print("Title 'Noof_Interactions_By_SubCategory' Tab present")
    else:
        print("Title 'Noof_Interactions_By_SubCategory' Tab not open")
        return
      
    # Locate all bars in the bar graph
    vertical_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']/*[name()='g']"
    bars_list = driver.find_elements(By.XPATH, vertical_xpath)
    print(f"Total bars: {len(bars_list)}")

    actions = ActionChains(driver) 
    for bar in bars_list:
        actions.move_to_element(bar).click().perform()
        time.sleep(1) 
     
        try:    
            tooltip_xpath = "//div[@id='NoOfInteractionBySubCategoryId']//div//*[name()='svg']//*[name()='g']//*[name()='g'][2]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='g'][2]/*[name()='g'][4]/*[name()='g']/*[name()='g']"
            tooltip_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, tooltip_xpath)))
            print("Tooltip Data:", tooltip_element.text)
        except TimeoutException:
                print("Tooltip not found for this bar")  

##################################################################################################################################################################  
if __name__ == "__main__":
    driver = setup_driver()
    navigate_to_login(driver) 
    fill_login_credentials(driver) 
    Interactions_menu(driver)
    Mode_of_Interaction(driver)
    Top_10Doctors_by_Interaction(driver) 
    Noof_Interactions_By_Category(driver)
    Noof_Interactions_By_SubCategory(driver) 
# #############################################################################################################################################