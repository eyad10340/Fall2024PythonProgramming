# State Sales Tax and County Sales tax 
State_Sales_Tax_Rate=0.05
County_Sales_Tax_Rate=0.025

#Initialization of variables
Amount_Of_Purchase=0.0
State_Sales_Tax=0.0
County_Sales_Tax=0.0
Total_Sales_Tax=0.0
Total_Sales_Amount = 0.0

#display Results
print()
Amount_Of_Purchase= float(input("Enter The amount of the property Purchase: \n"))
State_Sales_Tax=State_Sales_Tax_Rate*Amount_Of_Purchase
County_Sales_Tax=County_Sales_Tax_Rate*Amount_Of_Purchase
Total_Sales_Tax= State_Sales_Tax + County_Sales_Tax
Total_Sales_Amount=Amount_Of_Purchase +  Total_Sales_Tax

print("The State Sales Tax is : $",format(State_Sales_Tax,".2f"))
print("County_Sales_Tax is : $",format(County_Sales_Tax,".2f"))
print("Total_Sales_Tax is : $",format(Total_Sales_Tax,".2f"))
print("Your Total Purchase Amount is : $",format(Total_Sales_Amount,".2f"))

print("\n Press the enter key to exit")