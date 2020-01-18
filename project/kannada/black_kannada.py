import wekan
del wekan
import random
s = ["ಹತ್ತಿ (Cotton)","ಗೋಧಿ (Wheat)","ಜೋಳ (Jower)","ಸೂರ್ಯಕಾಂತಿ (Sunflower)","ತಂಬಾಕು (Tobacco)","ರಾಗಿ (Ragi)","ತೈಲ ಬೀಜಗಳು (Oilseeds)"]
w = ["ಈರುಳ್ಳಿ (Onions)","ಹಸಿರು ಚಳಿಯನ್ನು (Green chills)","ಅವರೆಕಾಳು (Peas)","ಬ್ರಿಂಜಲ್ಸ್ (Brinjal)"]
r = s + w
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
        print("ಅಮಾನ್ಯವಾದ ಆಯ್ಕೆಯಿಂದ ನಿರ್ಗಮಿಸಿದೆ, \tದಯವಿಟ್ಟು ಪುನಃ ಪ್ರಯತ್ನಿಸಿ >>")
