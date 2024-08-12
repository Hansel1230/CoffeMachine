import Dictionaries as Dictionaries

#TODO: Coins
def insertCoins(UserChoice:str):
    global GisValid
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
            Dictionaries.resources["water"]-=50
            Dictionaries.resources["Coffee"]-=18
                        
    if UserChoice==  "cappuccino":
        if coins <3.5:
            isenough = False
        else:
           Dictionaries.resources["water"]-=250
           Dictionaries.resources["Coffee"]-=24
           Dictionaries.resources["Milk"]-=100

    if UserChoice==  "latte":
        if coins <2.5:
            isenough = False
        else:
           Dictionaries.resources["water"]-=200
           Dictionaries.resources["Coffee"]-=24
           Dictionaries.resources["Milk"]-=150
    
    if isenough:
       Dictionaries.resources["Money"]=coins
    else:
        print("Sorry that's not enough money. Money refunded.")
        GisValid = False
 
def latte():
     
    Dictionaries.resources["Money"]-= 2.50
    Dictionaries.DictUserChoice["Choice"] = 'late'

def cappuccino():
    Dictionaries.resources["Money"]-= 3.00
    Dictionaries.DictUserChoice["Choice"] = 'cappuccino'

def espresso():
    Dictionaries.resources["Money"]-= 1.50
    Dictionaries.DictUserChoice["Choice"] = 'espresso'

#TODO: Check resources sufficient
def IsValidaresources(pUserChoice:str):
    global isOn,GisValid 
    
    if (Dictionaries.DictUserChoice.get(pUserChoice)) ==0:
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
    global GisValid,isOn
    wata=Dictionaries.resources["water"]
    coffe =Dictionaries.resources["Coffee"]
    milk=Dictionaries.resources["Milk"]
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
                print(f"Here is ${round(Dictionaries.resources['Money'],2)} in change.")
                print(f"Here is your {Dictionaries.DictUserChoice['Choice']} ☕ Enjoy!")
                Dictionaries.resources['Money'] = 0

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
        #TODO: Print report.
        Dictionaries.printresourses()
    
    if UserChoice== "drinks":
        drinksTxt = ''
        #TODO: Print Drinks.
        for i in Dictionaries.DictDrinks:
            print(f'{i.capitalize()}:')
            for j in Dictionaries.DictDrinks[i],[]:
                drinksTxt = str(j)
                if drinksTxt != '[]':
                    drinksTxt = drinksTxt.replace('{', '')
                    drinksTxt = drinksTxt.replace('}', '')
                    drinksTxt = drinksTxt.replace("'", "")
                    print(drinksTxt)
    
    if isOn:
        IsValidaresources(UserChoice)
