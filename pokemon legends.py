choosen=False
from random import *
from time import sleep


mode="normal"
print("Note:This game is still under developing. We will not add Ho-oh into the game becuase of a placeholder glitch. We may add it someday...... but only after we figure out a way to solve the bug.")
sleep(2)
sleep(1)
print("Warning: Using an unvalid move will softlock the game. Use moves displayed on the screen ONLY, and be sure to type every first letter of a word in UPPERCASE.")

sleep(1)

#print("In the stadium, the weather is always Tera Blaze, which automatically clears all status conditions every 3 rounds. All other buffs or debuffs will remain until the Pokemon with the buff or debuff faints.")
sleep(1)
print("Note:This is test version ver0.1, and is NOT what the real game(which will be released in the future) will look like.")
print("Downloading resources1/12")
sleep(0.2)
print("Downloading resources2/12")
sleep(0.3)
print("Downloading resources3/12")
sleep(0.2)
print("Downloading resources4/12")
sleep(0.4)
print("Downloading resources5/12")
sleep(0.6)
print("Downloading resources6/12")
sleep(0.3)
print("Downloading resources7/12")
sleep(0.5)
print("Downloading resources8/12")
sleep(0.7)
print("Downloading resources9/12")
sleep(1)
print("Downloading resources10/12")
sleep(0.2)
print("Downloading resources11/12")
sleep(0.4)
print("Download complete. Press return to start the game.")
x=input()
print("Ceiran:")
print("")
print("Welcome to the final battle of the Legend league.")
print("I am Ceiran, the founder of the league.")
print("You are going to use 2 Legendary Pokemon to beat Ayatsugi, the champion of the league.")
print("")
print("Ayatsugi:")
print("")

valid=0
while valid==0:
    print("Please, what is your name?")
    name=input()
    if name=="":
        print("Please choose a valid name.")
    elif name=="ceiran" or "Ceiran":
        valid=1
    elif name=="ayatsugi" or "Ayatsugi":
        print("I knew it. Someone is controlling you.")
    elif name=="gentaku" or "Gentaku":
        print("Do you want to get destroyed by the power of Ryumei???")
    elif name=="renko" or "Renko":
        print("...")
    elif name=="cat" or "dog" or "horse":
        print("Meooeigh!")
    else:
        print("Woah, woah! I wont want to fight the champion! Do it yourself!")
    
print("Ayatsugi:")
print("")
print("Wow, that's a great name,",name,"!")
print("Let us start the battle now.")
print("Please, choose 2 Pokemon. Type in lowercase only.")

#Defining Pokemons and their atrributes, actions and battle system
 
def battle(a,b,aname,bname):
     over=False
     while over==False:
         a.attack(a,b,aname)
         b.defend(b,a)
         b.oppatk(b,a,bname)
         a.defend(a,b)
         if a.hp<=0 or b.hp<=0:
             over=True
         if a.perish1!=None:
             a.perish1-=1
         if a.perish1==0:
             a.hp=0
         if b.perish1!=None:
             b.perish1-=1
         if b.perish1==0:
             b.hp=0
         print(f"{aname}: {a.hp}/{a.maxhp}HP")
         print(f"{bname}: {b.hp}/{b.maxhp}HP")
         if a.hp<=0 or b.hp<=0:
           over=True
     if b.hp<=0:
       print(f"{bname} has fainted" )
     
     if a.hp<=0:
       print("%s has fainted" % aname)
def battle2(a1,a2,b1,b2,a1_name,a2_name,b1_name,b2_name):
    print("Go! %s!" % a1_name)
    print(f"Champion Ayatsugi sent out {b1_name}!")
    sleep(1)
    battle(a1,b1,a1_name,b1_name)
    if not (a1.hp<=0 and b1.hp<=0):
        if a1.hp<=0:
            print("Go! %s!" % a2_name)
            battle(a2,b1,a2_name,b1_name)
            if a2.hp<=0:
                print("Your last Pokemon has fainted")
                sleep(1)
                print("The winner is Ayatsugi")
                print("YOU LOSE")
                lose()
            else:
                print(f"Champion Ayatsugi sent out {b2_name}!")
                battle(a2,b2,a2_name,b2_name)
                if a2.hp<=0:
                    print("Your last Pokemon has fainted")
                    sleep(1)
                    print("The winner is Ayatsugi")
                    print("YOU LOSE")
                    lose()
                else:
                    print(f"{b2_name} has fainted")
                    print("YOU WIN")
                    win()
        elif b1.hp<=0:
            print(f"Champion Ayatsugi sent out {b2_name}!")
            battle(a1,b2,a1_name,b2_name)
            if b2.hp<=0:
                print(f"{(b2_name)} has fainted")
                print("YOU WIN")
                win()
            else:
                print("Go! %s!" % a2_name)
                battle(a2,b2,a2_name,b2_name)
                if a2.hp<=0:
                    print("Your last Pokemon has fainted")
                    sleep(1)
                    print("The winner is Ayatsugi")
                    print("YOU LOSE")
                    lose()
                else:
                    print("f{(b2_name)} has fainted")
                    print("YOU WIN")
                    win()
    else:
        print("Go! %s!" % str(a2_name))
        print(f"Champion Ayatsugi sent out {str(b2_name)}")
        battle(a2,b2,a2_name,b2_name)
        if a2.hp<=0:
            print("Your last Pokemon has fainted")
            sleep(1)
            print("The winner is Ayatsugi")
            print("YOU LOSE")
            lose()
        else:
            print(f"{str(b2_name)} has fainted")
            print("YOU WIN")
            win()
def win():
    print("Ceiran:")
    print("")
    print("Congrajulations!")
    sleep(2)
    print("You are the new champion now.")
    sleep(2)
    print("I have seen too many of these recursions.")
    sleep(2)
    print(f"{name}, the same person...")
    sleep(2)
    print("Becoming champion again and again.")
    sleep(2)
    print("Maybe its just a trick of the light... I will never know.")
    sleep(2)
    print("Good luck then!")
    sleep(2)
    print(f"Hope we can meet again someday. I will always be waiting for you in the stadium, {name}.")
    sleep(1)
    print("Ayatsugi:")
    print("")
    print(f"Good job,{name}! Looks like you have beat all of my Pokemon.")
    sleep(2)
    print("You see, I know this isnt over.")
    sleep(2)
    print("As a champion who lived more than 300 years, I can see the flow of timelines.")
    sleep(2)
    print("We are just living in a reality made by sheer commands typed into the computer.")
    sleep(2)
    print("And the reality changes all the time. My lore, my personalities, my Pokemon...... ")
    sleep(2)
    print("They will all change someday.")
    sleep(2)
    print("And the worst part is, I wont even know it.")
    sleep(2)
    print("By that day, we will meet, and fight again.")
    sleep(2)
    print("I am trapped in a constantly changing flow of text.")
    sleep(2)
    print("Even though I see it, I cant do anything to it.")
    sleep(2)
    print("All i can do is maintain the stability of this world by to keep on fighting.")
    sleep(2)
    print(f"But you, {name}...")
    sleep(2)
    print("You are different.")
    sleep(2)
    print("Your will to change the course of this world...")
    sleep(2)
    print("I think I know the reason of a child possibly having that much power now.")
    sleep(2)
    print("There is someone controlling you do do all of this, isnt it?")
    sleep(2)
    print("Hey, you out there... If you really exist, be sure to come back.")
    sleep(2)
    print(f"See you on the next update, {name}! I am looking forward to it.")
    sleep(2)
    sleep(2)
    print("")
    print("YOU BEAT THE GAME!")
    print("Be sure to come back on ver0.2!")
def lose():
    print("Ceiran:")
    print("")
    sleep(2)
    print("What a pity.")
    print("You tried to choose the best Pokemon, but still lost.")
    print("Well, good luck next time then! See you!")
    sleep(2)
    sleep(2)
    print("GAME OVER")
    print("Be sure to win next try!")

class Pokemon:
    def __init__(self,maxhp,hp,atk,defense,move1,move2,move3,move4,type1,type2,move1_pw,move2_pw,move3_pw,move4_pw,move1_buff,move2_buff,move3_buff,move4_buff):
        self.maxhp=maxhp
        self.hp=hp
        self.atk=atk
        self.defense=defense

        self.move1=move1
        self.move2=move2
        self.move3=move3
        self.move4=move4
        self.moveset=[move1,move2,move3,move4]
        self.type1=type1
        self.type2=type2
        self.move1_pw=move1_pw
        self.move2_pw=move2_pw
        self.move3_pw=move3_pw
        self.move4_pw=move4_pw
        self.move1_buff=move1_buff
        self.move2_buff=move2_buff
        self.move3_buff=move3_buff
        self.move4_buff=move4_buff
        self.res1=False
        self.freeze1=False
        self.para1=False
        self.perish1=None
        self.sleep1=False

    def attack(self,opp,name,t):
        if self.freeze1==False:
            if self.para1==False or (self.para1==True and randint(1,2)==2):
                print("Usable moves:")
                sleep(0.5)
                print(self.move1)
                print(self.move2)
                print(self.move3)
                print(self.move4)
                sleep(0.5)
                print("Please choose a move to use. Be sure to type every first letter of a word in uppercase.")
                move=input()
                if move in self.moveset:
                    print("%s used %s!" %(t, move))
                    if move==self.move1:
                        global damage
                        damage=self.move1_pw*self.atk
                        if randint(1,1000) in range(600,750):
                            damage*=1.5
                            print("Critical hit! Damage increased this round")
                        if self.move1_buff=="poison" or "flame" :
                            opp.res(opp)
                        if self.move1_buff=="freeze"  or "sleep":
                            opp.freeze(opp)
                        if self.move1_buff=="para":
                            opp.para(opp)
                        if self.move1_buff=="pwup":
                            self.atk+=20
                            self.defense+=20
                            self.move1_pw+=10
                            self.move2_pw+=10
                            self.move3_pw+=10
                            self.move4_pw+=10
                            print("Stats increased due to move effects")
                        if self.move1_buff=="pwdn":
                            opp.atk-=20
                            opp.defense-=20
                            print("Opponent's Pokemon stats decreased")
                        if self.move1_buff=="restore":
                            self.hp+=(self.maxhp-self.hp)/2
                            print("HP restored. %s HP left" % self.hp)
                        validmove=1
                            #break
                    elif move==self.move2:
                        
                        damage=self.move2_pw*self.atk
                        if randint(1,1000) in range(600,750):
                            damage*=1.5
                            print("Critical hit! Damage increased this round")
                        if self.move2_buff=="poison" or "flame" :
                            opp.res(opp)
                        if self.move2_buff=="freeze"  or "sleep":
                            opp.freeze(opp)
                        if self.move2_buff=="para":
                            opp.para(opp)
                        if self.move2_buff=="pwup":
                            self.atk+=20
                            self.defense+=20
                            self.move1_pw+=10
                            self.move2_pw+=10
                            self.move3_pw+=10
                            self.move4_pw+=10
                            print("Stats increased due to move effects")
                        if self.move2_buff=="pwdn":
                            opp.atk-=20
                            opp.defense-=20
                            print("Opponent's Pokemon stats decreased")
                        if self.move2_buff=="restore":
                            self.hp+=(self.maxhp-self.hp)/2
                            print("HP restored. %s HP left" % self.hp)
                        if self.move2_buff=="deep sleep":
                            print("The opposing Pokemon has gone into a sleep so deep, it is never waking up")
                            opp.deep_sleep()
                            self.move2="empty move"
                            self.move2_pw=0
                            self.move2_buff=None
                        validmove=1
                    #reak
                    elif move==self.move3:
                        
                        damage=self.move3_pw*self.atk
                        if randint(1,1000) in range(600,750):
                            damage*=1.5
                            print("Critical hit! Damage increased this round")
                        if self.move3_buff=="poison" or "flame" :
                            opp.res(opp)
                        if self.move3_buff=="freeze"  or "sleep":
                            opp.freeze(opp)
                        if self.move3_buff=="para":
                            opp.para(opp)
                        if self.move3_buff=="pwup":
                            self.atk+=20
                            self.defense+=20
                            self.move1_pw+=10
                            self.move2_pw+=10
                            self.move3_pw+=10
                            self.move4_pw+=10
                            print("Stats increased due to move effects")
                        if self.move3_buff=="restore":
                            self.hp+=(self.maxhp-self.hp)/3
                            print("HP restored. %s HP left" % self.hp)
                        if self.move3_buff=="pwdn":
                            opp.atk-=20
                            opp.defense-=20
                            print("Opponent's Pokemon stats decreased")
                        if self.move3_buff=="complete restore":
                            self.hp+=(self.maxhp-self.hp)/2
                            if self.res1==True:
                                self.res1=False
                            if self.freeze1==True:
                                self.freeze1=False
                            if self.para1==True:
                                self.para1=False
                            if self.perish1!=None:
                                self.perish1=None
                            print("All statuses cleared, including perish.")
                            print("HP restored. %s HP left" % self.hp)
                            self.move3="empty move"
                            self.move3_pw=0
                            self.move3_buff=None
                        #break   
                        validmove=1
                    else:
                            
                            damage=self.move1_pw*self.atk
                            if randint(1,1000) in range(600,750):
                                damage*=1.5
                                print("Critical hit! Damage increased this round")
                            if self.move4_buff=="poison" or "flame" :
                                opp.res(opp)
                            if self.move4_buff=="freeze"  or "sleep":
                                opp.freeze(opp)
                            if self.move4_buff=="para":
                                opp.para(opp)
                            if self.move4_buff=="pwup":
                                self.atk+=20
                                self.defense+=20
                                self.move1_pw+=10
                                self.move2_pw+=10
                                self.move3_pw+=10
                                self.move4_pw+=10
                                print("Stats increased due to move effects")
                            if self.move4_buff=="restore":
                                self.hp+=(self.maxhp-self.hp)/2
                                print("HP restored. %s HP left" % self.hp)
                            if self.move4_buff=="perish":
                                self.perish(self,opp)
                            if self.move4_buff=="pwdn":
                                opp.atk-=20
                                opp.defense-=20
                                print("Opponent's Pokemon stats decreased")
                            validmove=1
                            #break
                else:        
                            print("%s has been freezed, paralysed or is sleeping, and cannot use a move." % t)
                            validmove=1
                           # break
            else:
                    print("No data found for this move. Please choose another one.")
    def oppatk(self,opp,name,t):
        if self.sleep1==False or randint(1,10)==6:
            if self.freeze1==False:
                if self.para1==False or (self.para1==True and randint(1,2)==2):
                    move=choice(self.moveset)
                    if move in self.moveset:
                        print("%s used %s!" % (t,move))
                        if move==self.move1:
                            global damage
                            damage=self.move1_pw*self.atk
                            if randint(1,1000) in range(600,750):
                                damage*=1.5
                                print("Critical hit! Damage increased this round")
                            if self.move1_buff=="poison" or "flame" :
                                opp.res(opp)
                            if self.move1_buff=="freeze"  or "sleep":
                                opp.freeze(opp)
                            if self.move1_buff=="para":
                                opp.para(opp)
                            if self.move1_buff=="pwup":
                                self.atk+=20
                                self.defense+=20
                                self.move1_pw+=10
                                self.move2_pw+=10
                                self.move3_pw+=10
                                self.move4_pw+=10
                                print("Stats increased due to move effects")
                            if self.move1_buff=="restore":
                                self.hp+=(self.maxhp-self.hp)/2
                                print("HP restored. %s HP left" % self.hp)
                        elif move==self.move2:
                            damage=self.move2_pw*self.atk
                            if randint(1,1000) in range(600,750):
                                damage*=1.5
                                print("Critical hit! Damage increased this round")
                            if self.move2_buff=="poison" or "flame" :
                                opp.res(opp)
                            if self.move2_buff=="freeze"  or "sleep":
                                opp.freeze(opp)
                            if self.move2_buff=="para":
                                opp.para(opp)
                            if self.move2_buff=="pwup":
                                self.atk+=20
                                self.defense+=20
                                self.move1_pw+=10
                                self.move2_pw+=10
                                self.move3_pw+=10
                                self.move4_pw+=10
                                print("Stats increased due to move effects")
                            if self.move2_buff=="restore":
                                self.hp+=(self.maxhp-self.hp)/2
                                print("HP restored. %s HP left" % self.hp)
                        elif move==self.move3:
                            damage=self.move3_pw*self.atk
                            if randint(1,1000) in range(600,750):
                                damage*=1.5
                                print("Critical hit! Damage increased this round")
                            if self.move3_buff=="poison" or "flame" :
                                opp.res(opp)
                            if self.move3_buff=="freeze"  or "sleep":
                                opp.freeze(opp)
                            if self.move3_buff=="para":
                                opp.para(opp)
                            if self.move3_buff=="pwup":
                                self.atk+=20
                                self.defense+=20
                                self.move1_pw+=10
                                self.move2_pw+=10
                                self.move3_pw+=10
                                self.move4_pw+=10
                                print("Stats increased due to move effects")
                            if self.move3_buff=="restore":
                                self.hp+=(self.maxhp-self.hp)/2
                                print("HP restored. %s HP left" % self.hp)
                        else:
                            damage=self.move4_pw*self.atk
                            if randint(1,1000) in range(600,750):
                                damage*=1.5
                                print("Critical hit! Damage increased this round")
                            if self.move4_buff=="poison" or "flame" :
                                opp.res(opp)
                            if self.move4_buff=="freeze"  or "sleep":
                                opp.freeze(opp)
                            if self.move4_buff=="para":
                                opp.para(opp)
                            if self.move4_buff=="pwup":
                                self.atk+=20
                                self.defense+=20
                                self.move1_pw+=10
                                self.move2_pw+=10
                                self.move3_pw+=10
                                self.move4_pw+=10
                                print("Stats increased due to move effects")
                            if self.move4_buff=="restore":
                                self.hp+=(self.maxhp-self.hp)/2
                                print("HP restored. %s HP left" % self.hp)
                        
            else:
                print(f"{t} has been freezed, paralysed or is sleeping.") 
    def defend(self,opp,t):
        sleep(1)
        global damage
        damage=damage//self.defense
        self.hp-=damage
        print("The defending Pokemon has took %s damage. It has %s HP left." % (damage, self.hp))
        damage=0
        if self.res==True:
            self.hp-=self.maxhp/8
            sleep(1)
            print("The defending Pokemon has took %s damage from poison or burn. %s HP left." % (self.maxhp/8, self.hp))
    def res(self,t):
        self.res1=True
        #print("The defending Pokemon has been poisoned or burnt.")
    def freeze(self,t):
        self.freeze1=True
        #print("The defending Pokemon has been freezed or is sleeping.")
    def para(self,t):
        self.para1=True
        #print("The defending Pokemon has been paralysed.")
    def perish(self,opp,t):
        self.perish1=3
        opp.perish1=3
    def sleep(self,t):
        self.sleep1=True
        
        
#Pokemon and their stats


mewtwo=Pokemon(680, 680, 154, 90, "Psycho Cut", "Psycho Blast", "Original Power", "Life Dew", "psychic", None, 90, 100, 60, 0, None, None, "pwup", "restore")
mew=Pokemon(600,600,100,100,"Heat Wave","Solar Blade","Seed Bomb","Ice Beam","psychic",None,95,120,80,90,"flame",None,"restore","freeze")
lugia=Pokemon(680,680,90,154,"Aeroblast","Dragon Rush","Hydro Pump","Sky Attack","psychic","flying",100,100,110,140,None,"para",None,"para")
entei=Pokemon(580,580,115,85,"Eruption","Sacred fire","Extrasensory","Scorching sands","fire",None,150,100,80,70,"flame","flame",None,"flame")
raikou=Pokemon(580,580,85,100,"Zap Cannon","Aura Sphere","Supercell Slam","Extrasensory","electric",None,120,80,100,80,"para",None,"para",None)
suicune=Pokemon(580,580,90,115,"Blizzard","Sheer cold","Surf","Extrasensory","water",None,110,400*random(),90,80,"freeze","freeze",None,None)
celebi=Pokemon(600,600,100,100,"Leaf Storm","Future Sight","Life Dew","Perish song","grass","psychic",130,120,0,0,None,None,"restore","perish")
groudon=Pokemon(670,670,150,140,"Precipice Blades","Eruption","Solar Beam","Hammer Arm","ground",None,120,150,120,100,None,"flame","flame","pwdn")
kyogre=Pokemon(670,670,150,140,"Muddy water","Origin Pulse","Water Spout","Ice Beam","water",None,90,110,150,90,None,None,None,"freeze")
rayquaza=Pokemon(680,680,150,90,"Dragon Acsent","Draco Meteor","Storm","Hyper Beam","dragon","flying",120,130,110,150,None,"pwup","para",None)
deoxys=Pokemon(600,600,180,160,"Psycho Boost", "Hyper Beam", "Meteor Beam","Focus Blast","psychic",None,140,150,120,120,"pwdn",None,"pwup","pwdn")
palkia=Pokemon(680,680,150,120,"Earth Power","Spacial Rend","Hydro Pump","Ice beam","water","dragon",90,150,110,90,"pwdn","pwdn",None,"freeze")
dialga=Pokemon(680, 680, 150, 120,"Roar Of Time","Iron Tail","Flash Cannon","Blizzard","steel","dragon",150,100,80,110,None,"pwdn","pwdn","freeze")
giratina=Pokemon(680,680,120,120,"Shadow Force","Aura Sphere","Stone Edge","Poltergeist","ghost","dragon",120,80,100,110,"pwdn",None,"pwup","para")
darkrai=Pokemon(600,600,135,90,"Dream Eater","Dark void","Thunder","Sludge Bomb","dark",None,100,0,110,90,"sleep","deep sleep","para","poison")
cresselia=Pokemon(600,600,75,130,"Moonblast","Future Sight","Lunar Blessing","Lunar Dance","psychic",None,95,120,0,0,"pwdn",None,"complete restore","restore")
zekrom=Pokemon(680,680,150,120,"Bolt Strike","Fusion Bolt","Draco Meteor","Scale Shot","electric","dragon",130,100,130,45*randint(1,5),"para","para","pwup",None)
reshiram=Pokemon(680, 680,150,120,"Blue Flare","Fusion Flame","Draco Meteor","Overheat","fire","dragon",130,100,130,130,"flame","flame","pwup","pwdn")
kyurem=Pokemon(660,660,170,100,"Glaciate","Blizzard","Stone Edge", "Draco Meteor","ice","dragon",90,110,100,130,"pwdn","freeze",None,"pwup")
diancie=Pokemon(600,600,160,150,"Diamond Storm","Mist Explosion","Stone Egde","Meteor Beam","rock","fairy",100,150,100,120,"pwup","pwup",None,"pwdn")
xerneas=Pokemon(680,680,131,98,"Geomancy","Moonblast","Close Combat","Thunder","fairy",None,50,95,120,110,("restore" and "pwup"), "pwdn","pwdn","para")
zygarde=Pokemon(708,708,100,216,"Land's Wrath","Thousand Arrows","Thousand Waves","Core Enforcer","ground","dragon",90,135,90,100,"pwdn","pwup","para","pwdn")
zacian=Pokemon(720,720,170,148,"Behemoth Blade","Moonblast","Hyper Beam","Steel Beam","fairy","steel",100,95,150,140,"pwup","pwdn","pwup","pwup")
miraidon=Pokemon(680,680,135,135,"Electro Drift","Overheat","Outrage","Solar Blade","electric","dragon",100,130,120,120,("pwup" and "para"),("pwdn" and "flame"),("para" and "pwup"),("pwup" and "pwdn"))


#Pokemon choosing   


pokemon1=None
poke1_name=None
pokemon2=None 
poke2_name=None

print("Enter your first Pokemon:")
while choosen==False:
    user=input()
    if user=="Mewtwo":
        choosen=True
        print("Looks like you have chosen Mewtwo, the Genetic Pokemon.")
        pokemon1=mewtwo
        poke1_name=user
    elif user=="Mew":
        choosen=True
        print("Looks like you have chosen Mew, the New Species Pokemon.")
        pokemon1=mew
        poke1_name=user
    elif user=="Lugia":
        choosen=True
        print("Looks like you have chosen Lugia, the Diving Pokemon.")
        pokemon1=lugia
        poke1_name=user
    #elif user=="hooh" or "ho-oh":
     #   choosen=False
      #  print("Choose legendaries or mythicals only. Be sure to not make spelling errors. Some Pokemon have not been added in the game yet, including all Pokemon introduced in Gen 7 or later.")
    elif user=="Entei":
        choosen=True
        print("Looks like you have chosen Entei, the Volcano Pokemon.")
        pokemon1=entei
        poke1_name=user
    elif user=="Raikou":
        choosen=True
        print("Looks like you have chosen Raikou, the Thunder Pokemon.")
        pokemon1=raikou
        poke1_name=user
    elif user=="Suicune":
        choosen=True
        print("Looks like you have chosen Suicune, the Aurora Pokemon.")
        pokemon1=suicune
        poke1_name=user
    elif user=="Celebi":
        choosen=True
        print("Looks like you have chosen Celebi, the Time Travel Pokemon.")
        pokemon1=celebi
        poke1_name=user
    elif user=="Groudon":
        choosen=True
        print("Looks like you have chosen Groudon, the Continental Pokemon.")
        pokemon1=groudon
        poke1_name=user
    elif user=="Kyogre":
        choosen=True
        print("Looks like you have chosen Kyogre, the Sea Basin Pokemon.")
        pokemon1=kyogre
        poke1_name=user
    elif user=="Rayquaza":
        choosen=True
        print("Looks like you have chosen Rayquaza, the Sky High Pokemon.")
        pokemon1=rayquaza
        poke1_name=user
    #elif user=="latias" or "latios":
     #   choosen=True
      #  mode="hell"
       # print("Looks like you have chosen The Eon Duo! Congrajulations for unlocking HELL MODE.")
    elif user=="Deoxys":
        choosen=True
        print("Looks like you have chosen Deoxys, the DNA Pokemon.")
        pokemon1=deoxys
        poke1_name=user
    #elif user=="jirachi":
     #   choosen=True
      #  mode="sleep"
       # print("Looks like you have chosen Ji... Oh dear! She is still asleep, and too unconscious to battle! Congrajulations on unlocking DEPRIVATION MODE.")
    elif user=="Palkia":
        choosen=True
        print("Looks like you have chosen Palkia, the Space Pokemon.")
        pokemon1=palkia
        poke1_name=user
    elif user=="Dialga":
        choosen=True
        print("Looks like you have chosen Dialga, the Time Pokemon.")
        pokemon1=dialga
        poke1_name=user
    elif user=="Giratina":
        choosen=True
        print("Looks like you have chosen Giratina, the Antimatter Pokemon.")
        pokemon1=giratina
        poke1_name=user
    #elif user=="arceus":
     #   choosen=True
      #  print("The God does not want to fight. Congrajulations on unlocking MYTH MODE.")
       # mode="god"
    elif user=="Darkrai":
        choosen=True
        print("Looks like you have chosen Darkrai, the Nightmare Pokemon.")
        pokemon1=darkrai
        poke1_name=user
    elif user=="Cresselia":
        choosen=True
        print("Looks like you have chosen Cresselia, the Lunar Pokemon.")
        pokemon1=cresselia
        poke1_name=user
    elif user=="Zekrom":
        print("Looks like you have chosen Zekrom, the Deep Black Pokemon.")
        pokemon1=zekrom
        poke1_name=user
    elif user=="Reshiram":
        choosen=True
        print("Looks like you have chosen Reshiram, the Vast White Pokemon.")
        pokemon1=reshiram
        poke1_name=user
    elif user=="Kyurem":
        choosen=True
        print("Looks like you have chosen Kyurem, the Boundary Pokemon.")
        pokemon1=kyurem
        poke1_name=user
    elif user=="Diancie":
        choosen=True
        print("Looks like you have chosen Diancie, the Jewel Pokemon.")
        pokemon1=diancie
        poke1_name=user
    elif user=="Xerneas":
        choosen=True
        print("Looks like you have chosen Xerneas, the Life Pokemon.")
        pokemon1=xerneas
        poke1_name=user
    elif user=="Zygarde":
        print("Looks like you have chosen Zygarde, the Order Pokemon.")
        choosen=True
        pokemon1=zygarde
        poke1_name=user
    #elif user=="yveltal":
     #   choosen=True
      #  mode="die"
       # print("Looks like you have chosen Yveltal, the Destruction Pokemon. You are completely destroyed and warped to another world. Congrajulations on unlocking REBIRTH MODE.")
    else:
        print("Choose legendaries or mythicals only. Be sure to not make spelling errors. Some Pokemon have not been added in the game yet, including all Pokemon introduced in Gen 7 or later.")
choosen=False
print("Enter your second Pokemon:")
while choosen==False:
    user2=input()
    if user2=="Mewtwo":
        choosen=True
        print("Looks like you have chosen Mewtwo, the Genetic Pokemon.")
        pokemon2=mewtwo
        poke2_name=user2
    elif user2=="Mew":
        choosen=True
        print("Looks like you have chosen Mew, the New Species Pokemon.")
        pokemon2=mew
        poke2_name=user2
    elif user2=="Lugia":
        choosen=True
        print("Looks like you have chosen Lugia, the Diving Pokemon.")
        pokemon2=lugia
        poke2_name=user2
    #elif user=="hooh" or "ho-oh":
     #   choosen=False
      #  print("Choose legendaries or mythicals only. Be sure to not make spelling errors. Some Pokemon have not been added in the game yet, including all Pokemon introduced in Gen 7 or later.")
    elif user2=="Entei":
        choosen=True
        print("Looks like you have chosen Entei, the Volcano Pokemon.")
        pokemon2=entei
        poke2_name=user2
    elif user2=="Raikou":
        choosen=True
        print("Looks like you have chosen Raikou, the Thunder Pokemon.")
        pokemon2=raikou
        poke2_name=user2
    elif user2=="Suicune":
        choosen=True
        print("Looks like you have chosen Suicune, the Aurora Pokemon.")
        pokemon2=suicune
        poke2_name=user2
    elif user2=="Celebi":
        choosen=True
        print("Looks like you have chosen Celebi, the Time Travel Pokemon.")
        pokemon2=celebi
        poke2_name=user2
    elif user2=="Groudon":
        choosen=True
        print("Looks like you have chosen Groudon, the Continental Pokemon.")
        pokemon2=groudon
        poke2_name=user2
    elif user2=="Kyogre":
        choosen=True
        print("Looks like you have chosen Kyogre, the Sea Basin Pokemon.")
        pokemon2=kyogre
        poke2_name=user2
    elif user2=="Rayquaza":
        choosen=True
        print("Looks like you have chosen Rayquaza, the Sky High Pokemon.")
        pokemon2=rayquaza
        poke2_name=user2
    #elif user=="latias" or "latios":
    #    choosen=True
     #   mode="hell"
        #print("Looks like you have chosen The Eon Duo! Congrajulations for unlocking HELL MODE.")
    elif user2=="Deoxys":
        choosen=True
        print("Looks like you have chosen Deoxys, the DNA Pokemon.")
        pokemon2=deoxys
        poke2_name=user2
    #elif user=="jirachi":
     #   choosen=True
      #  mode="sleep"
       # print("Looks like you have chosen Ji... Oh dear! She is still asleep, and too unconscious to battle! Congrajulations on unlocking DEPRIVATION MODE.")
    elif user2=="Palkia":
        choosen=True
        print("Looks like you have chosen Palkia, the Space Pokemon.")
        pokemon2=palkia
        poke2_name=user2
    elif user2=="Dialga":
        choosen=True
        print("Looks like you have chosen Dialga, the Time Pokemon.")
        pokemon2=dialga
        poke2_name=user2
    elif user2=="Giratina":
        choosen=True
        print("Looks like you have chosen Giratina, the Antimatter Pokemon.")
        pokemon2=giratina
        poke2_name=user2
    #elif user=="arceus":
     #   choosen=True
      #  print("The God does not want to fight. Congrajulations on unlocking MYTH MODE.")
       # mode="god"
    elif user2=="Darkrai":
        choosen=True
        print("Looks like you have chosen Darkrai, the Nightmare Pokemon.")
        pokemon2=darkrai
        poke2_name=user2
    elif user2=="Cresselia":
        choosen=True
        print("Looks like you have chosen Cresselia, the Lunar Pokemon.")
        pokemon2=cresselia
        poke2_name=user2
        choosen=True
    elif user2=="Zekrom":
        print("Looks like you have chosen Zekrom, the Deep Black Pokemon.")
        pokemon2=zekrom
        poke2_name=user2
        choosen=True
    elif user2=="Reshiram":
        choosen=True
        print("Looks like you have chosen Reshiram, the Vast White Pokemon.")
        pokemon2=reshiram
        poke2_name=user2
    elif user2=="Kyurem":
        choosen=True
        print("Looks like you have chosen Kyurem, the Boundary Pokemon.")
        pokemon2=kyurem
        poke2_name=user2
    elif user2=="Diancie":
        choosen=True
        print("Looks like you have chosen Diancie, the Jewel Pokemon.")
        pokemon2=diancie 
        poke2_name=user2
    elif user2=="Xerneas":
        choosen=True
        print("Looks like you have chosen Xerneas, the Life Pokemon.")
        pokemon2=xerneas
        poke2_name=user2
    elif user2=="Zygarde":
        choosen=True
        print("Looks like you have chosen Zygarde, the Order Pokemon.")
        pokemon2=zygarde 
        poke2_name=user2
    #elif user=="yveltal":
     #   choosen=True
      #  mode="die"
       # print("Looks like you have chosen Yveltal, the Destruction Pokemon. You are completely destroyed and warped to another world. Congrajulations on unlocking REBIRTH MODE.")
    else:
        print("Choose legendaries or mythicals only. Be sure to not make spelling errors. Some Pokemon have not been added in the game yet, including all Pokemon introduced in Gen 7 or later.")
if mode=="normal":   
    print("Let us start the battle now!")
    
    battle2(pokemon1,pokemon2,miraidon,zacian,poke1_name,poke2_name,"Miraidon","Zacian")
    
