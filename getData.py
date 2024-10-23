import pymongo
from utils.ProductManage import Products
from utils.SalesManage import Sales
from utils.MonthDetails import Month
from utils.Business import Business
from utils.EmployeeManage import Employees 


#Connection With Database
# print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
# print(client)
db=client["FinancePotfolio"]
collection=db["business"]


def getFromDB():
    return collection.find()


def reStart():
    allBusiness=getFromDB()
    
    allBusinessForMain=[]

    for i in allBusiness:
        password=i["password"]
        bid=i["bid"]
        name=i["name"]
        debt={"amount":i["debt"]["amount"],"Total_EMI":i["debt"]["Total_EMI"],"paidedEMI":i["debt"]["paidedEMI"],"persentage":i["debt"]["persentage"]}
        haveEquity=i["haveEquity"]
        assets=i["assets"]

        currentYearMonths=[]
        for j in i["currentYearMonths"]:
            currentYearMonths.append(createMonthObj(j))
        years=[]
        for j in i["years"]:
            allM=[]
            for k in j:
                allM.append(createMonthObj(k))
            years.append
        profit=i["profit"]
        annualRevenueRunRate=i["annualRevenueRunRate"]
        currentYearRevenue=i["currentYearRevenue"]
        

        b=Business(password,bid,name)
        b.debt=debt
        b.haveEquity=haveEquity
        b.assets=assets
        b.currentYearMonths=currentYearMonths
        b.years=years
        b.profit=profit
        b.annualRevenueRunRate=annualRevenueRunRate
        b.currentYearRevenue=currentYearRevenue
        b.productObjectForBusiness=createProductObj(i["product"])
        b.employeeObjectForBusiness=createEmployeeObj(i["employee"])
        
        allBusinessForMain.append(b)
       
    return allBusinessForMain


def createEmployeeObj(emp):
    employee=Employees()
    for j in emp["employeesDetails"]:
        employee.addEmployee(j["eid"],j["name"],j["designation"],j["salary"],j["x"])

    return employee


def createProductObj(pdct):
    product=Products()
        # product.

    for j in pdct["allProduct"]:
        product.addProduct(j["pid"],j["name"],j["cost"],j["revenue"],j["x"])
    
    return product


def createSalesObj(s):
    sale=Sales()
    listOfProductSale=[]
    totalRevenue=s["totalRevenue"]
    COGS=s["COGS"]
    for i in s["listOfProductsSale"]:
        sale.productSaleAdd(i["pid"],i["name"],i["cost"],i["revenue"],i["quantity"])
    return sale


def createMonthObj(m):
    revenue=m["revenue"]
    debt={"amount":m["debt"]["amount"],"Total_EMI":m["debt"]["Total_EMI"],"paidedEMI":m["debt"]["paidedEMI"],"persentage":m["debt"]["persentage"]}
    haveEquity=m["haveEquity"]
    EBITDA=m["EBITDA"]
    assets=m["assets"]
    marketing=m["marketing"]
    grossProfit=m["grossProfit"]
    netProfit=m["netProfit"]
    totalSalaries=m["totalSalaries"]
    COGS=m["COGS"]
    totalTaxes=m["totalTaxes"]
    other=m["other"]
    sales=createSalesObj(m["sales"])
    shareMarket=m["shareMarket"]

    monthObj=Month(revenue,debt,haveEquity,EBITDA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,sales,shareMarket)
    return monthObj