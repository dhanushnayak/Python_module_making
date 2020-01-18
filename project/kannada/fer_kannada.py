class Soil:
    def __init__(fer,org,inorg):
        fer.org = org
        fer.inorg = inorg
    def organic(fer):
        print("ಸಾವಯವ ಕೃಷಿ ಸಾಧಿಸಲು ನೀವು ಬಳಸಬಹುದು : \n" + fer.org)
        print(">>>>>>>>>>ಧನ್ಯವಾದ<<<<<<<<<<")
    def inorganic(fer):
        print("ಕೆಳಗಿನ ಕೀಟನಾಶಕವನ್ನು ನೀವು ರಾಸಾಯನಿಕ ರಚನೆಗೆ ಬಳಸಬಹುದು : \n" + fer.inorg)
        print(">>>>>>>>>>ಧನ್ಯವಾದ<<<<<<<<<<")

s = Soil(" ಮೀನು ಎಮಲ್ಷನ್ (Fish emulsion : 9% N, 0% P, 0% K) \n ಹತ್ತಿ ಬೀಜದ ಊಟ (Cotton seed meal : 6% N, 3% P, 1% K )\n ಕಾರ್ನ್ ಅಂಟು ಊಟ (Corn gluten meal  :0.5% N, 0.5% P, 1% K) \n ಕಡಲಕಳೆಗಳು (Seaweed : 1% N, 2% P, 5% K )\n ಹಸು ಗೊಬ್ಬರ (Cow manure : 2.5% N, 1% P, 1.5% K )\n ಚಿಕನ್ ಗೊಬ್ಬರ (ಕೋಳಿ) (Chicken manure (poultry) : 3.5% N, 1.5% P, 1.5% K )\n ಗ್ರೀನ್ಲ್ಯಾಂಡ್ (GREENSAND : 1%N,1%P,5%K )\n ಕಾಂಪೋಸ್ಟ್ (Compost : 2%N,1.5%P,1.5%K )\n ಸೋಯಾ ಊಟ (Soybean meal) : 3%N,0.5%P,2.5%K \nರಕ್ತದ ಊಟ ( Blood meal : 12%N,1.5%P,0.5%K )\n ಮೀನು ಊಟ ( Fish meal : 10% N, 5% P, 4% K )", "ಏಸ್ಫೇಟ್ (Acephate (C)) \n ಅಲಾಕ್ಲೋರ್ (Alachlor (B2)) \  n ಅಟ್ರಾಜೈನ್  (Atrazine (c))\n ಬೆನೊಮಿಲ್ (Benomyl (C)) \n ಬೈಫೆಂಟ್ರಿನ್ (Bifenthrin (C)) \n ಕ್ಯಾಪ್ಟನ್ (Captan (B2)) \n ಕ್ಲೋರೊಥಲೋನಿಲ್ (Chlorothalonil (B2)) \n ಸೈಪರ್ಮೆಥರಿನ್ (Cypermethrin (C)) \n ಡಿಕ್ಲೋರೊವೊಸ್ (Dichlorvos (C)) \n ಡಿಕ್ಲೊಫೊಪ್-ಮೀಥೈಲ್ (Diclofop-Methyl (C)) \n ಡಿಕೊಫೊಲ್ (Dicofol (C)) \n ಮನ್ಕೊಜೆಬ್ (Mancozeb (B2)) \n ಮೆಥೊಮಿಲ್ (Methomyl (C)) \n ಮೆಟಾಲಾಕ್ಲರ್ (Metolachlor (C)) \n ಆಕ್ಸಾಡಿಯಾಜಾನ್ (Oxadiazon (C)) \n ಆಕ್ಸಿಫ್ಲುವೊರ್ಫೆನ್ (Oxyflourfen (C)) \n ಪೆರ್ಮೆಥ್ರಿನ್ (Permethrin (C)) \n ಫಾಸ್ಫಮಿಡನ್ (Phosphamidon (C)) \n ಪ್ರೊಪಿಕೊನಜೋಲ್ (Propiconazole (C)) \n ಪ್ರೊಪೋಕ್ಸೂರ್ (propoxur (B2)) \n ಥಿಯೊಡಿಕಾರ್ಬ್ (Thiodicarb (C)) \n ಥಿಯೋಫನೇಟ್ ಮೀಥೈಲ್ (Thiophanate Methyl (C)) \n ಟ್ರೈಡಿಮ್ಫೊನ್  (Triadimefon (C)) \n ಟ್ರೈಫ್ಲುರಾಲಿನ್ (Trifluralin (C))")
while(True):
    p = input("ಬೆಳೆ ಅನುಷ್ಠಾನದ ವಿಧ : \t 1.ಸಾವಯವ ಕೃಷಿ \t 2.ರಾಸಾಯನಿಕ ಕೃಷಿ \n ********* ಆಯ್ಕೆಯನ್ನು ಸಲ್ಲಿಸಿ ********* \n")
    if p == '1':
        s.organic()
        break
    elif p == '2':
        s.inorganic()
        break
    else:
        print("ನಿರ್ಗಮನ *** ದಯವಿಟ್ಟು ಪುನಃ ಪ್ರಯತ್ನಿಸಿ>>>")
