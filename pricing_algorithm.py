base = input("What is the base price of this city? ")
size = input("What is the size of your venue? ")
accessiblity = input("Is your venue accessible? ")
lighting = input("Does your venue have nice lighting? ")
lighting_rails = input("Does your venue have lighting rails? ")
hanging_rails = input("Does your venue have hanging rails? ")
display = input("Does your venue have a spot to display goods? ")
extra = input("Does your venue have extra positive features? ")

rp = base*size*accessiblity*lighting*lighting_rails*hanging_rails*display*extra
minp = rp*0.8
maxp = rp*1.2


print("The recommended price is: "+str(rp))
print("The price range is "+"["+str(minp)+" , "+str(maxp)+"]")
