def fuel_consumption(fuel,distance):
    if fuel<=0:
        print(fuel,"is an Invalid Input")
    elif distance<=0:
        print(distance,"is an Invalid Input.")
    else:
        comp= (fuel/distance)*100

    return round(comp,2)
def fuel_consumption1(fuel,distance):
    distance_miles = distance * 0.6214
    # Convert fuel consumption from liters to gallons
    fuel_gallons = fuel* 0.2642
    # Calculate miles per gallon (mpg)
    mpg = round(distance_miles / fuel_gallons, 2)
    return mpg

fuel=20
distance=150

result= fuel_consumption(fuel,distance)
result1= fuel_consumption1(fuel,distance)
print(result,"km/lit")
print(result1,"miles/gallon")