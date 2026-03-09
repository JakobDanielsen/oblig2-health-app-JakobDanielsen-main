print("*"*20)
print("Welcome to oblig 2:")

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
print(bmi)
bmi = round(bmi,2)
print(bmi)

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
print(bmi_category)

def get_health_advice():
    match bmi_category:
        case "Obese":
            advice = "Drastically change diet: more protein, cut unnecessary calories like raffined sugar or empty fats, get a gym membership and focus on cardio"
        case "Overweight":
            advice = "Go on daily walks, dont eat out of boredom, focus on foods rich in saturated fats and protein"
        case "Normal":
            advice = "Seems like you know your stuff, but remember; staying in shape isnt free, effort and discipline are still necessary"
        case "Underweight":
            advice = "Eat until you are full every meal, dont skip any meals, include saturated fats and protein"
        case _:
            advice = bmi_category + " is not a valid category"
    return advice

print(get_health_advice())

def get_ideal_weight():
    ideal_weight = 22*height_m**2 # type: ignore
    return ideal_weight

print(get_ideal_weight())