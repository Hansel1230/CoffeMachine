 #Dictionaty
resources = {
    "water":300,
    "Milk":200,
    "Coffee":100,
    "Money":0
}
 #Dictionaty
DictUserChoice = {
    "espresso":0.0,
    "latte":0.0,
    "capuccino":0.0,
    "report":0.0
}    

Greturn=True

#TODO: Check resources sufficient
def IsValidaresources(pUserChoice:str):
    global DictUserChoice
    global isOn
    global Greturn
    
    if (DictUserChoice.get(pUserChoice)) ==0:
        match UserChoice:
            case "espresso":
                IsValidResources2('espresso')
            case "cappuccino":
                IsValidResources2('cappuccino')
            case "latte":
                IsValidResources2('latte')

        if not Greturn:
            isOn = False
    else:
        print('Opcion invalida')
    
def IsValidResources2(pUserChoice:str):
    global resources,Greturn
    wata=resources["water"]
    coffe = resources["Coffee"]
    milk= resources["Milk"]
    resource = ''

    if pUserChoice == 'espresso':
        if wata<50:
            resource= 'water'
        if coffe<18:
            resource= 'coffe'

    if pUserChoice == 'latte':
        if wata<200:
            resource= 'water'
        if coffe<24:
            resource= 'coffe'
        if milk<150:
            resource= 'milk'

    if pUserChoice == 'cappuccino':
        if wata<250:
           resource= 'water'
        if coffe<24:
            resource= 'coffe'
        if milk<100:
            resource= 'milk'
    
    if resource != '':
        print(f"Sorry there is not enough {resource}.")
        Greturn= False
        off()

#TODO: Coins
def insertCoins(UserChoice:str):
    global resources
    isenough = True
    print("Please insert coins.")
    quartes = int(input("How many quartes?:"))
    dimes =   int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    coins= (quartes*0.25)+ (0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    
    if UserChoice== "espresso":
           if coins <4.0:
            isenough = False     
    if UserChoice==  "cappuccino":
        if coins <3.5:
            isenough = False
    if UserChoice==  "latte":
        if coins <2.5:
            isenough = False
    resources["Money"]=coins

#TODO: Print report.
def printresourses():
    global resources
    print(f'Water:{resources["water"]}ml')
    print(f'Milk:{resources["Milk"]}ml')
    print(f'Coffee:{resources["Coffee"]}ml')
    print(f'Money:${resources["Money"]}')

def espresso():
    a=1

def latte():
        a=1

def cappuccino():
    a=1

def off():
    print('Good bye')
    global isOn
    isOn=False
    
def report():
    printresourses()


isOn = True
while isOn:

    #TODO: Prompt user by asking

    print('☕ What would you like? (espresso/latte/cappuccino):”')
    UserChoice = input()

    if UserChoice=="off":
        off()
    if UserChoice== "report":
        report()
    
    IsValidaresources(UserChoice)
    if Greturn== True:
        insertCoins(UserChoice)

        match UserChoice:
            case "espresso":
                espresso()
            case "cappuccino":
                cappuccino()
            case "latte":
                latte()

