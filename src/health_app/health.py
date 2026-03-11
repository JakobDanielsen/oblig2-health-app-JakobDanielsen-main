#Jeg valgte bevisst å bruke dictionaries istedenfor classes denne oppgaven ettersom vi jobber med ganske simple objekter og dict er mer kompatibelt med json(hovedsakelig at man lett kan gå fra dict til json og json til dict). K-I-S-S: keep it stupid simple
def get_ideal_weight(height_m):
    return round(22*height_m**2,1)

def addRecord():
    # -robust spørring
    while True: # validerer at name ikke er tom
        name = input("What is your name?: ")
        if name:
            break
        print("Name must contain a string")

    while True: # validerer at weight ikke er tom eller null eller mindre
        weight_kg = input("Enter your weight (kg): ")
        try:
            if weight_kg:
                weight_kg = float(weight_kg)
                if weight_kg >0: 
                    break
            print("Invalid weight")
        except ValueError:
            print("Please provide a number")

    while True: #validerer at heiht ikke er tom eller null eller mindre
        height_m = input("Enter your height (m): ")
        try:
            if height_m:
                height_m = float(height_m)
                if height_m >0:
                    break
            print("Invalid height")
        except ValueError:
            print("Please provide a number")  

    # -bmi utregning
    bmi = weight_kg/height_m**2
    bmi = round(bmi,2)
   
    

    # -bmi categorization
    bmi_category:str = ""

    if bmi >= 30:
        bmi_category = "Obese"
    elif bmi >= 25 and bmi<30:
        bmi_category = "Overweight"
    elif bmi < 25 and bmi>=18.5:
        bmi_category = "Normal"
    else:
        bmi_category = "Underweight"
    print("Health status: "+bmi_category)

    # -object create (ref linje 1 i denne filen)
    health_object = {
        "name":name,
        "weight_kg": weight_kg,
        "height_m": height_m,
        "bmi": bmi,
        "bmi_category":bmi_category,
        "ideal_weight": get_ideal_weight(height_m)
    }

    print ("*"*20)
    print(f"Entry saved: \n{name} \nBMI: {bmi} ({bmi_category})\nIdeal weight: {health_object['ideal_weight']} kg \nAdvice: {get_health_advice(health_object)}\n")

    return health_object


def get_health_advice(object):
    if not object["bmi_category"]:
        print("object not properly defined")
        return
    match object["bmi_category"]:
        case "Obese":
            advice = "Drastically change diet: more protein, cut unnecessary calories like raffined sugar or empty fats, get a gym membership and focus on cardio"
        case "Overweight":
            advice = "Go on daily walks, dont eat out of boredom, focus on foods rich in saturated fats and protein"
        case "Normal":
            advice = "Seems like you know your stuff, but remember; staying in shape isnt free, effort and discipline are still necessary"
        case "Underweight":
            advice = "Eat until you are full every meal, dont skip any meals, include saturated fats and protein"
        case _:
            advice = object["bmi_category"] + " is not a valid category"
    return advice

#print(get_health_advice(object))



