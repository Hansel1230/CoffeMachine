 #Dictionaty
resources = {
    "water":300,
    "Milk":200,
    "Coffee":100,
    "Money":0,
    "InChange":0
}
 #Dictionaty
DictUserChoice = {
    "espresso":0.0,
    "latte":0.0,
    "cappuccino":0.0,
    "report":0.0,
    "Choice":''
}  
 
#TODO: Coins
def insertCoins(UserChoice:str):
    global resources,GisValid
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
           else:
            resources["water"]-=50
            resources["Coffee"]-=18
                        
    if UserChoice==  "cappuccino":
        if coins <3.5:
            isenough = False
        else:
            resources["water"]-=250
            resources["Coffee"]-=24
            resources["Milk"]-=100

    if UserChoice==  "latte":
        if coins <2.5:
            isenough = False
        else:
            resources["water"]-=200
            resources["Coffee"]-=24
            resources["Milk"]-=150
    
    if isenough:
        resources["Money"]=coins
    else:
        print("Sorry that's not enough money. Money refunded.")
        GisValid = False

#TODO: Print report.
def printresourses():
    global resources
    print(f'Water:{resources["water"]}ml')
    print(f'Milk:{resources["Milk"]}ml')
    print(f'Coffee:{resources["Coffee"]}ml')
    print(f'Money:${round(resources["Money"],2)}')
 
def latte():
    global resources,DictUserChoice
    resources["Money"]-= 2.50
    DictUserChoice["Choice"] = 'late'

def cappuccino():
    global resources,DictUserChoice
    resources["Money"]-= 3.00
    DictUserChoice["Choice"] = 'cappuccino'

def espresso():
    global resources,DictUserChoice
    resources["Money"]-= 1.50
    DictUserChoice["Choice"] = 'espresso'

#TODO: Check resources sufficient
def IsValidaresources(pUserChoice:str):
    global DictUserChoice
    global isOn
    global GisValid
    
    if (DictUserChoice.get(pUserChoice)) ==0:
        match pUserChoice:
            case "espresso":
                IsValidResources2('espresso')
            case "cappuccino":
                IsValidResources2('cappuccino')
            case "latte":
                IsValidResources2('latte')

        if not GisValid:
            isOn = False
    else:
        print('Opcion invalida')
    
def IsValidResources2(pUserChoice:str):
    global resources,GisValid,DictUserChoice,isOn
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
        GisValid= False
        isOn = False
         
    else:
        if GisValid== True:
            insertCoins(UserChoice)
            if GisValid== True:
                match UserChoice:
                    case "espresso":
                        espresso()
                    case "cappuccino":
                        cappuccino()
                    case "latte":
                        latte()
                print(f"Here is ${round(resources['Money'],2)} in change.")
                print(f"Here is your {DictUserChoice['Choice']} ☕ Enjoy!")
                resources['Money'] = 0

isOn = True
while isOn:
    GisValid = True
    #TODO: Prompt user by asking

    print('☕ What would you like? (espresso/latte/cappuccino):”')
    UserChoice = input()

    if UserChoice=="off":
        print('Good bye')
        isOn = False
        GisValid = False
    if UserChoice== "report":
        printresourses()
    
    if isOn:
        IsValidaresources(UserChoice)