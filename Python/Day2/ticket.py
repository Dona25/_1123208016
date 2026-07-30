print(f"Movie Ticket Booking")
movie = input("Enter Movie Name: ")
total_tickets = int(input("Enter the total number of tickets: "))
children = int(input("Enter Number of Children: "))
ticket_price = 150
adults = total_tickets - children
total_amount = adults * ticket_price
print("Booking Details")
print(f"Movie Name: {movie}")
print(f"Total Tickets: {total_tickets}")
print(f"Children Tickets: {children}")
print(f"Paid Tickets: {adults}")
print(f"Ticket Price: ₹ {ticket_price}")
print(f"Total Amount: ₹ {total_amount}")
confirm = input("\nConfirm Booking (yes/no): ")
if confirm.lower() == "yes":
    print("Booking Successful!")
    print("Enjoy Your Movie!")
else:
    print("Booking Cancelled!")