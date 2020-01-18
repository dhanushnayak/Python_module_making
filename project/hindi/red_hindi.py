import wehin
del wehin
import random
s = ["गेहूं (Wheat)","मक्का (Maize)","रागी (Ragi)","तिलहन (Oilseeds)","बाजरा (Millets)","आम (Mango)"]
w = ["चावल (Rice)","रागी (Ragi)","गेहूं (Wheat)","आम (Mango)"]
r = w + ["गन्ना (Sugercane)","मूंगफली (Groundnets)"]
while(True):
    
    a = input("वर्तमान मौसम सबमिट करें : 1.गर्मियों \t 2.बरसात \t 3.सर्दियों\n")
    if a == "1":
        print("गर्मी में उगाई गई फसल : \n")
        random.shuffle(s)
        for i in s:
            print(i)
        import hindi.fer_hindi
        break
    elif a == "2":
        print("बरसात में उगाई गई फसल : \n")
        random.shuffle(r)
        for i in r:
            print(i)
        import hindi.fer_hindi
        break
    elif a == "3":
        print("सर्दियों में उगाई गई फसल : \n")
        random.shuffle(w)
        for i in w:
            print(i)
        import hindi.fer_hindi
        break
    else:
        print("अमांय पसंद से बाहर निकले *** फिर कोशिश करो>>")
          
