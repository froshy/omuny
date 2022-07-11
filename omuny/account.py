class account():
    """
     A class to represent an account
    """

    def __init__(uname, pword):
        self.total_owed_to_others = 0
        self.total_owed_to_you = 0
        self.pword = pword
        self.uname = uname
        self.reports = {}
        self.owed_to_one = {}

    def get_owed_to_you(self, account) -> String:
        return account.owed_to_one[self]
    
    def get_owed(self, account) -> String:
        return self.owed_to_one[account]

    def get_total_owed_to_you(self) -> String:
        return self.total_owed_to_you

    def get_total_owed_to_others(self) -> String:
        return self.total_owed_to_others
    
    def get_uname(self) -> String:
        return self.uname

    def set_pword(self,pword) -> String:
        if verify_pword():
            self.pword = pword

    def add_owe_to_you(self) -> String:
        pass

    def add_owe_other(self) -> String:
        pass
    
    def verify_pword(vpword) -> bool:
        pass
    


    
    def __repr__() -> String:
        pass
    

    

