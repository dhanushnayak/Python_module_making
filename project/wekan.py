from selenium import webdriver
driver = webdriver.Chrome()
city = str(input("ಪ್ರದೇಶವನ್ನು ನಮೂದಿಸಿ ?? "))
    
driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
print("Time :\t" + driver.find_elements_by_class_name("current-local-time")[0].text)

print(city +" is "+ (driver.find_elements_by_class_name("height")[0].text + "m above sea level"))
print("located : " +driver.find_elements_by_class_name("geo")[0].text)   
print("Weather Report: \n\t" + driver.find_elements_by_class_name("phrase")[2].text)


