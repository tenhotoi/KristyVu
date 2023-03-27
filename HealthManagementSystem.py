# https://www.geeksforgeeks.org/health-management-system-using-python/

import datetime
  
class HealthManagement():
    def __init__(self) -> None:
        self.name = {1: "Nilesh", 2: "Shanu"}
        self.a = {1: "Log", 2: "Retrieve"}
        self.b = {1: "Food", 2: "Exercise"}
        
    def getdate(self):    
        # to get date and time
        return datetime.datetime.now()

    def addname(self):
        nameentry = input("Please enter patient name to add into the database: ")
        self.name.update({len(self.name) + 1 : nameentry.replace(" ", "").title()})
        
    def selectname(self):
        for key, value in self.name.items():
    
            # taking input of name
            print("Press", key, "for", value, "\n", end="")

        try:    
            n = int(input("type here...     "))
        except ValueError as err:
            print(err, "\n Please enter expected values, which is between 1 and", len(self.name))
            exit('Invalid entry.')
            # return 'Invalid entry.'

        if n not in range(1, len(self.name) + 1):
            print("Please enter number between 1 and ", len(self.name))
            exit('Invalid entry.')
            # return 'Invalid entry.'
        else:
            return n
        
    def select_file_action(self):
        for key, value in self.a.items():
    
            # taking input of function that user wants to
            # do (either log or retrieve)
            print("Press", key, "for", value, "\n", end="")
            
        try:
            x = int(input("type here...     "))
        except ValueError as err:
            print(err, "\n Please enter expected values, which is either 1 or 2.")
            exit('Invalid entry.')
            # return 'Invalid entry.'
        
        if x not in range(1, len(self.a) + 1):
            print("Please enter number between 1 and ", len(self.a), ' to select option of read or write file.')
            exit('Invalid entry.')
            # return 'Invalid entry.'
        else:
            return x
    
    
    def select_task(self):
        for key, value in self.b.items():
            
            # ask user to choose between food 
            # and exercise
            print("Press", key, "for", value, "\n", end="")

        try:
            y = int(input("type here...     "))
        except ValueError as err:
            print(err, "\n Please enter expected values, which is either 1 or 2.")
            exit('Invalid entry.')
            # return 'Invalid entry.'

        if y not in range(1, len(self.b) + 1):
            print("Please enter number between 1 and ", len(self.b), ' to select task option.')
            exit('Invalid entry.')
            # return 'Invalid entry.'
        else:
            return y
    
    def action(self, n, x, y):
        if n == 'Invalid entry.' or x == 'Invalid entry.' or y == 'Invalid entry.':
            return 'Invalid entry.'

        nameEntry = self.name[n]
        actionEntry = self.b[y]
        filename = nameEntry+actionEntry+".txt"
        print("File name: ", filename)

        # Entering information into files:
        if x == 1:
            value = input("Please enter information regarding " + actionEntry + " for " + nameEntry + " \n" )
    
            try:
                with open(filename, "a") as f:   
                    # printing date and time
                    f.write(str([str(self.getdate())]) + ": " + nameEntry.title() + ": " + value + "\n")
                    print("Successfully written.")
                    return "Successfully written."
            except IOError as io:
                print(io)
                return str(io)
        
        # Reading information from files:
        elif x == 2:
            # printing date and time
            try:         
                with open(filename, "r") as f:
                    a = f.read()
                    print(a)
                    f.close()
                    return "Succesfully read file."
            except IOError as io:
                print(io)
                return str(io)
        else:
            return "Invalid argument(s) entered."

if __name__ == '__main__':
    manage = HealthManagement()
    manage.addname()
    name = manage.selectname()
    file_action = manage.select_file_action()
    task = manage.select_task()
    manage.action(name, file_action, task)