seed = 0x5a0
pickupMons = 6

def rngAdvance(prev):
    rng = ((prev * 0x41c64e6d) + 0x6073) 
    return rng % 0x100000000

def findPickupItem(item):
    if(item <= 29):
            return("Super Potion")
    elif(item >= 30 and item <= 39):
            return("Full Heal")
    elif(item >= 40 and item <= 49):
            return("Ultra Ball")
    elif(item >= 50 and item <= 59):
            return("Rare Candy")
    elif(item >= 60 and item <= 69):
            return("Full Restore")
    elif(item >= 70 and item <= 79):
            return("Revive")
    elif(item >= 80 and item <= 89):
            return("Nugget")
    elif(item >= 90 and item <= 94):
            return("Protein")
    elif(item >= 95 and item <= 98):
            return("PP Up")
    elif(item == 99):
            return("King's Rock")
        
temp = seed
for i in range(0, 3000):
    itemList = ""
    temp = rngAdvance(temp)
    temp1 = temp
    #print(hex(temp >> 16))
    
    temp1 = rngAdvance(temp1)
    temp1 = rngAdvance(temp1)
    temp1 = rngAdvance(temp1)
    iv1 = temp1 >> 16
    if((iv1 % 10) == 0):
        temp1 = rngAdvance(temp1)
        iv2 = temp1 >> 16
        itemList = "Pickup Mon 1" + ": " + str(findPickupItem(iv2 % 100) + " ")
    for j in range(0, pickupMons - 1):
        temp1 = rngAdvance(temp1)
        iv3= temp1 >> 16
        if(iv3 % 10 == 0):
            temp1 = rngAdvance(temp1)
            iv4 = temp1 >> 16
            itemList = itemList + "Pickup Mon " + str(j + 2) + " : " + str(findPickupItem(iv4 % 100))
    if(itemList != ""):
        print("Frame: " + str(i) + " " + itemList)
    else:
        print("Frame: " + str(i))
                
    
        
    
