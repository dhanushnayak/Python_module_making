def nwest():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಟ ಪ್ರಮಾಣದ ಮರುಭೂಮಿ ಮಣ್ಣು ಇದೆ*****")
    import kannada.desert_kannada
def north():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಠ ಪ್ರಮಾಣದ ಮಣ್ಣಿನ ಮಣ್ಣು ಇದೆ*****")
    import kannada.alluvial_kannada
def neast():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಟ ಪ್ರಮಾಣದ ಕೆಂಪು ಮಣ್ಣು ಇದೆ*****")
    import kannada.red_kannada
def west():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಠ ಪ್ರಮಾಣದ ಕಪ್ಪು ಮಣ್ಣು ಇದೆ*****")
    import kannada.black_kannada
def central():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಠ ಪ್ರಮಾಣದ ಕಪ್ಪು ಮಣ್ಣು ಇದೆ*****")
    import kannada.black_kannada
def east():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಟ ಪ್ರಮಾಣದ ಕೆಂಪು ಮಣ್ಣು ಇದೆ*****")
    import kannada.red_kannada
def swest():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಟ ಪ್ರಮಾಣದ ಕೆಂಪು ಮಣ್ಣು ಇದೆ*****")
    import kannada.red_kannada
def south():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಟ ಪ್ರಮಾಣದ ಕೆಂಪು ಮಣ್ಣು ಇದೆ*****")
    import kannada.red_kannada
def seast():
    print("*****ವಲಯದಲ್ಲಿ ಗರಿಷ್ಠ ಪ್ರಮಾಣದ ಮೆಕ್ಕಲು ಮಣ್ಣು ಇದೆ*****")
    import kannada.alluvial_kannada
while(True):
    
    a = input("ರಾಜ್ಯವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ (State) : \n1.ಜಮ್ಮು ಮತ್ತು ಕಾಶ್ಮೀರ (Jammu and Kashmir)\n2.ಹಿಮಾಚಲ ಪ್ರದೇಶ (Himachal Pradesh)\n3.ಪಂಜಾಬ್ (Punjab)\n4.ಉತ್ತರಾಖಂಡ್ (Uttarkand)\n5.ಉತ್ತರ ಪ್ರದೇಶ (Uttar pradesh)\n6.ಹರಿಯಾಣ (Haryana)\n7.ರಾಜಸ್ಥಾನ (Rajasthan)\n8.ಅಸ್ಸಾಂ (Assam)\n9.ಸಿಕ್ಕಿಂ (Sikkim)\n10.ನಾಗಾಲ್ಯಾಂಡ್ (Nagaland)\n11.ಮೇಘಾಲಯ (Meghalaya)\n12.ಮಣಿಪುರ (Manipur)\n13.ಮಿಜೋರಾಮ್ (Mizoram)\n14.ತ್ರಿಪುರ (Tripura)\n15.ಅರುಣಾಚಲ ಪ್ರದೇಶ (Arunachal Pradesh)\n16.ಪಶ್ಚಿಮ ಬೆಂಗಲ್ (West bengal)\n17.ಮಧ್ಯ ಪ್ರದೇಶ (Madhya Pradesh)\n18.ಛತ್ತೀಸ್ಗಢ (Chhattisgarh)\n19.ಗುಜರಾತ್ (Gujarat)\n20.ಗೋವಾ (Goa)\n21.ಮಹಾರಾಷ್ಟ್ರ (Maharashtra)\n22.ಬಿಹಾರ (Bihar)\n23.ಒರಿಸ್ಸಾ (Orissa)\n24.ಜಾರ್ಖಂಡ್ (Jharkhand)\n25.ತೆಲಂಗಾಣ (Telangana)\n26.ಆಂಧ್ರ ಪ್ರದೇಶ (Andhra Pradesh)\n27.ಕರ್ನಾಟಕ (Karnataka)\n28.ಕೇರಳ (Kerala)\n29.ತಮಿಳು ನಾಡು (Tamil nadu)\nನಿಮ್ಮ ರಾಜ್ಯ ಆಯ್ಕೆಯನ್ನು ಸಲ್ಲಿಸಿ : \n")
    if a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6':
        north()
        break
    elif a == '7':
        nwest()
        break
    elif a == '8' or a == '9' or a == '10' or a == '11' or a == '12' or a == '13' or a == '14' or a == '15':
        neast()
        break
    elif a == '17' or a == '18':
        central()
        break
    elif a == '19' or a == '20' or a == '21':
        west()
        break
    elif a == '22' or a == '23' or a == '24' or a == '16':
        east()
        break
    elif a == '25' or a == '26' or a == '27':
        south()
        break
    elif a == '28':
        swest()
        break
    elif a == '29':
        seast()
        break
    else:
        print(">> ತಪ್ಪು ಆಯ್ಕೆ *** ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ >>")
    
        
    

