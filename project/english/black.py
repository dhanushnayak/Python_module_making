import we
del we
import random
s = ["Cotton","Wheat","Jower","Sunflower","Tobacco","Ragi","Oilseeds"]
w = ["Onions","Green chills","Peas","Brinjal"]
r = s + w
while(True):
    
    a = input("Submit the present SEASON and click ok***\n")
    if a == "summer" or a == "SUMMER":
        print("Crops Grown in SUMMER : \n")
        random.shuffle(s)
        for i in s:
            print(i)
        import english.fer
        break
    elif a == "rainy" or a == "RAINY":
        print("Crops Grown in RAINY : \n")
        random.shuffle(r)
        for i in r:
            print(i)
        import english.fer
        break
    elif a == "winter" or a == "WINTER":
        print("Crops Grown in WINTER : \n")
        random.shuffle(w)
        for i in w:
            print(i)
        import english.fer
        break


    else:
        print("Invalid Choice >> Try Again >>")
