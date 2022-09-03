# EXAMPLE-1
class animemcs:
    animetype = str("shonen")
    pass

    def showcard(self):
        return f"Name is {self.name} . Power is {self.pwr} . Anime he/her is in is {self.anime} . His/Her color is {self.color}"

    def __init__(self, mcname, mcpwr, mcanime, mccolor):
        self.name = mcname
        self.pwr = mcpwr
        self.anime = mcanime
        self.color = mccolor

    @property
    def email(self):
        return f"{self.name}@gmail.com"

    @email.setter
    def emailset(self, string):
        names = string.split('@')[0]
        self.name = names.split(".")[0]

    def __add__(self, other):
        return self.pwr + other.pwr


class animeants(animemcs):
    def printants(self):
        return f"Name is {self.name} . Power is {self.pwr} . Anime he/her is in is {self.anime}. His/Her color is {self.color}"


Naruto = animemcs("Naruto Uzumaki", 8, "Naruto Shippuden", "orange")=
Luffy = animemcs("Monkey D Luffy", 7, "One piece", "red")
CapedBaldy = animemcs("Saitama", 10, "One punch man", "yellow")
Deku = animemcs("Izuku Midoriya", 6, "My Hero Academia", "green")
AttackTitan = animemcs("Eren Yeager", 9.5, "Attack on Titan", "Brownish-Peach")
Ichigo = animemcs("IchigoKurosaki", 8, "Bleach", "black")
Kaguya = animeants("Kaguya Otsusuki", 9, "Naruto Shippuden", "White")

print(animeants)
# Naruto.name="Naruto Uzimaki"
# Naruto.pwr="8"
# Naruto.anime="Naruto Shippuden"

# Luffy.name="Monkey D Luffy"
# Luffy.pwr="7"
# Luffy.anime="One piece"

# CapedBaldy.name=("Saitama")
# CapedBaldy.pwr="10"
# CapedBaldy.anime="One punch Man"

# showmc=input("Naruto , Luffy or Saitama?\n")

# if  showmc=="Luffy" :
#   print(Luffy.showcard())

# elif showmc=="Naruto" :
#     print(Naruto.showcard())

# elif showmc=="Saitama" :
#     print(CapedBaldy.showcard())

# else :
#     print("Error , type again")


# #Multilevel Inheritance
# #Electronic device --> Pocket gadget --> Smartphone

# class ED:
#     circuit=1
#     directconnection=1
#     nonportable=1
#     electricity=1
#     technology=1
#     buttons=1


# class PG(ED):
#     circuit=1
#     electricity=1
#     battery=1
#     buttons=1
#     technology=1
#     portable=1

# class SM(PG , ED) :
#     circuit=1
#     electricity=1
#     battery=1
#     technology=1
#     screentouch=1
#     portable=1
#     wifi=1

# electronicdevice = ED()
# pocketgadget=PG()
# smartphone=SM()
