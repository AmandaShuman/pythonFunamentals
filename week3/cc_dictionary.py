inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall inches:", total_inches)
print_total_snowfall(inches_snow)

while True:
    inches_snow["Thursday"] = input("How many inches of snow fell on Thursday? ")
    if inches_snow["Thursday"].isdigit() >= 0: 
        inches_snow["Thursday"] = int(inches_snow["Thursday"])
        print_total_snowfall(inches_snow)
        break
    else:
        print("Invalid input. Try again.")
        continue
