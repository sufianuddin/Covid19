#Importing packages
import pandas as pd
import gspread as gs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

start_time = time.time()

options = Options()
options.headless = True
options.add_argument("disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument('--disable-logging')
options.add_argument("log-level=3")

driver = webdriver.Chrome('chromedriver.exe', options=options)   #Google Chrome Version 92.0.4515.107
print ("Headless Chrome Initialized")
driver.set_window_position(975, 5)
driver.get('https://datastudio.google.com/embed/reporting/1PLVi5amcc_R5Gh928gTE8-8r8-fLXJQF/page/R24IB')

path='//*[@id="body"]/div/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/lego-report/lego-canvas-container/div/file-drop-zone/span/content-section/div[71]/canvas-component/div/div/div[1]/div/div/lego-table'
timeout = 20

try:
    element_present = EC.presence_of_element_located((By.XPATH, path))
    WebDriverWait(driver, timeout).until(element_present)
    element = driver.find_elements_by_class_name('tableBody')[1]
    elemText = element.text
    
    driver.quit()
    
    # Convert string to list
    def Convert(string):
        ls = list(string.split("\n"))
        return ls
     
    lsData=Convert(elemText)
    
    df = pd.DataFrame(lsData)
    
    df1= df.iloc[0:5].reset_index(drop=True)
    df2= df.iloc[5:10].reset_index(drop=True)
    df3= df.iloc[10:15].reset_index(drop=True)
    df4= df.iloc[15:20].reset_index(drop=True)
    df5= df.iloc[20:25].reset_index(drop=True)
    df6= df.iloc[25:30].reset_index(drop=True)
    df7= df.iloc[30:35].reset_index(drop=True)
    
    dfs = [df1, df2, df3, df4, df5, df6, df7]
    nan_value = 0
    
    result_1 = pd.concat(dfs, join='outer', axis=1).fillna(nan_value)
    
    result_1transposed = result_1.T
    finalData = result_1transposed.rename(columns={0: "Province", 1: "Confirmed Cases", 2: "Active Cases", 3: "Deaths", 4: "Recoveries"}).reset_index(drop=True)
    print(finalData)
    
    products_list = [finalData.columns.values.tolist()] + finalData.values.tolist()
    
    print ("Data to Google Sheets Initialized")
    gc = gs.service_account(filename='keys.json')   #Google credentials from google service
    sh = gc.open("countryProvince")   #Goole sheet file name
    worksheet = sh.worksheet("Sheet1")   #Sheet tab name
    req=worksheet.update('A1', products_list)   #Send data to google spread sheet
    
    seconds = time.time() - start_time
    print('Time Taken to Complete this Job:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
    
except TimeoutException:
    print ("Timed out waiting for page to load")
    driver.quit()