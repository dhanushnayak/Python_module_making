from selenium import webdriver
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_driver_path = r"D://dataset/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver = webdriver.Chrome()
city = str(input("Enter the locality ?? "))
    
driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
print("Time :\t" + driver.find_elements_by_class_name("current-local-time")[0].text)

print(city +" is "+ (driver.find_elements_by_class_name("height")[0].text + "m above sea level"))
print("located : " +driver.find_elements_by_class_name("geo")[0].text)   
print("Weather Report: \n\t" + driver.find_elements_by_class_name("phrase")[2].text)


