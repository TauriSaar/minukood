def paranda_komavead(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" kuid ", ", kuid ")
    lause = lause.replace(" vaid ", ", vaid ")
    print(lause)
    
lause = input("Pane oma tekst siia: ")
paranda_komavead(lause)