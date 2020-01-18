import wekan
del wekan
import random
s = ["ಹತ್ತಿ (Cotton)","ಅಕ್ಕಿ (Rice)","ಗೋಧಿ (Wheat)","ಬಜ್ರಾ (Bajra)","ಸೆಣಬು (Jute)","ತಂಬಾಕು (Tobacco)","ಹಸಿರು ಗ್ರಾಂ (Green gram)"]
w = ["ಅಕ್ಕಿ (Rice)","ಸೆಣಬು (Jute)","ಗೋಧಿ (Wheat)","ಕಡಲೆ (Chickpea)"]
r = ["ಹತ್ತಿ (Cotton)","ಅಕ್ಕಿ (Rice)","ಗೋಧಿ (Wheat)","ಬಜ್ರಾ (Bajra)","ಸೆಣಬು (Jute)","ತಂಬಾಕು (Tobacco)","ಹಸಿರು ಗ್ರಾಂ (Green gram)","ಕಡಲೆ (Chickpea)"]
while(True):
    
    a = input("ಪ್ರಸ್ತುತ ಋತುವನ್ನು ಸಲ್ಲಿಸಿ : 1.ಬೇಸಿಗೆ \t 2.ಮಳೆಗಾಲ \t 3.ಚಳಿಗಾಲ\n")
    if a == "1":
        print("ಬೇಸಿಗೆಯಲ್ಲಿ ಬೆಳೆಯುವ ಬೆಳೆಗಳು : \n")
        random.shuffle(s)
        for i in s:
            print(i)
        import kannada.fer_kannada
        break
    
    elif a == "2":
        print("ಮಳೆಗಾಲದಲ್ಲಿ ಬೆಳೆಯುವ ಬೆಳೆಗಳು : \n")
        random.shuffle(r)
        for i in r:
            print(i)
        import kannada.fer_kannada
        break
    elif a == "3":
        print("ಚಳಿಗಾಲದಲ್ಲಿ ಬೆಳೆಯುವ ಬೆಳೆಗಳು : \n")
        random.shuffle(w)
        for i in w:
            print(i)
        import kannada.fer_kannada
        break
    else:
         print("ಅಮಾನ್ಯವಾದ ಆಯ್ಕೆಯಿಂದ ನಿರ್ಗಮಿಸಿದೆ, \tದಯವಿಟ್ಟು ಪುನಃ ಪ್ರಯತ್ನಿಸಿ>>")
