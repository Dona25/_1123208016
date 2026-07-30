print("Bill Calculation")
n=int(input("Enter the number of members: "))
total_bill=int(input("Enter the total bill: "))
tips=int(input("Enter the tips given: "))
total=total_bill+tips
bill_share=total/n
print(f"The share of each member: {bill_share}")