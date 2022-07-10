from bank import Bank
class ABank:
    def __init__(self,loanamount:int,loanyear:int,loanrate:float) -> None:
        super().__init__()
        self.__loanamount = loanamount
        self.__loanyear = loanyear
        self.__loanrate = loanrate
        self.interest = 0
        self.monthlypay = 0

    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value

    @property
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    @property
    def loanrate(self):
        return self.__loanrate
    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value

    def flat_rate(self):
        self.interest = self.loanamount * (self.loanrate / 100) * self.loanyear
        return self.interest
        
    def flat_rate2(self):
        self.monthlypay = (self.loanamount + self.interest) / (self.loanyear * 12)
        return self.monthlypay

    def display_interest(self):
        print(f'***** {self.bankname} info *****')
        print(f'Loan : {self.loanamount:,.2f} baht')
        print(f'Rate : {self.loanrate}%')
        print(f'Year : {self.loanyear}')
        print(f'-- Interest --')
        print(f'interest : {self.flat_rate():,.2f} baht')
        print(f'Monthly Repayment : {self.flat_rate2():,.2f} baht')