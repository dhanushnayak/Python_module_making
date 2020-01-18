def nwest():
    print("*****The Zonal contains maximum amount of DESERT SOIL*****")
    import english.desert
def north():
    print("*****The Zonal contains maximum amount of ALLUVIAL SOIL*****")
    import english.alluvial
def neast():
    print("*****The Zonal contains maximum amount of RED SOIL*****")
    import english.red
def west():
    print("*****The Zonal contains maximum amount of BLACK SOIL*****")
    import english.black
def central():
    print("*****The Zonal contains maximum amount of BLACK SOIL*****")
    import english.black
def east():
    print("*****The Zonal contains maximum amount of RED SOIL*****")
    import english.red
def swest():
    print("*****The Zonal contains maximum amount of RED SOIL*****")
    import english.red
def south():
    print("*****The Zonal contains maximum amount of RED SOIL*****")
    import english.red
def seast():
    print("*****The Zonal contains maximum amount of ALLUVIAL SOIL*****")
    import english.alluvial
while(True):
    
    a = input("Select the State : \n1.Jammu and Kashmir\n2.Himachal Pradesh\n3.Punjab\n4.Uttarkand\n5.Uttar pradesh\n6.Haryana\n7.Rajasthan\n8.Assam\n9.Sikkim\n10.Nagaland\n11.Meghalaya\n12.Manipur\n13.Mizoram\n14.Tripura\n15.Arunachal Pradesh\n16.West bengal\n17.Madhya Pradesh\n18.Chhattisgarh\n19.Gujarat\n20.Goa\n21.Maharashtra\n22.Bihar\n23.Orissa\n24.Jharkhand\n25.Telangana\n26.Andhra Pradesh\n27.Karnataka\n28.Kerala\n29.Tamil Nadu\nSubmit your State option : \n")
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
        print(">> Wrong choice*** Try Again >>")
    
        
    
