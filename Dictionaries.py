resources = {
    "water":300,
    "Milk":200,
    "Coffee":100,
    "Money":0,
    "InChange":0
}

DictUserChoice = {
    "espresso":0.0,
    "latte":0.0,
    "cappuccino":0.0,
    "report":0.0,
    "Choice":'',
    "drinks":0.0
}  

DictDrinks = {
    "espresso":{
        "water":"50ml",
        "coffe":"18g"
    },
    "latte":{
        "water":"200ml",
        "milk":"150ml",
        "coffe":"24g"
    },
    "cappuccino":{
       "water":"250ml",
        "milk":"100ml",
        "coffe":"24g"
    }
}  


def printresourses():
    print(f'Water:{resources["water"]}ml')
    print(f'Milk:{resources["Milk"]}ml')
    print(f'Coffee:{resources["Coffee"]}g')
    print(f'Money:${round(resources["Money"],2)}')