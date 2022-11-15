from genericpath import exists


class EmailStore:

    def __init__(self):
    
        self.emails = []

    def exists(self, email):
        '''
        Method that checks if an email exists in store.
        '''
        return email in self.emails

    def add(self, first_name, last_name):

        '''
        Method that adds a new email to the store.
        The email address is of the format {first_name}.{last_name}{count}@marist.edu
    
        @return the email that was added.
        '''
        email = None
        if first_name == None or last_name == None:
            raise Exception("first/last name cannot be None!")
        
        # TODO use a while loop to construct email from first_name and last_name and check if it exists.   
        count = 1   
        while True:
            email = f"{first_name.lower()}.{last_name.lower()}{count}@marist.edu"
            if self.exists(email):
                count += 1
                continue
            else:
                self.emails.append(email)
                break
        return email

    def remove(self, email):
        '''
        Method that removes an email from the store.
        '''
        if not self.exists(email):
            raise Exception("The email doest not exist!")
        self.emails.remove(email)
