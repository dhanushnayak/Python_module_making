import wekan
del wekan
import random
s = ["ಗೋಧಿ (Wheat)","ಮೆಕ್ಕೆ ಜೋಳ (Maize)","ರಾಗಿ (Ragi)","ತೈಲ ಬೀಜಗಳು (Oilseeds)","ಧಾನ್ಯಗಳು (Millets)","ಮಾವಿನ ಹಣ್ಣು (Mango)"]
w = ["ಅಕ್ಕಿ (Rice)","ರಾಗಿ (Ragi)","ಗೋಧಿ (Wheat)","ಮಾವಿನ ಹಣ್ಣು (Mango)"]
r = w + ["ಕಬ್ಬು (Sugecane)","ಕಡಲೆಕಾಯಿ (Groundnets)"]
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
          
