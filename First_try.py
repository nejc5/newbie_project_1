import time
name = input("Kako ti je ime??\n")
print(f"Živjo {name}")
while True:
    number = int(input(f"Kako si kaj danes {name}, na lestvici od 1-10?\n"))
    nonsense = (f"Da si oceniš svoj dan z {number}/10, pomeni, da")
    if number < 4 and number > 0:
        print(f"{nonsense} si danes zelo žalostna. Upam, da boš kmalu bolje.")
        break
    elif number < 8 and number > 0:
        print(f"{nonsense} nisi žalostna, pa tudi ne najbolj vesela.")
        break
    elif number < 11 and number > 0:
        print(f"{nonsense}, imaš danes zelo vesel dan. Kar tako naprej!")
        break
    else:
        print(f"Opazil sem, da nisi zbral/a številke med 1 in 10, tako, da te prosim, da še enkrat odgovarjaš.")
        continue
time.sleep(1.5)
print(f"Za nasledno stvar, ki jo bova delala, boš rabil/a odgovarjati z odgovori DA ali NE.")
DA_answer = "DA"
NE_answer = "NE"
while True:
    answer = input(f"Ali si za?(DA/NE)\n").upper()
    if answer == DA_answer or answer == NE_answer:
        break
    else:
        print(f"Verjetno je prišlo do napake pri tipkanju, saj niste odgovorili z DA ali NE. Prosim, da še enkrat odgovarjate.")
if answer == NE_answer:
    exit()
print(f"Najprej si boš rabil/a zamisliti katero koli barvo. Ta barva rabi biti v mavrici.\nSedaj ti bom postavljal vprašanja, na katera odgovarji z DA ali NE.")
print(f"Če si idiot, kot jaz in ne veš katere barvo so v njej, je tukaj plonkec\nBarve: Rdeča, roza, vijolična, modra, zelena, rumena in oranžna.\nDo se daj bi se že rabil odločiti, toda ti tam še 10s sekund, do 1. vprrašanja.")
time.sleep(10)

answer_1 = input(f"1.) ALi je barva, ki si jo zbral/a, ena od treh primarnih barvami.( DA or NE )\n").upper()
answer_2 = input(f"2.) Ali je barva, ki si jo izbrala, mešanica rumene in modre?\n").upper()
answer_3 = input(f"3.) Ali so Nejčeve oči iste barve, kot barva, ki si jih zbral/a?\n").upper()
answer_4 = input(f"4.) Ali je ta barva sekundarna barva?\n").upper()
answer_5 = input(f"5.) Je to ena od dveh barv, ki imata lasnost, da če se zmešata med seboj, postaneta oranžna?\n").upper()
answer_6 = input(f"6.) Ali je to barva, ki je sinonim za visoko plemstvo?\n").upper()
answer_7 = input(f"7.) eAli je to barva, ki je iste barve kot barva človeške krvi?\n").upper()
List = []

for x in range(1, 8):
    if vars()[f"answer_{x}"] == DA_answer:
        List.append(f"{x}")

if "1" in List:
    if "3" in List:
        print("Tvoja izbrana barva je Modra!")
    elif "7" in List:
        print("Tvoja izbrana barva je Rdeča!")
    else:
        print("Tvoja izbrana barva je Rumena!")
elif "4" in List:
    if "6" in List:
        print("Tvoja izbrana številka je Vijolična!")
    else:
        print("Tvoja izbrana barva je Roza!")
elif "2" in List:
    print("Tvoja izbrana barva je Zelena!")
else:
    print("Tvoja izbrana barva je Oranžna!")