
#blueprint
class Garage:
    def __init__(self):
        self.ticket = 0
        self.paymentstatus = {}
        self.numspaces = 15
        self.parkingspaces = {}
        for x in range(1,self.numspaces+1):
            self.parkingspaces[x] = 0
#dictionary^

    def taketicket(self):
        pass
    def ticketcount(self):
        pass

    def enter(self):
        self.ticket += 1
        self.paymentstatus[self.ticket] = False
        parkingspace = self.__next_free_space()  #keynumb from dict
        self.parkingspaces[parkingspace] = self.ticket
        print(f"You've been issured ticket number {self.ticket} for parking space number {parkingspace}")


##Key value statement
    def __next_free_space(self):
        """Finds the first available parking space in the dictionary"""
        for parking_spot, occupied in self.parkingspaces.items():
            if occupied == 0:
                return parking_spot


    def exit(self):
         if (welcome == 'exit'):
            if ticket >=15:
               print('garage is empty')
                   
            else:
                returnticket = self.ticket
                self.parkingspaces += 1
                print('spaces left: ' + (ticket))
        
    def quit(self):
        print('bye')



#actual object
parkingg = Garage()


while True:
    user_input = input("Thanks for choosing J%A&M's garage, please pick from the following: enter/exit or quit ").lower()
    if user_input == 'enter':
        parkingg.enter()
        continue
    if user_input == 'exit':
        parkingg.exit()
        continue
    if user_input == 'quit':
        parkingg.quit()
        break
    else:
        print("invalid input, try harder")
        continue
        

