import pymongo


#Connection With Database
print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
print(client)
db=client["FinancePotfolio"]
collection=db["business"]



def updatePasswordForManagerInDB(b):
    collection.update_one({"bid":b.bid},{"$set" :{"password":b.password}})


def updateBusinessID(b):
    collection.update_one({"name:":b.name},{"$set" :{"bid":b.bid}})


def updateBusinessName(b):
    collection.update_one({"bid":b.bid},{"$set" :{"name":b.name}})


def updateBusinessEquity(b):
    collection.update_one({"bid":b.bid},{"$set" :{"haveEquity":b.haveEquity}})


def updateBusinessAssets(b):
    collection.update_one({"bid":b.bid},{"$set" :{"assets":b.assets}})


def updateBusinessDebt(b):
    collection.update_one({"bid":b.bid},{"$set" :{"debt":{"amount":b.debt["amount"],"Total_EMI":b.debt["Total_EMI"],"paidedEMI":b.debt["paidedEMI"],"persentage":b.debt["persentage"]}}})


def updateBusinessProductDetails(b):
    allProduct=[]
    for i in b.productObjectForBusiness.allProduct:
        allProduct.append({"pid":i.pid,"name":i.name,"cost":i.cost,"revenue":i.revenue,"x":i.x})

    collection.update_one({"bid":b.bid},{"$set" :{"product":{"allProduct":allProduct}}})


def updateBusinessEmployeeDetails(b):
    employeesDetails=[]
    for i in b.employeeObjectForBusiness.employeesDetails:
        employeesDetails.append({"eid":i.eid,"name":i.name,"designation":i.designation,"salary":i.salary,"x":i.x})

    collection.update_one({"bid":b.bid},{"$set" :{"employee":{"employeesDetails":employeesDetails}}})


def updateBusinessCurrentYearMonth(b):
    mlist=[]
    
    for i in b.currentYearMonths:
        mlist.append(getmonthDictionry(i))

    collection.update_one({"bid":b.bid},{"$set" :{"currentYearMonths":mlist}})
    collection.update_one({"bid":b.bid},{"$set" :{"annualRevenueRunRate":b.annualRevenueRunRate}})
    collection.update_one({"bid":b.bid},{"$set" :{"currentYearRevenue":b.currentYearRevenue}})


def updateBusinessYears(b):
    Y=[]

    for y in b.years:
        allM=[]
        for m in y:
            allM.append(getmonthDictionry(m))
        Y.append(allM) 

    collection.update_one({"bid":b.bid},{"$set" :{"years":Y}})


def insertInDB(b):
    CYM=[]
    for m in b.currentYearMonths:
        CYM.append(getmonthDictionry(m))
    
    Y=[]
    for y in b.years:

        allM=[]
        for m in y:
            allM.append(getmonthDictionry(m))

        Y.append(allM)   
    
    employeesDetails=[]
    for i in b.employeeObjectForBusiness.employeesDetails:
        employeesDetails.append({"eid":i.eid,"name":i.name,"designation":i.designation,"salary":i.salary,"x":i.x})
    
    allProduct=[]
    for i in b.productObjectForBusiness.allProduct:
        allProduct.append({"pid":i.pid,"name":i.name,"cost":i.cost,"revenue":i.revenue,"x":i.x})

    collection.insert_one({
        "password":b.password,
        "bid":b.bid,
        "name":b.name,
        "debt":{
            "amount":b.debt["amount"],
            "Total_EMI":b.debt["Total_EMI"],
            "paidedEMI":b.debt["paidedEMI"],
            "persentage":b.debt["persentage"]
        },
        "haveEquity":b.haveEquity,
        "assets":b.assets,
        "currentYearMonths":CYM,
        "years":Y,
        "profit":b.profit,
        "annualRevenueRunRate":b.annualRevenueRunRate,
        "currentYearRevenue":b.currentYearRevenue,
        "product":{
            "allProduct":allProduct
        },
        "employee":{
            "employeesDetails":employeesDetails
        }
    })


def getmonthDictionry(m):
    sale=m.sales
    listOfProductsSale=[]

    for i in sale.listOfProductsSale:
        listOfProductsSale.append({"pid":i.pid,"name":i.name,"cost":i.cost,"revenue":i.revenue,"quantity":i.quantity})

    monthDic={
        "revenue":m.revenue,
        "debt":{
            "amount":m.debt["amount"],
            "Total_EMI":m.debt["Total_EMI"],
            "paidedEMI":m.debt["paidedEMI"],
            "persentage":m.debt["persentage"]
        },
        "haveEquity":m.haveEquity,
        "EBITDA":m.EBITDA,
        "assets":m.assets,
        "marketing":m.marketing,
        "grossProfit":m.grossProfit,
        "netProfit":m.netProfit,
        "totalSalaries":m.totalSalaries,
        "COGS":m.COGS,
        "totalTaxes":m.totalTaxes,
        "other":m.other,
        "sales":{
            "listOfProductsSale":listOfProductsSale,
            "totalRevenue":sale.totalRevenue,
            "COGS":sale.COGS
        },
        "shareMarket":{}
    }

    return monthDic


def deleteEvery():
    collection.delete_many({})

# collection.update_one({"bid:":1},{"$set" :{"currentYearMonths":[]}})
# deleteEvery()