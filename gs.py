
# coding: utf-8

man = ["Inuyasha", "Naruto", "Shinji-kun", "Conan", "Luffy"]
woman = ['Madoka', 'Kagome', 'AyanamiRei', 'Nyaruko', 'Mikoto']

manList = {'Inuyasha': ['Nyaruko', 'Ayanamirei', 'Mikoto', 'Kagome', 'Madoka'],
           'Naruto': ['AyanamiRei', 'Mikoto', 'Nyaruko', 'Kagome', 'Madoka'],
           'Shinji-kun': ['AyanamiRei', 'Madoka', 'Kagome', 'Nyaruko', 'Mikoto'],
           'Conan': ['AyanamiRei', 'Nyaruko', 'Madoka', 'Mikoto', 'Kagome'],
           'Luffy': ['Nyaruko', 'Mikoto', 'AyanamiRei', 'Kagome', 'Madoka'],
           }
womanList = {'Madoka': ['Luffy', 'Conan', 'Inuyasha', 'Shinji-kun', 'Naruto'],
             'Kagome': ['Shinji-kun', 'Naruto', 'Conan', 'Luffy', 'Inuyasha'],
             'AyanamiRei': ['Naruto', 'Inuyasha', 'Luffy', 'Conan', 'Shinji-kun'],
             'Nyaruko': ['Inuyasha', 'Naruto', 'Shinji-kun', 'Conan', 'Luffy'],
             'Mikoto': ['Naruto', 'Shinji-kun', 'Inuyasha', 'Luffy', 'Conan'],
             }
manStatus = {}
womanStatus = {}

for M in man:
    manStatus[M] = None
for W in woman:
    womanStatus[W] = None

#print(manStatus,womanStatus)

def gocon():
    for m in man:
        if manStatus[m] == None:
            w = manList[m][0]
            del manList[m][0]
            if womanStatus[w] == None:
                womanStatus[w] = m
                manStatus[m] = w
            elif womanList[w].index(m) <= womanList[w].index(womanStatus[w]):
                manStatus[womanStatus[w]] = None
                womanStatus[w] = m
                manStatus[m] = w
    for m in man:
        if manStatus[m] == None:
            gocon()
    return True



gocon()
print("-結果発表-")
print(manStatus)
