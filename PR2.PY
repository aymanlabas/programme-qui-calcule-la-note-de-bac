def fsvt():
    math = float(input("Note du math: "))
    svt = float(input("Note du SVT: "))
    pc = float(input("Note du pc: "))
    philo = float(input("Note du philo: "))
    english = float(input("Note d'anglais: "))

    Sm = math * 7
    Ss = svt * 7
    sP = pc * 5
    sph = philo * 2
    se = english * 2
    nts_nat = Sm + Ss + sP + sph + se
    somme_natio = nts_nat / 23

    print(f"la not total de matier math {Sm} ")
    print(f"la not total de matier svt: {Ss} ")
    print(f"la not total de matier pc: {sP} ")
    print(f"la not total de matier philo: {sph}")
    print(f"la not total english: {se} ")
    print(f"la not total:{nts_nat} ")
    print(f"la note national: {somme_natio}")

    nt_rg = float(input("la note géneral de l'examen régional: "))
    if nt_rg == 00 or nt_rg == 0 :
        nar = float(input("Saisir la note arabe: "))
        nfr = float(input("Saisir la note francais: "))
        nhg = float(input("Saisir la note histoire geo: "))
        nei = float(input("Saisir la note education islamique: "))
        ar = nar * 2
        fr = nfr * 4
        hg = nhg * 2
        ei = nei * 2
        note_reg = (ar + fr + hg +ei) / 10
        print(f"la note génerale du regional {note_reg}")
        not_cc = float(input("la not cc: "))
        ngb = somme_natio * 0.50 + note_reg * 0.25 + not_cc * 0.25
        print(f"la not general de l'exam bac 2023: {ngb}")
        if ngb == 10 and ngb < 12:
            print("felicitation vous avez réussi avec un mentions: passable ")
        elif  ngb >= 12 and ngb < 14:
            print("felicitation vous avez réussi avec un mentions: assez bien ")
        elif ngb >= 14 and ngb < 16:
            print("felicitation vous avez réussi avec un mentions: bien")
        elif ngb > 16:
            print("felicitation vous avez réussi avec un mentions: très bien")
    else :
        not_cc = float(input("la not cc: "))
        ngb = somme_natio * 0.50 + nt_rg * 0.25 + not_cc * 0.25
        print(f"la not general de l'exam bac 2023: {ngb}")

        if ngb == 10 and ngb < 12:
            print("felicitation vous avez réussi avec un mentions: passable ")
        elif  ngb >= 12 and ngb < 14:
            print("felicitation vous avez réussi avec un mentions: assez bien ")
        elif ngb >= 14 and ngb < 16:
            print("felicitation vous avez réussi avec un mentions: bien")
        elif ngb > 16:
            print("felicitation vous avez réussi avec un mentions: tres bien")

def fsm():
    math = float(input("Note du math: "))
    svt = float(input("Note du SVT: "))
    pc = float(input("Note du pc: "))
    philo = float(input("Note du philo: "))
    english = float(input("Note d'anglais: "))

    Sm = math * 9
    Ss = svt * 3
    sP = pc * 7
    sph = philo * 2
    se = english * 2
    nts_nat = Sm + Ss + sP + sph + se
    somme_natio = nts_nat / 23

    print(f"la not total de matier math {Sm} ")
    print(f"la not total de matier svt: {Ss} ")
    print(f"la not total de matier pc: {sP} ")
    print(f"la not total de matier philo: {sph}")
    print(f"la not total english: {se} ")
    print(f"la not total:{nts_nat} ")
    print(f"la note national: {somme_natio}")

    nt_rg = float(input("la note géneral de l'examen régional: "))
    if nt_rg == 00 or nt_rg == 0 :
        nar = float(input("Saisir la note arabe: "))
        nfr = float(input("Saisir la note francais: "))
        nhg = float(input("Saisir la note histoire geo: "))
        nei = float(input("Saisir la note education islamique: "))
        ar = nar * 2
        fr = nfr * 4
        hg = nhg * 2
        ei = nei * 2
        note_reg = (ar + fr + hg +ei) / 10
        print(f"la note génerale du regional {note_reg}")
        not_cc = float(input("la not cc: "))
        ngb = somme_natio * 0.50 + note_reg * 0.25 + not_cc * 0.25
        print(f"la not general de l'exam bac 2023: {ngb}")
        if ngb == 10 and ngb < 12:
            print("felicitation vous avez réussi avec un mentions: passable ")
        elif  ngb >= 12 and ngb < 14:
            print("felicitation vous avez réussi avec un mentions: assez bien ")
        elif ngb >= 14 and ngb < 16:
            print("felicitation vous avez réussi avec un mentions: bien")
        elif ngb > 16:
            print("felicitation vous avez réussi avec un mentions: très bien")
    else :
        not_cc = float(input("la not cc: "))
        ngb = somme_natio * 0.50 + nt_rg * 0.25 + not_cc * 0.25
        print(f"la not general de l'exam bac 2023: {ngb}")

        if ngb == 10 and ngb < 12:
            print("felicitation vous avez réussi avec un mentions: passable ")
        elif  ngb >= 12 and ngb < 14:
            print("felicitation vous avez réussi avec un mentions: assez bien ")
        elif ngb >= 14 and ngb < 16:
            print("felicitation vous avez réussi avec un mentions: bien")
        elif ngb > 16:
            print("felicitation vous avez réussi avec un mentions: tres bien")

def fpc():
    math = float(input("Note du math: "))
    svt = float(input("Note du SVT: "))
    pc = float(input("Note du pc: "))
    philo = float(input("Note du philo: "))
    english = float(input("Note d'anglais: "))

    Sm = math * 7
    Ss = svt * 5
    sP = pc * 7
    sph = philo * 2
    se = english * 2
    nts_nat = Sm + Ss + sP + sph + se
    somme_natio = nts_nat / 23

    print(f"la not total de matier math {Sm} ")
    print(f"la not total de matier svt: {Ss} ")
    print(f"la not total de matier pc: {sP} ")
    print(f"la not total de matier philo: {sph}")
    print(f"la not total english: {se} ")
    print(f"la not total:{nts_nat} ")
    print(f"la note national: {somme_natio}")

    nt_rg = float(input("la note géneral de l'examen régional: "))
    if nt_rg == 00 or nt_rg == 0 :
        nar = float(input("Saisir la note arabe: "))
        nfr = float(input("Saisir la note francais: "))
        nhg = float(input("Saisir la note histoire geo: "))
        nei = float(input("Saisir la note education islamique: "))
        ar = nar * 2
        fr = nfr * 4
        hg = nhg * 2
        ei = nei * 2
        note_reg = (ar + fr + hg +ei) / 10
        print(f"la note génerale du regional {note_reg}")
        not_cc = float(input("la not cc: "))
        ngb = somme_natio * 0.50 + note_reg * 0.25 + not_cc * 0.25
        print(f"la not general de l'exam bac 2023: {ngb}")
        if ngb == 10 and ngb < 12:
            print("felicitation vous avez réussi avec un mentions: passable ")
        elif  ngb >= 12 and ngb < 14:
            print("felicitation vous avez réussi avec un mentions: assez bien ")
        elif ngb >= 14 and ngb < 16:
            print("felicitation vous avez réussi avec un mentions: bien")
        elif ngb > 16:
            print("felicitation vous avez réussi avec un mentions: très bien")
    else :
        not_cc = float(input("la not cc: "))
        ngb = somme_natio * 0.50 + nt_rg * 0.25 + not_cc * 0.25
        print(f"la not general de l'exam bac 2023: {ngb}")

        if ngb == 10 and ngb < 12:
            print("felicitation vous avez réussi avec un mentions: passable ")
        elif  ngb >= 12 and ngb < 14:
            print("felicitation vous avez réussi avec un mentions: assez bien ")
        elif ngb >= 14 and ngb < 16:
            print("felicitation vous avez réussi avec un mentions: bien")
        elif ngb > 16:
            print("felicitation vous avez réussi avec un mentions: tres bien")

def main():
    print("Ce programme sert à calculer la note génerale de l'examen national, il y'a 3 filières: \n Sciences mathématiques \n Sciences physiques \n Sciences de la vie et terre")
    print("sm : Sciences mathématiques\npc : Sciences physiques chimie\nsvt : Sciences de la vie et terre")
    f = input("Saisir votre filière:")

    if f == "sm" or f == "SM" or f == "Sm" :
        fsm()
    elif f == "pc" or f =="pc" or f =="PC":
        fpc()
    elif f == "svt" or f =="Svt" or f =="Svt":
        fsvt()
    else:
        print("Cette filière est introuvable, veuillez saisir l'une des existants: \n ----------------------------------------------------------------")
        main()

main()