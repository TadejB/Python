dnk_zapis = open("dnk.txt", "r").read()

ziga = {
    "spol": "moski",
    "rasa": "belec",
    "barva_las": "oranzna",
    "barva_oci": "rjava",
    "oblika_obraza": "okrogla"
}

matej = {
    "spol": "moski",
    "rasa": "belec",
    "barva_las": "crna",
    "barva_oci": "modra",
    "oblika_obraza": "ovalna"
}

miha = {
    "spol": "moski",
    "rasa": "belec",
    "barva_las": "rjava",
    "barva_oci": "zelena",
    "oblika_obraza": "kvadratna"
}



crna  = "CCAGCAATCGC"
rjava = "GCCAGTGCCG"
korencek = "TTAGCTATCGC"


kvadrat = "GCCACGG"
okrogel = "ACCACAA"
ovalen = "AGGCCTCA"


modra = "TTGTGGTGGC"
zelena = "GGGAGGTGGC"
rjave_oci = "AAGTAGTGAC"


moski = "TGCAGGAACTTC"
zenska = "TGAAGGACCTTC"

belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

result_list = []

dnk_zapis.find(crna)


if dnk_zapis.find(crna) > 0:
    result_list.append(crna)
elif dnk_zapis.find(rjava) > 0:
    result_list.append(rjava)
elif dnk_zapis.find(korencek) > 0:
    result_list.append(korencek)

if dnk_zapis.find(kvadrat) > 0:
    result_list.append(kvadrat)
elif dnk_zapis.find(okrogel) > 0:
    result_list.append(okrogel)
elif dnk_zapis.find(ovalen) > 0:
    result_list.append(ovalen)

if dnk_zapis.find(modra) > 0:
    result_list.append(modra)
elif dnk_zapis.find(zelena) > 0:
    result_list.append(zelena)
elif dnk_zapis.find(rjave_oci) > 0:
    result_list.append(rjave_oci)

if dnk_zapis.find(moski) > 0:
    result_list.append(moski)
elif dnk_zapis.find(zenska) > 0:
    result_list.append(zenska)

if dnk_zapis.find(belec) > 0:
    result_list.append(belec)
elif dnk_zapis.find(crnec) > 0:
    result_list.append(crnec)
elif dnk_zapis.find(azijec) > 0:
    result_list.append(azijec)

print result_list

if result_list[3] == ziga["spol"] and result_list[4] == ziga["rasa"] and result_list[0] == ziga["barva_las"] \
        and result_list[2] == ziga["barva_oci"] and result_list[1] == ziga["oblika_obraza"]:
    print "ziga did it"

elif result_list[3] == matej["spol"] and result_list[4] == matej["rasa"] and result_list[0] == matej["barva_las"]\
        and result_list[2] == matej["barva_oci"] and result_list[1] == matej["oblika_obraza"]:
    print "matej did it"
else:
    print "miha did it"