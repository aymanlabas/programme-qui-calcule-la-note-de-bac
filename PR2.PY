math= float(input("math n: "))
svt= float(input("svt n: "))
pc= float(input("pc n: "))
philo= float(input("philo n: "))
english= float(input("english n: "))

Sm= math*7
Ss= svt*7
sP= pc*5
sph= philo*2
se= english*2
les_ntt= Sm+Ss+sP+sph+se
not_national=les_ntt/23

print(f"la not total de matier math {Sm} ")
print(f"la not total de matier svt: {Ss} ")
print(f"la not total de matier pc: {sP} ")
print(f"la not total de matier philo: {sph}")
print(f"la not total english: {se} ")
print(f"la not total:{les_ntt} ")
print(f"la note national: {not_national}")

not_rg=float(input("la not regional: "))
not_cc=float(input("la not cc: "))
ngb = not_national*0.50+not_rg*0.25+not_cc*0.25
print(f"la not general de l'exam bac 2023: {ngb}")
if ngb == 10 and ngb < 12:
    print("felicitation vous avez réussi avec un mentions: passable ")
elif  ngb >= 12 and ngb < 14:
    print("felicitation vous avez réussi avec un mentions: assez bien ")
elif ngb >= 14 and ngb < 16:
    print("felicitation vous avez réussi avec un mentions:  bien ")
elif ngb > 16:
    print("felicitation vous avez réussi avec un mentions: tres bien ")
