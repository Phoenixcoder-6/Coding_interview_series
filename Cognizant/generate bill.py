def generate_bill(pizza,puffs,colddrink):
    totalbill= (pizza*100 + puffs*20 + colddrink*10)
    return totalbill

result=generate_bill(10,12,5)
print("Total price:",result)