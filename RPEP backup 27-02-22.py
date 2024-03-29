""" RPEP backup february 27, 2022"""

from psychopy import visual, event, core, gui, data
import pandas, numpy, os, random

os.chdir(r'C:\Users\Lenovo\Desktop\School\1e Master\Jaarvakken\Research Project Experimental Psychology\Fotos') 

#random variables
#1. condition order
conditions = ['relevant tactile', 'irrelevant tactile', 'control condition']
cond1 = random.choice(conditions)
cond2, cond3 = cond1, cond1
while cond2 == cond1:
    cond2 = random.choice(conditions)
while cond3 in (cond1, cond2):
    cond3 = random.choice(conditions)
    
randomconditions = [cond1, cond2, cond3]
print(randomconditions)

#2 wordlist order
wordlists = [(0,15),(15,30),(30,45)]
list1 = random.choice(wordlists)
list2, list3 = list1, list1
while list2 == list1:
    list2 = random.choice(wordlists)
while list3 in (list1, list2):
    list3 = random.choice(wordlists)
    
randomlists = [list1, list2, list3]
print(randomlists) 

#dialog box
my_directory = os.getcwd()
directory_to_write_to      = my_directory + "\Data" #Nu maakt hij door dit nog eens extra mapje data in mapje data. -> fixen
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)
print('dir:', directory_to_write_to)
info = {"Participant naam":"Incognito", "Subject nummer":0, "Leeftijd":0, "Gender":["man", "vrouw", "X"]}
## present the dialog box
myDlg = gui.DlgFromDict(dictionary = info, title = "Please put in your personal information")
## construct the name of the data file
os.chdir(r'C:\Users\Lenovo\Desktop\School\1e Master\Jaarvakken\Research Project Experimental Psychology\Fotos\Data') 

already_exists = True
while already_exists is True:
    file_name = directory_to_write_to + str(info["Subject nummer"]) + '.xlsx'
    if os.path.exists(file_name) is False:
        already_exists = False
    ##ask for a new participant number if already in use
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Oei, dit nummer is al in gebruik! Kies een ander nummer.")
        myDlg2.show()
        if myDlg2.OK:
            myDlg.show()

#combine arrays in trials matrix
data = numpy.column_stack([info["Subject nummer"], info["Leeftijd"], info["Gender"], randomconditions[0],randomconditions[1],randomconditions[2], str(randomlists[0]), str(randomlists[1]), str(randomlists[2])])
numpy.savetxt("randomvariables.txt", data, delimiter = "\t", fmt = "%.10s")
dataFrame = pandas.DataFrame.from_records(data)
dataFrame.columns = ['Nummer','Leeftijd','Gender','Condition 1','Condition 2','Condition 3','List 1','List 2','List 3']
dataFrame.to_excel(file_name, engine = 'xlsxwriter') # de excel file slaat nog niet op in het juiste mapje

os.chdir(r'C:\Users\Lenovo\Desktop\School\1e Master\Jaarvakken\Research Project Experimental Psychology\Fotos') 
#make window
win = visual.Window(fullscr = False, color = 'white')
#function for text
MessageOnSCreen = visual.TextStim(win, text = "OK")
def message(message_text = "", response_key = None, duration = 2, height = None, pos = (0.0, 0.8), color = "black"):
    
     
     MessageOnSCreen.text    = message_text
     MessageOnSCreen.height  = height
     MessageOnSCreen.pos     = pos
     MessageOnSCreen.color   = color
     
     MessageOnSCreen.draw()

#woorden:
SwahiliList = ['Angalia', 'Nguo ya nguo', 'Ganda','Manyoya','Brashi ya rangi', 'Nyepesi','Jani', 'Msumari', 'Bati linaweza', 'Uma', 'Pipi', 'Marumaru','Kamba','Gari','Mfuniko wa chupa', 'Mchemraba wa rubix', 'Sarafu', 'Bata ya kuoga', 'Mswaki', 'Mkufu', 'Mkasi', 'Kikombe', 'Vichwa vya sauti', 'Fizi', 'Jiwe','Mpiga shimo', 'Maua', 'Kinyago cha kinywa', 'Simu', 'Yai', 'Kete','Kipande cha karatasi', 'Kalamu', 'Kuzuia', 'Chupa', "Kining'iniza nguo",'Ndizi', 'Kijiko','Funguo','Kitabu','Kipande cha fumbo', 'Kiatu', 'Bisibisi', 'Sifongo', 'Karatasi ya karatasi']
Nl1 = ['Uurwerk','Wasknijper','Schelp','Veer','Verfborstel','Aansteker','Blad','Spijker','Blikje','Vork','Snoepje','Knikker','Touw','Speelgoed auto','Kroonkurk']
Nl2 = ['Rubikubs','Muntje','Badeend','Tandenborstel','Ketting','Schaar','Tas','Koptelefoon','Gom','Steen','Perforator','Bloem','Mondmasker','Gsm','Ei']
Nl3 = ['Dobbelsteen','Paperclip','Balpen','Blokje','Fles','Klerenhanger','Banaan','Lepel','Sleutels','Boek','Puzzelstuk','Schoen','Schroevendraaier','Spons','Blad papier']
myMouse = event.Mouse() 
mouse1 = myMouse.getPressed()

#Intertrial function
ITI = 0.3
def intertrial_pauze(control = True):
    message(message_text = 'Wacht op het volgende voorwerp', pos = (0.0,0.0))
    win.flip()
    core.wait(ITI)
    
#Training function
def training(lijst):
    for i in range(lijst[0],lijst[1]):
        y = str(i+1) + '.jpg'
        stim= visual.ImageStim(win, image=y, pos = (0.0, -0.2))
        stim.draw()
        message(message_text = SwahiliList[i])
        win.flip()
        core.wait(0.8)
        if i+1 != lijst[1]:
            intertrial_pauze()
        
#Distractor function
def distractor():
    #explanation of distractor task
    message(message_text = 'Nu zal u enkele rekensommen te zien krijgen, u moet beslissen of deze fout of juist zijn.' + "\n\nAls de berekening juist is, druk 'T' op het toetsenbord. Denk je dat het fout is,druk dan op 'F'" +"\n\nKlik op de spatiebalk om verder te gaan.", pos = (0.0,0.0), height = 0.08)
    win.flip()
    event.waitKeys(keyList = "space")

    #calculations
    calcu= ["12 x 6 = 72","126 + 389= 515","321 : 3 = 109", "26 x 3 = 78", "314 - 220 = 94","12 x 12 = 133","88-32 = 56",
    "42 : 3 = 14", "562 - 78 = 494", "22 + 96 = 118", "88 x 3 = 264", "33 x 11 = 333","623 + 76 = 700","41-23 = 19",
    "333 - 90 = 234", "48 : 3 = 16","73 + 74 = 147","465 - 321 = 144","32 x 7 = 221", "55 x 3 = 165", "77-21 = 56"]
    corr = ["t","t","f","t","t","f","t",
    "t", "f","t","t","f","f","f",
    "f","t","t","t","f","t","t"]
    ct = -1
    score,f = 0,0
    algehad = [-1]

    #which calculations in which condition
    n = 0
    if number == 0:
        n= (0,6)
    elif number == 1:
        n = (6,11)
    else:
        n = (12,17)
    
    fout = False
    while score <6:
        if len(algehad) == 7:
            algehad = []
        if fout is True:
            ct = random.randint(n[0],n[1])
        else:
            while ct in algehad:
                ct = random.randint(n[0],n[1])
        message(message_text = calcu[ct] ,response_key = ["f","t"], pos = (0.0,0.0))
        message(message_text = f'score = {score}', pos= (-0.5,0.5))
        win.flip()
        keys = event.waitKeys(maxWait = 10, keyList = ["f","t"])
        #feedback for participant
        if keys == None:
            message(message_text = "Te traag!" , pos = (0.0,0.0))
            win.flip()
            core.wait(0.2)
            fout = True
            f+=1
        elif keys[0] == corr[ct]:
            score +=1
            print('+1 punt')
            fout = False
            algehad.append(ct)
        else:
            message(message_text = "Fout!"+"\n\nProbeer gefocust te blijven op de rekensom" , pos = (0.0,0.0))
            win.flip()
            core.wait(0.2)
            fout = True
            f+=1
        if f > 2:
            score,f = 0,0

##Test function
def test(lijst, number):
    #intro
    message(message_text = "Test fase" +"\n\nIn dit deel zal u enkel het nederlandse woord te zien krijgen, antwoord luidop met het corresponderende woord dat u geleerd heeft in Swahili.'" + "\n\nVoor elk woord heeft u telkens 30 seconden de tijd." +"\n\nKlik op de spatiebalk om te beginnen met de test fase.", pos = (0.0,0.0), height = 0.07)
    win.flip()
    event.waitKeys(keyList = "space")
         
    ##dit moet nog veranderen naar enkel het nederlandse woord
    for i in range(lijst[0], lijst[1]):
        if lijst[0] == 0:
            message(message_text = Nl1[i], pos = (0,0),height = 0.2)
        elif lijst[0] == 15:
            message(message_text = Nl2[i-15], pos = (0,0),height = 0.2)
        elif lijst[0] == 30:
            message(message_text = Nl3[i-30], pos = (0,0),height = 0.2)
        win.flip()
        core.wait(1)
        #if i+1 != lijst[1]:
            #intertrial_pauze()
            
##Smallbreak function
def pauze():
    message(message_text = 'Neem een korte pauze en klik op de spatiebalk als u verder wilt gaan', response_key = 'space', pos = (0.0,0.0))
    win.flip()
    event.waitKeys(keyList = "space")

#  UITVOEREN ##
message(message_text = "Welkom!" +"\n\nIn dit experiment zult u woorden Swahili moeten memoriseren." + "\n\nHet experiment bestaat uit 3 delen, telkens met een trainingsfase en een testfase" + "\n\nKlik op de spatiebalk om verder te gaan.", pos = (0.0,0.0), height = 0.07)
win.flip()
event.waitKeys(keyList = "space")

for number, condition in enumerate(randomconditions):
    if condition == 'control condition':
        if number in (1, 2):
            message(message_text = "Control condition" + "\n\nIn dit deel heeft u geen voelbox nodig." +"\n\nU hebt telkens 20 seconden om het woord te memoriseren."+ "\n\nKlik op de spatiebalk als u klaar bent voor de trainingsfase", pos = (0.0,0.0), height = 0.08)
            win.flip()
            event.waitKeys(keyList = "space")
        else:
            message(message_text = "Control condition" +"\n\nU hebt telkens 20 seconden de tijd om het woord te memoriseren."+"\n\nKlik op de spatiebalk als u klaar bent voor de eerste trainingsfase", pos = (0.0,0.0), height = 0.08)
            win.flip()
            event.waitKeys(keyList = "space")
    elif condition == 'relevant tactile':
        while (myMouse.getPressed()[0] != 1):
            message(message_text = "#Relevant tactile" + "\n\nIn dit deel van het experiment zal u de voelbox moeten gebruiken." + "\n\nZorg er zeker voor dat u het object goed aanraakt, er kunnen ook vragen komen over de tactiele eigenschappen van het voorwerp." +"\n\nU hebt telkens 20 seconden de tijd om het woord te memoriseren."+ "\n\nKlik op de linker muisknop in de voelbox om de trainingsfase te starten" + "\n\nProbeer het voorwerp onmiddelijk hierna aan te raken!", pos = (0.0,0.0), height = 0.08)
            win.flip()
    else: 
        while (myMouse.getPressed()[0] != 1):
            message(message_text = "#Irrelevant tactile" + "\n\nIn dit deel van het experiment zal u de voelbox moeten gebruiken." + "\n\nZorg er zeker voor dat u het object goed aanraakt, er kunnen ook vragen komen over de tactiele eigenschappen van het voorwerp." +"\n\nU hebt telkens 20 seconden de tijd om het woord te memoriseren."+ "\n\nKlik op de linker muisknop van de muis in de voelbox om de trainingsfase te starten" + "\n\nProbeer het voorwerp onmiddelijk hierna aan te raken!", pos = (0.0,0.0), height = 0.08)
            win.flip()
    training(randomlists[number])
    distractor()
    test(randomlists[number], condition)
    if number < 2:
        pauze()

message(message_text = "Bedankt voor uw deelname!", pos = (0.0,0.0))
win.flip()
event.waitKeys(keyList = "space")
 
#nog te fixen:
# -> de excel file slaat nog niet op in het juiste mapje
# -> intertrial interval kiezen
#-> bug in laatste distractor taak
#-> foto's vervangen
