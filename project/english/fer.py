
class Soil:
    def __init__(fer,org,inorg):
        fer.org = org
        fer.inorg = inorg
    def organic(fer):
        print("To achieve ORGANIC you can use : \n" + fer.org)
        print(">>>>>>>>>>ENDED<<<<<<<<<<")

    def inorganic(fer):
        print("The PESTICDES you can use : \n" + fer.inorg)
        print(">>>>>>>>>>ENDED<<<<<<<<<<")
        

s = Soil(" Fish emulsion : 9% N, 0% P, 0% K \n Cotton seed meal : 6% N, 3% P, 1% K \n Corn gluten meal :0.5% N, 0.5% P, 1% K \n Seaweed : 1% N, 2% P, 5% K \n Cow manure : 2.5% N, 1% P, 1.5% K \n Chicken manure (poultry) : 3.5% N, 1.5% P, 1.5% K \n GREENSAND : 1%N,1%P,5%K \n Compost : 2%N,1.5%P,1.5%K \n Soybean meal : 3%N,0.5%P,2.5%K \n Blood meal : 12%N,1.5%P,0.5%K \n Fish meal : 10% N, 5% P, 4% K ", "Acephate (C) \n Alachlor (B2) \n Atrazine (C) \n Benomyl (C) \n Bifenthrin (C) \n Captan (B2) \n Chlorothalonil (B2) \n Cypermethrin (C) \n Dichlorvos (C) \n Diclofop-Methyl (C) \n Dicofol (C) \n Mancozeb (B2) \n Methomyl (C) \n Metolachlor (C) \n Oxadiazon (C) \n Oxyflourfen (C) \n Permethrin (C) \n Phosphamidon (C) \n Propiconazole (C) \n Propoxur (B2) \n Thiodicarb (C) \n Thiophanate Methyl (C) \n Triadimefon (C) \n Trifluralin (C)")

while(True):
    
    p = input("Type of implemention of Crop : \t 1.ORGANIC FARMING \t 2.CHEMICAL FARMING \n *********Submit Option ********* \n")
    if p == '1':
        s.organic()
        break
    elif p == '2':
        s.inorganic()
        break
    else:
        print("Try Again >>>")
