from health import addRecord,get_health_advice,get_ideal_weight
from data import saveObject,jsonObject

print("\n")
print("*"*20)
print("Welcome to oblig 2:")

def writeNewEntry():
    health_entry = addRecord()
    get_health_advice(health_entry)
    saveObject(health_entry)

while True:
    choice = input("\nChoose an option: \n\n1: Add a health record\n2: View records\n3: View statistics\n4: Save and quit\n\n")
    match choice:
        case "1":
            writeNewEntry()
        case "2":
            for entry in jsonObject():
                print("\n")
                for key, value in entry.items():
                    print(key, value)
                print(f"Ideal weight difference: {round(entry['ideal_weight']-entry['weight_kg'],2)} kg")
        case "3":
            print("3 registered")
        case "4":
            print("Saving and quitting") # løsningen min lagrer etter hver gang og en "final save" vil ikke gjøre noe
            break
        case _:
            print("Command not registered. Input a number from 1-4")

