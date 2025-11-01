#Program to CALCULATE PROFIT OR LOSS BASED ON COST PRICE AND SELLING PRICE.

cp=float(input("Enter the Cost Price: "))
sp=float(input("Enter the Selling Price: "))

# Calculate profit or loss
if sp>cp:
    profit=sp-cp
    print("You made a Profit of:",profit)
elif sp<cp:
    loss=cp-sp
    print("Loss of:",loss)
else:
    print("No Profit, No Loss.")