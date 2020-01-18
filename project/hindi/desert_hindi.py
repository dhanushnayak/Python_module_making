import wehin
del wehin
import random
s = ["बाजरा (Millets)","जौ (Barley)","Saguaro","कॉफी (coffee)"]
w = ["हाथियों के पेड़ (Elephant tress)","कैक्टस (Cactus)"]
r = s + ["रेगिस्तान गेंदा (Desert Marigold)"]
while(True):
    
    a = input("वर्तमान मौसम सबमिट करें और : 1.गर्मियों \t 2.बरसात \t 3.सर्दियों\n")
    if a == "1":
        print("गर्मी में उगाई फसलें : \n")
        random.shuffle(s)
        for i in s:
            print(i)
        import hindi.fer_hindi
        break
    elif a == "2":
        print("बरसात में उगाई फसलें : \n")
        random.shuffle(r)
        for i in r:
            print(i)
        import hindi.fer_hindi
        break
    elif a == "3":
        print("सर्दी में उगाई फसलें : \n")
        random.shuffle(w)
        for i in w:
            print(i)
        import hindi.fer_hindi
        break
    else:
        print("अमांय पसंद से बाहर निकले *** फिर कोशिश करो>>")
          
