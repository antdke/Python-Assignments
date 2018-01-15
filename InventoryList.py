## Anthony Dike - Due: Nov. 28, 2017
## CSCI-UA.0002-012
## Assignment 8: Part 2

#This program creates an inventory list that the user can manipulate and interact with.

"""
PART COMPLETION CHECKLIST

Part 2a: C o m p l e t e
Part 2b: C o m p l e t e
Part 2c: C o m p l e t e
Part 2d: C o m p l e t e
Part 2e: C o m p l e t e
Part 2f: C o m p l e t e

"""

"""
Important Realization: Just create lists of product name, costs, and quantity
instead of creating an 'inventory' list with a multitude of each prodName
"""


#PRODUCT INFO
product_quantity = [10, 5, 20]
product_names = ["hamburger", "cheeseburger", "small fries"]
product_costs = [0.99, 1.29, 1.49]



# input "plug-ins"
option = "(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: "
prodName = "Enter a product name: "
prompt = ""

while prompt.lower() != "q":

    prompt = input(option)
    
    if prompt.lower() == "s":
        product = input(prodName) 

        if product.lower() in product_names:
            location = product_names.index(product)
            print('We sell "' + product + '" at ' + str(product_costs[location]) + ' per unit')
            print("We currently have",product_quantity[location],"in stock")
            print()
            
        elif product.lower() not in product_names:
            print('Sorry, we don\'t sell "' + product + '"')
            print()

    elif prompt.lower() == "l":
        print(format("Product","<9"), format("Price",">20"), format("Quantity",">10"))
        
        # create a for loop here with one line fits all
        for x in range(len(product_names)):
            print(format(product_names[x],"<10"), format(product_costs[x],">20.2f"), format(product_quantity[x], ">10"))

        print()

    # REPORTING THE INVENTORY

    elif prompt.lower() == "e":
        print("Most expensive product: " + str(max(product_costs)) + " (" + product_names[product_costs.index((max(product_costs)))] + ")")
        print("Least expensive product: " + str(min(product_costs)) + " (" + product_names[product_costs.index((min(product_costs)))] + ")")
        totalProdValue = 0
        for n in range(len(product_names)):
            totalProdValue += (product_costs[n] * product_quantity[n])
        print("Total value of all products: ",format(totalProdValue,".2f"))
        print()

    # UPDATING A PRODUCT

    elif prompt.lower() == "u":
        # boolean checker
        #prodUpdated = False OBSELETE
        proceedName = False
        proceedCost = False
        proceedQuantity = False

        location = ""
        
        #while prodUpdated == False: OBSELETE
        prodToBeUpdated = input("Enter a product name: ")
        if prodToBeUpdated in product_names:
            print("What would you like to update?")
            updatePrompt = input("(n)ame, (c)ost or (q)uantity: ")

            # to UPDATE prodName
            
            
            if updatePrompt == "n":
                while proceedName == False:
                    nameUpdated = input("Enter a new name: ")
                    if nameUpdated not in product_names:
                        location = product_names.index(prodToBeUpdated)
                        product_names.insert(location, nameUpdated)
                        product_names.remove(prodToBeUpdated)
                        print("Product name has been updated")
                        print()
                        proceedName = True
                        #prodUpdated = True OBSELETE
                    else:
                        print("Duplicate name!")
                        continue
            
            # to UPDATE prodCost
                    
            
            elif updatePrompt == "c":
                while proceedCost == False:
                    costUpdated = float(input("Enter a new cost: "))
                    if costUpdated > 0:
                        location = product_names.index(prodToBeUpdated)
                        product_costs.insert(location, costUpdated)
                        product_costs.remove(product_costs[location + 1])
                        print("Product cost has been updated")
                        print()
                        proceedCost = True
                        #prodUpdated = True OBSELETE
                    else:
                        print("Invalid cost!")
                        continue
                            
                
            # to UPDATE prodQuantity
                    
            
            elif updatePrompt == "q":
                while proceedQuantity == False:
                    quantityUpdated = int(input("Enter a new quantity: "))
                    if quantityUpdated > 0:
                        location = product_names.index(prodToBeUpdated)
                        product_quantity.insert(location, quantityUpdated)
                        product_quantity.remove(product_quantity[location + 1])
                        print("Product quantity has been updated")
                        print()
                        proceedQuantity = True
                        #prodUpdated = True OBSELETE
                    else:
                        print("Invalid quantity!")
                        continue

            else:
                print("Invalid option")
                print()
                        
                        
        else:
            print("Product doesn't exist. Can't update.")
            print()
            
                
        

    # REMOVING A PRODUCT
    
    elif prompt.lower() == "r":
        location = ""
        
        prodRemoved = input("Enter a product name: ")
        if prodRemoved in product_names:
            location = product_names.index(prodRemoved)
            product_names.remove(prodRemoved)
            del product_costs[location]
            del product_quantity[location]
            print("Product removed!")
            print()
        else:
            print("Product doesn't exist. Can't remove.")
            print()
            
        

    # ADDING A PRODUCT
    
    elif prompt.lower() == "a":
        # boolean checkers
        newProdAdded = False # Master Key
        newProdNameCheck = False
        newProdCostCheck = False
        newProdAmountCheck = False
        # while loop conditions
        while newProdAdded == False:
            
            while newProdNameCheck == False:
                newProdName = input("Enter a new product name: ")
                if newProdName.lower() in product_names:
                    print("Sorry, we already sell that product. Try again.")
                    continue
                else:
                    product_names.append(newProdName)
                    print(product_names) #test
                    newProdNameCheck = True
                    
            while newProdCostCheck == False:
                newProdCost = float(input("Enter a product cost: "))
                if newProdCost < 1:
                    print("Invalid cost. Try again.")
                    continue
                else:
                    product_costs.append(newProdCost)
                    print(product_costs) #test
                    newProdCostCheck = True
                    
            while newProdAmountCheck == False:
                newProdAmount = int(input("How many of these products do we have? "))
                if newProdAmount < 1:
                    print("Invalid quantity. Try again.")
                    continue
                else:
                    product_quantity.append(newProdAmount)
                    print(product_quantity)
                    newProdAmountCheck = True
                    
            newProdAdded = True # Master Key unlocking
            print("Product added!")
            print()
                   
    elif prompt.lower() == "q":
        print("See you soon!")
        print()

    else:
        print("Invalid option, try again")
        print()

