import gr
del gr
from datetime import datetime
print("**************WELCOME TO NMIT ASSF****************")
print("we are here to help farmers in name of ASSF, On basic data.\n\n")
print("Date : ")
print(datetime.now().date())
print("\n")




while(True):
    a = input("\nSelect the Language through which you need to proceed : \n 1.English \n 2.हिंदी  \n 3.ಕನ್ನಡ \n 4.End process\n")
    
    if a == '1':
        import english.region
        break
    elif a == '2':
        import hindi.region_hindi
        break
    elif a == '3':
        import kannada.region_kannada
        break
    elif a == '4':
        print("Cancelled >>")
        break
    else:
        print("Try again >>")
