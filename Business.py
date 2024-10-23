import matplotlib.pyplot as plt
from utils.EmployeeManage import Employees 
from utils.ProductManage import Products
from utils.SalesManage import Sales
from utils.MonthDetails import Month
import Database.CRUD as db

class Business:

    def __init__(self,password,bid,name):
        self.password=password
        self.bid=bid
        self.name=name
        self.debt={"amount":0,"Total_EMI":0,"paidedEMI":0,"persentage":0}
        self.haveEquity=0
        self.assets=0
        self.currentYearMonths=[]
        self.years=[]
        self.profit=0
        self.annualRevenueRunRate=0
        self.currentYearRevenue=0
        self.productObjectForBusiness=Products()
        self.employeeObjectForBusiness=Employees()

    def owner(self):
        choice=None

        while choice!="3":
            print()
            choice=input("(1)View Chart For Analysis (2)View Table For Analysis (3)Generate Finance Matrix PDF (4)Change Some IMPORTANT Term (5)Exit \n")
            
            if choice=="1":
                self.viewChartForAnalysis()

            elif choice=="2":
                self.viewTableForAnalysis()

            elif choice=="3":
                self.generateFinanceMatrix() 

            elif choice=="4":
                self.changeIMPORTANTTerm()
            
            elif choice=="5":
                break

            else:
                print("Invalid Option")

    def viewChartForAnalysis(self):
        choice=input("(1)UnitEconomics Pie-Chart (2)Sale (3)Employee ")
        if choice=="1":

            activities=["COGS","Commissions,Logistics Packaging & Other","Performance Marketing","Salaries & Rent","EBITDA"]
            semiChoice=input("(1)Last Month (2)Current Year (3)Last 3 year")

            if semiChoice=="1":
                self.chartsUnitEconomicsForLastMonth(activities)

            elif semiChoice=="2":
                self.chartsUnitEconomicsForCurrentYear(activities)
            
            elif semiChoice=="3":
                self.chartsUnitEconomicsForLastYear(activities)

            else:
                print("invalid option try again...")

        elif choice=="2":
            pass

        else:
            print("invalid option")

    def chartsUnitEconomicsForLastMonth(self,activities):
            
            if self.currentYearMonths:
                m=self.currentYearMonths[len(self.currentYearMonths)-1]

            else:
                m=self.years[len(self.years)-1][11]
         
            revenue=m.revenue
            logistics=0
            if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
                logistics=self.debt["amount"]//self.debt["Total_EMI"]

            slices=[(m.COGS*100)/revenue,((logistics+m.other)*100)/revenue,(m.marketing*100)/revenue,(m.totalSalaries*100)/revenue,(m.EBITDA*100)/revenue]
            
            plt.pie(slices,labels=activities,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
            plt.legend()
            plt.show()


    def chartsUnitEconomicsForCurrentYear(self,activities):
        if self.currentYearMonths:
            logistics=0
            # if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            #     logistics=self.debt["amount"]//self.debt["Total_EMI"]
            m=self.calculateTermsInGivenTime(self.currentYearMonths)
            slices=[(m["COGS"]*100)/m["revenue"],((logistics+m["other"])*100)/m["revenue"],(m["marketing"]*100)/m["revenue"],(m["totalSalaries"]*100)/m["revenue"],(m["EBITDA"]*100)/m["revenue"]]
        
            plt.pie(slices,labels=activities,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
            plt.legend()
            plt.show()

            
    def chartsUnitEconomicsForLastYear(self,activities):
        if len(self.years)>=1:
            mList=[]
            for i in self.years:
                mList.append(i)
            m=self.calculateTermsInGivenTime(mList)
            logistics=0
            # if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            #     logistics=self.debt["amount"]//self.debt["Total_EMI"]

            slices=[(m["COGS"]*100)/m["revenue"],((logistics+m["other"])*100)/m["revenue"],(m["marketing"]*100)/m["revenue"],(m["totalSalaries"]*100)/m["revenue"],(m["EBITDA"]*100)/m["revenue"]]
        
            plt.pie(slices,labels=activities,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
            plt.legend()
            plt.show()

    
    def viewTableForAnalysis(self):
        thch=input("(1)Current Month (2)Current Year (3)Last 3 Year \n")

        if thch=="1":
            m=None
            if self.currentYearMonths:
                m=self.currentYearMonths[len(self.currentYearMonths)-1]
            else:
                m=self.years[len(self.years)-1][11]

            print(f"            *-* {self.name} *-*")
            print("--> Current Month : ")
            print("")
            print()
            print("haveEquity :",m.haveEquity)
            print("assets :",m.assets)
            print("Profit :",self.profit)
            print()
            print("Revenue :",m.revenue)

            print("COGS :",m.COGS)
            print("Gross Profit :",m.grossProfit)

            if m.debt["amount"]:
                print("•Dept : amount=",m.debt["amount"],"month left =",m.debt["Total_EMI"]-m.debt["paidedEMI"],"Persentage =",m.debt["persentage"])
            
            print("Marketing :",m.marketing)
            print("Salaries To Employees :",m.totalSalaries)
            print("Taxes :",m.totalTaxes)
            print("Other :",m.other)
            print()
            print("Net Profit :",m.netProfit)
            print("EBITDA :",m.EBITDA)
            print()
            print("Annual Revenue Run Rate :",self.annualRevenueRunRate)


        elif thch=="2":
            if self.currentYearMonths:
                m=self.calculateTermsInGivenTime(self.currentYearMonths)
                self.tableForAnalysis(m,"Current Year")
        
        elif thch=="3":
            if len(self.years)>=3:
                mList=[]
                for i in self.years[len(self.years)-1]:
                    mList.append(i)
                for i in self.years[len(self.years)-2]:
                    mList.append(i)
                for i in self.years[len(self.years)-3]:
                    mList.append(i)
                m=self.calculateTermsInGivenTime(mList)
                self.tableForAnalysis(m,"Last 3 Years")

        else:
            print("Invalid Option")


    def tableForAnalysis(self,m,time):
        print(f"            *-* {self.name} *-*")
        print("-->",time,": ")
        print("")
        print()
        print("Profit :",m["profit"])
        print()
        print("Revenue :",m["revenue"])

        print("COGS :",m["COGS"])
        print("Gross Profit :",m["grossProfit"])

        print("Marketing :",m["marketing"])
        print("Salaries To Employees :",m["totalSalaries"])
        print("Taxes :",m["totalTaxes"])
        print("Other :",m["other"])
        print()
        print("Net Profit :",m["netProfit"])
        print("EBITDA :",m["EBITDA"])
        print()


    def tableForAnalysisSaveInPDF(self,m,time):
        f=open("Finance_Portfolio.pdf","+w")
        f.write(f"            *-* {self.name} *-*\n")
        f.write("--> "+time+" : \n")
        f.write("\n")
        f.write("\n")
        f.write("Profit : "+str(m["profit"])+" \n")
        f.write("\n")
        f.write("Revenue : "+str(m["revenue"])+" \n")

        f.write("COGS : "+str(m["COGS"])+" \n")
        f.write("Gross Profit : "+str(m["grossProfit"])+" \n")

        f.write("Marketing : "+str(m["marketing"])+" \n")
        f.write("Salaries To Employees : "+str(m["totalSalaries"])+" \n")
        f.write("Taxes : "+str(m["totalTaxes"])+" \n")
        f.write("Other : "+str(m["other"])+" \n")
        f.write("\n")
        f.write("Net Profit : "+str(m["netProfit"])+" \n")
        f.write("EBITDA : "+str(m["EBITDA"])+" \n")
        f.close()
        print("All Data Saved in Finance_Portfolio.pdf file")


    def calculateTermsInGivenTime(self,givenTimeInMonth):
        ans={"profit":0,"revenue":0,"COGS":0,"grossProfit":0,"marketing":0,"totalSalaries":0,"totalTaxes":0,"other":0,"netProfit":0,"EBITDA":0}

        for m in givenTimeInMonth:
            ans["profit"]+=(m.netProfit*m.haveEquity)/100
            ans["revenue"]+=m.revenue
            ans["COGS"]+=m.COGS
            ans["grossProfit"]+=m.grossProfit
            ans["marketing"]+=m.marketing
            ans["totalSalaries"]+=m.totalSalaries
            ans["totalTaxes"]+=m.totalTaxes
            ans["other"]+=m.other
            ans["netProfit"]+=m.netProfit
            ans["EBITDA"]+=m.EBITDA

        return ans
    

    def generateFinanceMatrix(self):
        thch=input("(1)Current Month (2)Current Year (3)Last 3 Year \n")
        f=open("Finance_Portfolio.pdf","+w")
        m=None

        if self.currentYearMonths:
            m=self.currentYearMonths[len(self.currentYearMonths)-1]
        else:
            m=self.years[len(self.years)-1][11]

    
        if thch=="1":
            f.write(f"            *-* {self.name} *-*\n")
            f.write("--> Current Month : \n")
            f.write("\n")
            f.write("\n")
            f.write("haveEquity : "+str(m.haveEquity)+" \n")
            f.write("assets : "+str(m.assets)+" \n")
            f.write("Profit : "+str((m.netProfit*m.haveEquity)/100)+" \n")
            f.write("\n")
            f.write("Revenue : "+str(m.revenue)+" \n")

            f.write("COGS : "+str(m.COGS)+" \n")
            f.write("Gross Profit : "+str(m.grossProfit)+" \n")

            if m.debt["amount"]:
                f.write("•Dept : amount= "+str(m.debt["amount"])+" month left = "+str(m.debt["Total_EMI"]-m.debt["paidedEMI"])+" Persentage = "+str(m.debt["persentage"])+" \n")
            
            f.write("Marketing : "+str(m.marketing)+" \n")
            f.write("Salaries To Employees : "+str(m.totalSalaries)+ " \n")
            f.write("Taxes : "+str(m.totalTaxes)+" \n")
            f.write("Other : "+str(m.other)+" \n")
            f.write("\n")
            f.write("Net Profit : "+str(m.netProfit)+" \n")
            f.write("EBITDA : "+str(m.EBITDA)+" \n")
            f.write("\n")
            f.write("Annual Revenue Run Rate : "+str(self.annualRevenueRunRate)+" \n")
            f.close()
            print()
            print("All Data Saved in Finance_Portfolio.pdf file")

        elif thch=="2":
            if self.currentYearMonths:
                m=self.calculateTermsInGivenTime(self.currentYearMonths)
                self.tableForAnalysisSaveInPDF(m,"Current Year")
        
        elif thch=="3":
            if len(self.years)>=3:
                mList=[]
                for i in self.years[len(self.years)-1]:
                    mList.append(i)
                for i in self.years[len(self.years)-2]:
                    mList.append(i)
                for i in self.years[len(self.years)-3]:
                    mList.append(i)
                m=self.calculateTermsInGivenTime(mList)
                self.tableForAnalysisSaveInPDF(m,"Last 3 Years")

        else:
            print("invalid option try again....")


    def changeIMPORTANTTerm(self):
        semch=""
        while semch!="6":
            print()
            semch=input("(1)Business id (2)Business Name (3)haveEquity (4)assets (5)Debt (6)Exit\n")

            if semch=="1":
                newId=int(input("Enter New Business Id : "))
                self.bid=newId
                db.updateBusinessID(self)

            elif semch=="2":
                newName=input("Enter New Name For Business : ")
                self.name=newName
                db.updateBusinessName(self)

            elif semch=="3":
                newEquity=int(input("Enter New Business Equity : "))
                self.haveEquity=newEquity
                db.updateBusinessEquity(self)

            elif semch=="4":
                newAssets=int(input("Enter New Value Of Assets : "))
                self.assets=newAssets
                db.updateBusinessAssets(self)

            elif semch=="5":
                amount=float(input("Enter Amount Of Debt : "))
                totalMonth=int(input("If EMI Then Enter Total Month : "))
                persentage=float(input("Enter Persentage : "))
                self.debt={"amount":amount,"Total_EMI":totalMonth,"paidedEMI":0,"persentage":persentage}
                db.updateBusinessDebt(self)

            elif semch=="6":
                break

            else:
                print("Invalid Option")
                




    def manager(self):
        choice=None
        print("For Management Enter Number : ")
        
        while choice!="4":

            print()
            choice=input("(1)Add Month Details \n(2)Employee Management \n(3)Product Management \n(4)View Sale Details \n(5)View Chart For Analysis \n(6)View Table For Analysis \n(7)Generate Finance Matrix PDF \n(8)Exit \n")

            if choice=="1":
                saleObj=Sales()
                revenue=saleObj.saleInput(self.productObjectForBusiness)
                COGS=saleObj.COGS
                grossProfit=revenue-COGS
                
                debt=self.debt
                haveEquity=self.haveEquity
                assets=self.assets

                print()

                marketing=int(input("Enter Marketing Cost : "))
                depreciation=int(input("Enter Depreciation Cost : "))
                other=int(input("Enter Other Cost : "))

                totalSalaries=self.employeeObjectForBusiness.allEmployeeSalaryTotal()
                afterEMIProfit=self.currentDebtCalculation(grossProfit)
                IncomeBeforeTaxes=afterEMIProfit-marketing-depreciation-other-totalSalaries

                totalTaxes=self.taxCalculation(IncomeBeforeTaxes)  
                
                netProfit=IncomeBeforeTaxes-totalTaxes  
                self.profit=(netProfit*self.haveEquity)/100
                EBITDA=netProfit+depreciation+totalTaxes

                shareMarket=None
                if self.debt["amount"] and debt["Total_EMI"]:
                    EBITDA+=debt["amount"]/debt["Total_EMI"]

                m=Month(revenue,debt,haveEquity,EBITDA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,saleObj,shareMarket)
                
                self.storeDetails(m)

                
            elif choice=="2":
                self.employeeObjectForBusiness.employeeManagement()
                db.updateBusinessEmployeeDetails(self)

            elif choice=="3":
                self.productObjectForBusiness.productManagement()
                db.updateBusinessProductDetails(self)

            elif choice=="4":
                self.viewSaleDetails()

            elif choice=="5":
                self.viewChartForAnalysis()

            elif choice=="6":
                self.viewTableForAnalysis()

            elif choice=="7":
                self.generateFinanceMatrix()


            elif choice=="8":
                break

            else:
                print("INVALID Option")    


    def storeDetails(self,m):
        self.currentYearMonths.append(m)

        if len(self.currentYearMonths)==12:
            self.years.append(self.currentYearMonths)
            self.currentYearMonths.clear()
            db.updateBusinessYears(self)

        else:
            self.currentYearRevenue+=m.revenue
            self.annualRevenueRunRate=((self.currentYearRevenue/len(self.currentYearMonths))*12)
            db.updateBusinessCurrentYearMonth(self)


    def currentDebtCalculation(self,grossProfit):
        if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            emiPrice=self.debt["amount"]/self.debt["Total_EMI"]
            if emiPrice<grossProfit:
                afterEMIProfit=grossProfit-emiPrice
                self.debt={"amount":self.debt["amount"],"Total_EMI":self.debt["Total_EMI"],"paidedEMI":self.debt["paidedEMI"]+1,"persentage":self.debt["persentage"]}
                return afterEMIProfit
            else:
                return grossProfit
        else:
            return grossProfit
        

    def taxCalculation(self,IncomeBeforeTaxes):
        #corporate Tax  30% <1cr || 1<Pro>10 37% || >10cr 42%
        if IncomeBeforeTaxes<=0:
            return 0
        
        if IncomeBeforeTaxes>100000000:
            return (IncomeBeforeTaxes*42)/100
        
        if IncomeBeforeTaxes<10000000 and IncomeBeforeTaxes<=100000000:
            return (IncomeBeforeTaxes*37)/100
        
        return (IncomeBeforeTaxes*30)/100

        
    def viewSaleDetails(self):
        choice=input("(1)Last Month (2)Current Year (3)Last 3 year")

        if choice=="1":
            pass

        elif choice=="2":
            pass
        
        elif choice=="3":
            pass
        
        else:
            print("invalid option try again...")