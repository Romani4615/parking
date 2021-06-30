
#blueprint
#object
class Garage:
    def __init__(self):
        #attributes
        self.ticket = 0
        self.paymentstatus = {}
        self.numspaces = 15
        self.parkingspaces = {}
        for x in range(1,self.numspaces+1):
            self.parkingspaces[x] = 0
#dictionary^

#methods\/
    def enter(self):
        self.ticket += 1
        self.paymentstatus[self.ticket] = False
        parkingspace = self.__next_free_space()  #keynumb from dict
        self.parkingspaces[parkingspace] = self.ticket
        print(f"You've been issued ticket number {self.ticket} for parking space number {parkingspace}")


##Key value statement
    def __next_free_space(self):
        """Finds the first available parking space in the dictionary""" #iterating through the key/values of the parking space dictionary
        for parking_spot, occupied in self.parkingspaces.items():  #for key, value in dictionary(bc i wrote items, we basically opened up the dictionary)
            if occupied == 0:     #calling on value IF IT'S NOT FILLED WITH A TICKET(SPOT) 
                return parking_spot #THEN WE RETURN THE KEY TO 0 BC THE VALUE IS ZERO/EMPTY/NOTFILLED 
    def show(self):
        input(f'Here is all the availibe spots: {self.parkingspaces}\n press any key to continue')
        

    def exit(self):
        if self.paymentstatus[self.ticket] == False:
            print("please comeback when you've paid!")
            self.paynow()
                   
        else:
            returnticket = self.ticket
            self.parkingspaces += 1 
            print('spaces left: ' + (self.ticket))
        
    def quit(self):
        if self.paymentstatus[self.ticket] == False:
            print('YOU CAN NEVER LEAVE.. without paying')
            self.paynow()

    def paynow(self):
        input('Thanks for coming you owe: $15, please enter: pay to fulfill the transaction ').lower()
        print("Have a swell day")
        self.paymentstatus[self.ticket] = True

#actual object
parkingg = Garage()

#driver code
while True:
    user_input = input("Thanks for choosing A&M's garage, please pick from the following: enter/exit/show or quit ").lower()
    if user_input == 'enter':
        parkingg.enter()
        continue
    elif user_input == 'exit':
        parkingg.exit()
        break
    elif user_input == 'quit':
        parkingg.quit()
        break
    elif user_input == 'show':
        parkingg.show()
    elif user_input == 'pay':
        parkingg.paynow()
        continue


    else:
        print("invalid input, try harder")
        continue
        

