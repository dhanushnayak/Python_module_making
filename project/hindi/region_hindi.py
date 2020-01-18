def nwest():
    print("*****जोनल रेगिस्तान मिट्टी की अधिकतम राशि शामिल*****")
    import hindi.desert_hindi
def north():
    print("*****जोनल में जलोढ़ मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.alluvial_hindi
def neast():
    print("*****जोनल में लाल मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.red_hindi
def west():
    print("*****जोनल में लाल मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.black_hindi
def central():
    print("*****जोनल में लाल मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.black_hindi
def east():
    print("*****जोनल में लाल मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.red_hindi
def swest():
    print("*****जोनल में लाल मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.red_hindi
def south():
    print("*****जोनल में लाल मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.red_hindi
def seast():
    print("*****जोनल में जलोढ़ मिट्टी की अधिकतम मात्रा होती है*****")
    import hindi.alluvial_hindi
   
while(True):
    
    a = input("राज्य का चयन करें (State) : \n1.जम्मू-कश्मीर (jammu kashmir)\n2.हिमाचल प्रदेश (Himachal Pradesh)\n3.पंजाब (Punjab)\n4.उत्तरकांड (Uttarkand)\n5.उत्तर प्रदेश (Uttar pradesh)\n6.हरियाणा (Haryana)\n7.राजस्थान (Rajasthan)\n8.असम (Assam)\n9.सिक्किम (Sikkim)\n10.नागालैंड (Nagaland)\n11.मेघालय (Meghalaya)\n12.मणिपुर (Manipur)\n13.मिजोरम (Mizoram)\n14.त्रिपुरा (Tripura)\n15.अरुणाचल प्रदेश (Arunachal Pradesh)\n16.West bengal\n17.मध् यप्रदेश (Madhya Pradesh)\n18.छत्तीसगढ़ (Chhattisgarh)\n19.गुजरात (Gujarat)\n20.गोवा (Goa)\n21.महाराष्ट्र (Maharashtra)\n22.बिहार (Bihar)\n23.उड़ीसा (Orissa)\n24.झारखंड (Jharkhand)\n25.तेलंगाना (Telangana)\n26.आंध्र प्रदेश (Andhra Pradesh)\n27.कर्नाटक (Karnataka)\n28.केरल (Kerala)\n29.तमिलनाडु (Tamil Nadu)\nअपना राज्य विकल्प सबमिट करें  : \n")
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
        print(">> गलत विकल्प*** फिर कोशिश करो >>")
    
        
