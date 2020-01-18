import wehin
del wehin
import random
s = ["कपास (Cotton)","चावल (Rice)","गेहूं (Wheat)","बाजरा (Bajra)","जूट (Jute)","तंबाकू (Tobacco)","हरा ग्राम (Green gram)"]
w = ["चावल (Rice)","जूट (Jute)","गेहूं (Wheat)","छोला (Chickpea)"]
r = ["कपास (Cotton)","चावल (Rice)","गेहूं (Wheat)","बाजरा (Bajra)","जूट (Jute)","तंबाकू (Tobacco)","हरा ग्राम (Green gram)","छोला (Chickpea)"]
while(True):
    
    a = input("वर्तमान मौसम सबमिट करें : 1.गर्मियों \t 2.बरसात \t 3.सर्दियों\n")
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
         print("अमांय पसंद से बाहर निकले ***फिर कोशिश करो>>")
