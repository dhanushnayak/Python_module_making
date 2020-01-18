from selenium import webdriver
driver = webdriver.Chrome()
city = str(input("Enter the locality ?? "))
    
driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")

print(city +" is "+ (driver.find_elements_by_class_name("height")[0].text + "m above sea level"))
print("located : " +driver.find_elements_by_class_name("geo")[0].text)
print("Time :\t" + driver.find_elements_by_class_name("current-local-time")[0].text)
    
print("Weather Report: \n\t" + driver.find_elements_by_class_name("b-forecast__table-description-cell--js")[2].text)
