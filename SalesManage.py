import numpy as np

class Sales:

    class Sale:
        def __init__(self,pid,name,cost,revenue,quantity):
            self.pid=pid
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.quantity=quantity

    listOfProductsSale=[]
    totalRevenue=0
    COGS=0


    def productSaleAdd(self,pid,name,cost,revenue,noOfProductSale):
        self.listOfProductsSale.append(self.Sale(pid,name,cost,revenue,noOfProductSale))


    def saleInput(self,pdct): 
        
        for i in pdct.allProduct:
            
            noOfProductSale=int(input(str(i.pid)+" " +i.name+" quantity sale : "))
            self.listOfProductsSale.append(self.Sale(i.pid,i.name,i.cost,i.revenue,noOfProductSale))
            # print(i.revenue)
            self.totalRevenue+=(noOfProductSale*i.cost)
            self.COGS+=(noOfProductSale*(i.cost-i.revenue))

        return self.totalRevenue
    
    def viewSaleDetails(self):
        choice=input("(1)View All Product Sale (2)View Particular Product Sale")
        if choice=="1":
            self.viewAllProductSale()
        elif choice=="2":
            pid=int(input("Enter Product Id : "))
            for i in self.listOfProductsSale:
                if i.pid==pid:
                    print((i.pid,i.name,i.cost,i.revenue,i.noOfProductSale))
                    print()
        
        else:
            print("Invalid Option try again...")

    def viewAllProductSale(self):
        for i in self.listOfProductsSale:
            print((i.pid,i.name,i.cost,i.revenue,i.noOfProductSale))
            print()