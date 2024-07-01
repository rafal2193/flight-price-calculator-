#Rafal Krauze
#June 30,2024
#CMP 131
#Chapter 5 Lab Writing programmer-defined functions.
#This program will create a code that will caculate the total cost of flights tickets.
#The customer will be able to choose the amount of tickets they which to purchase and what section on the plane. 
#I hereby attest that this code is original and written by me alone. I understand that I risk a penalty for violating the Academic Integrity policy at CCM

#Defining my main function that will be used to determine the price. 
def calcPrice(num_tickets, seat_type):

#Catagorizing seat type and price
    if seat_type == 'first class':
        ticket_price = 1000
    elif seat_type == 'economy plus':
        ticket_price = 400
    elif seat_type == 'economy':
        ticket_price = 250
    else:
        print("Invalid seat type entered. Please choose from 'first class', 'economy plus', or 'economy'.")
        return None
    
    total_price = num_tickets * ticket_price
    return total_price

#Defining number of tickets and seat type
def main():
    num_tickets = int(input("How many tickets would you like to purchase? "))
    seat_type = input("Which seat type would you like (first class, economy plus, economy)? ")

#Caculation of ticket price
    total_due = calcPrice(num_tickets, seat_type)
    if total_due is not None:
        print(f"Total due: ${total_due}")
#Calls the main function
if __name__ == '__main__':
    main()
