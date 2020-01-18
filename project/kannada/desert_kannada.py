import wekan
del wekan
import random
s = ["ಧಾನ್ಯಗಳು (Millets)","ಬಾರ್ಲಿ (Barley)","ಸಾಗುರೊ (Saguaro)","ಕಾಫಿ (Coffee)"]
w = ["ಆನೆಯ ಮರಗಳು (Elephant tress)","ಕಳ್ಳಿ (Catcus)"]
r = s + ["ಮರುಭೂಮಿ ಮಾರಿಗೋಲ್ಡ್ (Desert Marigold)"]
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
        print("ಅಮಾನ್ಯವಾದ ಆಯ್ಕೆಯಿಂದ ನಿರ್ಗಮಿಸಿದೆ,***ದಯವಿಟ್ಟು ಪುನಃ ಪ್ರಯತ್ನಿಸಿ>>")
          
