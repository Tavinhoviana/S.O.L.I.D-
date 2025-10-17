class Programmer:
    def make(self):
        print("programmer creating code")

class Seller:
    def make(self):
        print("Selling the product")

class Company:
    def do_work(self, worker: any) -> None:
        worker.make()

Programmer = Programmer()
Seller = Seller()

company = Company()
company.do_work(Programmer)
company.do_work(Seller)
