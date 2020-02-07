import sqlite3
conn = sqlite3.connect('OS_Employee.db')
import pandas as pd
xl = pd.ExcelFile("SalesData.xlsx")
OrderData = xl.parse("Orders")
lines ="\n" + "#"*50 + "\n"

def login():

    User_Email = input("Please enter your Email to login: ")
    while not User_Email:
        User_Email = input("Email cannot be blank. Please enter your Email, again: ")
    User_Password = input("Please enter your password: ")
    while not User_Password:
        User_Password = input("Password cannot be blank. Please enter your password,again: ")

    with conn:
        cur= conn.cursor()
        try:
            selectquery = "SELECT COUNT (*) FROM Employee WHERE (Email = '" + User_Email + "'AND Password = '" + User_Password + "')"
            cur.execute(selectquery)
            
            results = cur.fetchone()
            
            if results[0] == 1:
                print("Login successful.")
                menu()
            else:
                print("Login unsucessful.")
                login()

        except:
            print("Connected Failed.")          
login()

def registration():
    print("Welcome to company! Registration for new employee.\n")
 
    with conn:
   
        cur=conn.cursor()

        try:

            ID=""
            fname=""
            lname=""
            an_email=""
            p_word=""

            while not ID:

                ID=input("Enter the employee ID:  ".strip())
    
                if ID:
                    ID=int(ID)
 
                    CheckID="SELECT COUNT(*) FROM Employee WHERE EmployeeID=%d" % (ID)
                    cur.execute(CheckID)
                    results=cur.fetchone()             
                    rows=results[0]
                    if rows==1:
                        print('ID already exists. Try another ID. \n')
                        ID=""
                        continue
                  
                else:
                    print("ID was blank. Please enter the new employee ID, again.")
                    
            while not fname:

                fname=input("Enter the first name: ".strip())
              
                if not fname:
                    print("First name was blank. Please enter the first name, again.")
                else:
                    fname=fname.title()
   
            while not lname:

                lname=input("Enter the last name: ".strip())
              
                if not lname:
                    print("Last name was blank. Please nter the last name, again.")
                else:
                    lname=lname.title()

            while not an_email:
               
                an_email=input("Enter the Email: ".strip())
              
                if not an_email:
                    print("Email was blank. Enter the email, again.")
                else:
                    an_email=an_email.lower()

            while not p_word:

                p_word=input("Enter the p_word: ".strip())
              
                if not p_word:
                    print("Password is blank. Please enter the password, again")
                else:
                    p_word=p_word.lower()
    
            InsertValue = "INSERT INTO Employee VALUES ('{}','{}','{}','{}','{}')"
            InsertString = InsertValue.format(ID, fname.title(), lname.title(), an_email, p_word.lower())
            cur.execute(InsertString)
            cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(ID))
            results = cur.fetchone()
            print(results)
            login()

        except:
            print("Connection failed. ID must be numbers.\n")
            registration()

 

def update():
    conn = sqlite3.connect('OS_Employee.db')
    print("\n ******* Update information ******* \n 1. Password \n 2. First Name \n 3. Last Name \n 4. Email \n 5. Return Main Menu")
    choice = input("Please enter number to update: ")
    
    if choice == "1":
        with conn:
            cur = conn.cursor()   
            try:
                EmpID = input("Please enter your Employee ID: ")
                OldPassword = input("Please enter your old password: ")
                NewPassword = input("Please enter your new password: ")
                    
                UpdateValue = "UPDATE Employee SET Password = ('{}') WHERE (EmployeeID = ('{}') AND Password = ('{}'))"
                UpdateString = UpdateValue.format(NewPassword, EmpID, OldPassword)
                cur.execute(UpdateString)
                cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(EmpID))
                results = cur.fetchone()
                if results:
                    print (results)
                    cont = input("Update another? (y/n): ")
                    if cont == "y":
                        update()
                    else: 
                        menu()
                else:
                    print("\n ID and password don't match. Check it")
                    option = input("Do you want to try again? (y/n): ")
                    if option =="y":
                        update()
                    else:
                        menu()
    
            except:
                print("\n ID and old password don't exist. Try again \n ")
                update()
                
    elif choice == "2":
        with conn:
            cur = conn.cursor()   
            try:
                EmpID = input("Please enter your Employee ID: ")
                OldFName = input("Please enter your old first name (Xxxx): ")
                NewFName = input("Please enter your first name (Xxxx): ")
                    
                UpdateValue = "UPDATE Employee SET FirstName = ('{}') WHERE (EmployeeID = ('{}') AND FirstName = ('{}'))"
                UpdateString = UpdateValue.format(NewFName, EmpID, OldFName)
                cur.execute(UpdateString)
                cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(EmpID))
                results = cur.fetchone()
                if results:
                    print (results)
                    cont = input("Update another? (y/n): ")
                    if cont == "y":
                        update()
                    else: 
                        menu()
                else:
                    print("\n ID or Old First Name don't match. Check it")
                    option = input("Do you want to try again? (y/n): ")
                    if option =="y":
                        update()
                    else:
                        menu()
    
            except:
                print("\n ID and old first name don't match. Capital the first letter of your last name \n")
                update()
                
    elif choice == "3":
        with conn:
            cur = conn.cursor()
            try:
                EmpID = input("Please enter your Employee ID: ")
                OldLName = input("Please enter your old last name (Xxxx): ")
                NewLName = input("Please enter your new last name (Xxxx): ")
                    
                UpdateValue = "UPDATE Employee SET LastName = ('{}') WHERE (EmployeeID = ('{}') AND LastName = ('{}'))"
                UpdateString = UpdateValue.format(NewLName, EmpID, OldLName)
                cur.execute(UpdateString)
                cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(EmpID))
                results = cur.fetchone()
                print(results)
                cont = input("Update another? (y/n): ")
                if results:
                    print (results)
                    cont = input("Update another? (y/n): ")
                    if cont == "y":
                        update()
                    else: 
                        menu()
                else:
                    print("\n ID or Old Last Name don't match. Check it")
                    option = input("Do you want to try again? (y/n): ")
                    if option =="y":
                        update()
                    else:
                        menu()

            except:
                print("\n ID and old last name don't exist. Capital the first letter of your last name.")
                update()
                
    elif choice == "4":
        with conn:
            cur = conn.cursor()
            try: 
                EmpID = input("Please enter your Employee ID: ")
                OldEmail = input("Please enter your old email: ")
                NewEmail = input("Please enter your email: ")
                    
                UpdateValue = "UPDATE Employee SET Email = ('{}') WHERE (EmployeeID = ('{}') AND Email = ('{}'))"
                UpdateString = UpdateValue.format(NewEmail, EmpID, OldEmail)
                cur.execute(UpdateString)
                cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(EmpID))
                results = cur.fetchone()
                if results:
                    print (results)
                    cont = input("Update another? (y/n): ")
                    if cont == "y":
                        update()
                    else: 
                        menu()
                else:
                    print("\n ID or Old First Name don't match. Check it")
                    option = input("Do you want to try again? (y/n): ")
                    if option =="y":
                        update()
                    else:
                        menu()
    
            except:
                print("\n ID and old email don't exist. Try again. \n ")
                update()
 
        
    elif choice == "5":
        menu()
            
    else:
        print("Number does not exist.")
        update()
    
def top_sales_region():
    print("The top-selling item per region.")
    print("\n 1.West \n 2.Central \n 3.South \n 4.East \n 5.Return Main Menu.")
    print(("*"*50))

    choice = input("Please enter the number of region: ")
    if choice == "1":
        
        print("**** Category in West ****: \n 1.Funiture \n 2.Office Supplies \n 3.Technology")
        
        nchoice = input("Enter the number of category: ")
        #print(("*"*50))
        
        if nchoice == "1":
       
            Product_Sales = OrderData.loc[OrderData['Region'] == "West"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Furniture", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of furniture in West: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option =input("Check another? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
            
        elif nchoice == "2":
            Product_Sales = OrderData.loc[OrderData['Region'] == "West"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Office Supplies", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of office supplies in West: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option =input("Check another? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
            
        elif nchoice =="3":
            Product_Sales = OrderData.loc[OrderData['Region'] == "West"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Technology", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of technology in West: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
        else:
            print("Number does not exist! Try again \n.")
            print("*"*50)
            top_sales_region()
        
    elif choice =="2":
        
        print("**** Category in Central ****: \n 1.Funiture \n 2.Office Supplies \n 3.Technology")
        
        nchoice = input("Enter the number of category: ")
        print(("*"*50))
        if nchoice == "1":
            Product_Sales = OrderData.loc[OrderData['Region'] == "Central"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Furniture", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of furniture in Central: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
            
        elif nchoice == "2":
            Product_Sales = OrderData.loc[OrderData['Region'] == "Central"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Office Supplies", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of office supplies in Central: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
        
        elif nchoice == "3":
            Product_Sales = OrderData.loc[OrderData['Region'] == "Central"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Technology", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of technology in Central: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
            
        else: 
            print("Number does not exist! Try again \n.")
            top_sales_region()
    
    elif choice == "3": 
    
        print("**** Category in South ****: \n 1.Funiture \n 2.Office Supplies \n 3.Technology")
        
        nchoice = input("Enter the number of category: ")
        #print(("*"*50))
        if nchoice == "1":
            Product_Sales = OrderData.loc[OrderData['Region'] == "South"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Furniture", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of furniture in South: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
                
        elif nchoice == "2":
            Product_Sales = OrderData.loc[OrderData['Region'] == "South"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Office Supplies", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("Top 5 items selling of office supplies in South: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                top_sales_region()
            else: 
                menu()
        
        elif nchoice == "3":
            Product_Sales = OrderData.loc[OrderData['Region'] == "South"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Technology", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("\n Top 5 items selling of technology in South: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
        
        else:
            print("Number does not exist! Try again \n.")
            top_sales_region()
            
    elif choice == "4":
        print("**** Category in South ****: \n 1.Funiture \n 2.Office Supplies \n 3.Technology")
        nchoice = input("Enter the number of category: ")
        #print(("*"*50))
        if nchoice == "1": 
            Product_Sales = OrderData.loc[OrderData['Region'] == "East"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Furniture", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("Top 5 items selling of furniture in East: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
            
        elif nchoice == "2":
            Product_Sales = OrderData.loc[OrderData['Region'] == "East"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Office Supplies", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("Top 5 items selling of office supplies in East: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
            
        elif nchoice == "3":
            Product_Sales = OrderData.loc[OrderData['Region'] == "East"]
            Product_Sales = Product_Sales.loc[Product_Sales['Category']=="Technology", ["Sub-Category","Sales"]]
            Product_Sales_result = Product_Sales.groupby(["Sub-Category"]).sum().sort_values(by = "Sales", ascending = False)
            Product_Sales_result = Product_Sales_result.reset_index()
            print("Top 5 items selling of technology in East: ")
            print(Product_Sales_result.head(5))
            print(lines)
            option=input("Check another ? (y/n): ")
            if option =='y':
                print()
                top_sales_region()
            else: 
                menu()
        
        else:
            print("Number does not exist! Try again \n.")
            top_sales_region()


    elif choice =="5":
        menu()
    
    else:
        print("Number does not exist\n")
        top_sales_region()
        
        
def top_segment():
    print("****** Segment ****** ")
    print("\n 1.Consumer \n 2.Corporate \n 3.Home Office \n 4.Return Main Menu")
    
    choice = input("Please enter the number to selecte segment: ")
    
    if choice == "1":
        print("*****To test*****:\n 1.Highest Profit \n 2.Highest Sales \n 3.Highest Quantity. ")
        
        nchoice = input("Enter the number: ")
        #print("*"*50)
        if nchoice == "1":
            Consumer_HighestProfits = OrderData.loc[OrderData['Segment']=="Consumer", ["Customer ID","Customer Name","Profit"]]
            Consumer_HighestProfits_result = Consumer_HighestProfits.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Profit", ascending = False)
            Consumer_HighestProfits_result = Consumer_HighestProfits_result.reset_index()
            print("Five Consumers have the highest sales: ")
            print(Consumer_HighestProfits_result.head(5))
            print(lines)

            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
          
        elif nchoice == "2":
            Consumer_HighestSales = OrderData.loc[OrderData['Segment']=="Consumer", ["Customer ID","Customer Name","Sales"]]
            Consumer_HighestSales_result = Consumer_HighestSales.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Sales", ascending = False)
            Consumer_HighestSales_result = Consumer_HighestSales_result.reset_index()
            print("Five Consumers have the highest profits: ")
            print(Consumer_HighestSales_result.head(5))
            print(lines)
            
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
            
            
        elif nchoice == "3":
            Consumer_HighestQuantity = OrderData.loc[OrderData['Segment']=="Consumer", ["Customer ID","Customer Name","Quantity"]]
            Consumer_HighestQuantity_result = Consumer_HighestQuantity.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Quantity", ascending = False)
            Consumer_HighestQuantity_result = Consumer_HighestQuantity_result.reset_index()
            print("Five Consumers have the highest profits: ")
            print(Consumer_HighestQuantity_result.head(5))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
            
        else: 
            print("Number does not exist. Try again! \n")
            top_segment()
            
    elif choice == "2":
        print("***** To test *****:\n 1.Highest Profit \n 2.Highest Sales \n 3.Highest Quantity. ")
        
        nchoice = input("Enter the number: ")
        #print("*"*50)
        
        if nchoice == "1":
            Corporate_HighestProfits = OrderData.loc[OrderData['Segment']=="Corporate", ["Customer ID","Customer Name","Profit"]]
            Corporate_HighestProfits_result = Corporate_HighestProfits.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Profit", ascending = False)
            Corporate_HighestProfits_result = Corporate_HighestProfits_result.reset_index()
            print("Five Corporates have the highest sales: ")
            print(Corporate_HighestProfits_result.head(5))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
            
            
        elif nchoice == "2": 
            Corporate_HighestSales = OrderData.loc[OrderData['Segment']=="Corporate", ["Customer ID","Customer Name","Sales"]]
            Corporate_HighestSales_result = Corporate_HighestSales.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Sales", ascending = False)
            Corporate_HighestSales_result = Corporate_HighestSales_result.reset_index()
            print("Five Corporates have the highest profits: ")
            print(Corporate_HighestSales_result.head(5))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
            
        
        elif nchoice == "3":
            Corporate_HighestQuantity = OrderData.loc[OrderData['Segment']=="Corporate", ["Customer ID","Customer Name","Quantity"]]
            Corporate_HighestQuantity_result = Corporate_HighestQuantity.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Quantity", ascending = False)
            Corporate_HighestQuantity_result = Corporate_HighestQuantity_result.reset_index()
            print("Five Consumers have the highest profits: ")
            print(Corporate_HighestQuantity_result.head(5))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
            
        else:
            print("Number does not exist. Try again! \n")
            top_segment()
    
    elif choice == "3":
        print("***** To test *****:\n 1.Highest Profit \n 2.Highest Sales \n 3.Highest Quantity. ")
        
        nchoice = input("Enter the number to identify the finacial statement: ")
        #print("*"*50)
                        
        if nchoice == "1":
            HomeOffice_HighestProfits = OrderData.loc[OrderData['Segment']=="Home Office", ["Customer ID","Customer Name","Profit"]]
            HomeOffice_HighestProfits_result = HomeOffice_HighestProfits.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Profit", ascending = False)
            HomeOffice_HighestProfits_result = HomeOffice_HighestProfits_result.reset_index()
            print("Five Home Offices have the highest sales: ")
            print(HomeOffice_HighestProfits_result.head(5))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                top_segment()
            else: 
                menu()

               
        elif nchoice == "2": 
            HomeOffice_HighestSales = OrderData.loc[OrderData['Segment']=="Home Office", ["Customer ID","Customer Name","Sales"]]
            HomeOffice_HighestSales_result = HomeOffice_HighestSales.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Sales", ascending = False)
            HomeOffice_HighestSales_result = HomeOffice_HighestSales_result.reset_index()
            print("Five Home Offices have the highest profits: ")
            print(HomeOffice_HighestSales_result.head(5))
            print(lines)

            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
                
        elif nchoice == "3":
            HomeOffice_HighestQuantity = OrderData.loc[OrderData['Segment']=="Home Office", ["Customer ID","Customer Name","Quantity"]]
            HomeOffice_HighestQuantity_result = HomeOffice_HighestQuantity.groupby(["Customer ID","Customer Name"]).sum().sort_values(by = "Quantity", ascending = False)
            HomeOffice_HighestQuantity_result = HomeOffice_HighestQuantity_result.reset_index()
            print("Five Consumers have the highest profits: ")
            print(HomeOffice_HighestQuantity_result.head(5))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                top_segment()
            else: 
                menu()
                 
        else:
            print("Number does not exist. Try again! \n")
            top_segment()
            
    elif choice =="4":
        menu()
    
    else:
        print("Number does not exist\n")
        top_segment()

def discount_eff():
    print("****** Category ****** ")
    print("\n 1.Office Furniture \n 2.Office Supplies \n 3.Technology \n 4.Return Main Menu")
    
    choice = input("Please enter the number to selecte the category: ")
    
    if choice == "1":
        print("***** In Furnityre - Discount effects in  *****:\n 1.Highest Sales \n 2.Losses Profit \n 3.Return to Main Menu. ")
        
        nchoice = input("Enter the number: ")
        #print("*"*50)
        if nchoice == "1":
            Discount_HighestSales = OrderData.loc[OrderData['Category']=="Furniture", ["Discount","Sales"]]
            Discount_HighestSales_result = Discount_HighestSales.groupby(["Discount"]).sum().sort_values(by = "Sales", ascending = False)
            Discount_HighestSales_result = Discount_HighestSales_result.reset_index()
            print("The sale has increased by this discount: ")
            print(Discount_HighestSales_result.head(1))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                discount_eff()
            else: 
                menu()
          
        elif nchoice == "2":
            Discount_LossesProfit = OrderData.loc[OrderData['Category']=="Furniture", ["Discount","Profit"]]
            Discount_LossesProfit_result = Discount_LossesProfit.groupby(["Discount"]).sum().sort_values(by = "Profit", ascending = False)
            Discount_LossesProfit_result = Discount_LossesProfit_result.reset_index()
            print("The profit has lose by this discount: ")
            print(Discount_LossesProfit_result.tail(1))
            print(lines)

            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                discount_eff()
            else: 
                menu()
        
        elif nchoice == "3":
            menu()
            
        else: 
            print("Number does not exist. Try again! \n")
            discount_eff()
            
    elif choice == "2":
        print("***** In Supplies - Discount effects *****:\n 1.Highest Sales \n 2.Losses Profit \n 3.Return to Main Menu. ")
        
        nchoice = input("Enter the number: ")
        print("*"*50)
        
        if nchoice == "1":
            Discount_HighestSales = OrderData.loc[OrderData['Category']=="Office Supplies", ["Discount","Sales"]]
            Discount_HighestSales_result = Discount_HighestSales.groupby(["Discount"]).sum().sort_values(by = "Sales", ascending = False)
            Discount_HighestSales_result = Discount_HighestSales_result.reset_index()
            print("The sale has increased by this discount: ")
            print(Discount_HighestSales_result.head(1))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                discount_eff()
            else: 
                menu()
            
            
        elif nchoice == "2": 
            Discount_LossesProfit = OrderData.loc[OrderData['Category']=="Office Supplies", ["Discount","Profit"]]
            Discount_LossesProfit_result = Discount_LossesProfit.groupby(["Discount"]).sum().sort_values(by = "Profit", ascending = False)
            Discount_LossesProfit_result = Discount_LossesProfit_result.reset_index()
            print("The profit has lose by this discount: ")
            print(Discount_LossesProfit_result.tail(1))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                discount_eff()
            else: 
                menu()
            
        
        elif nchoice == "3":
            print()
            
        else:
            print("Number does not exist. Try again! \n")
            discount_eff()
    
    elif choice == "3":
        print("***** Discount effects*****:\n 1.Highest Sales \n 2.Losses Profit \n 3.Return to Main Menu. ")
        
        nchoice = input("Enter the number to identify the finacial statement: ")
        print("*"*50)
                        
        if nchoice == "1":
            Discount_HighestSales = OrderData.loc[OrderData['Category']=="Technology", ["Discount","Sales"]]
            Discount_HighestSales_result = Discount_HighestSales.groupby(["Discount"]).sum().sort_values(by = "Sales", ascending = False)
            Discount_HighestSales_result = Discount_HighestSales_result.reset_index()
            print("The sale has increased by this discount: ")
            print(Discount_HighestSales_result.head(1))
            print(lines)
            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                discount_eff()
            else: 
                print("Bye!")

               
        elif nchoice == "2": 
            Discount_LossesProfit = OrderData.loc[OrderData['Category']=="Technology", ["Discount","Profit"]]
            Discount_LossesProfit_result = Discount_LossesProfit.groupby(["Discount"]).sum().sort_values(by = "Profit", ascending = False)
            Discount_LossesProfit_result = Discount_LossesProfit_result.reset_index()
            print("The profit has lose by this discount: ")
            print(Discount_LossesProfit_result.tail(1))
            print(lines)

            option = input("Check another  (y/n)? ")
            if option =='y':
                print()
                discount_eff()
            else: 
                print("Bye!")
                
        elif nchoice == "3":
            main()
                 
        else:
            print("Number does not exist. Try again! \n")
            discount_eff()
            
    elif choice =="4":
        menu()
    
    else:
        print("Number does not exist\n")
        discount_eff()
        
def menu():
    print("(っ◔◡◔)っ ♥ Main Menu ♥")
    print("1). Input New Users Information.")
    print("2). Identify top-selling items per region.") 
    print("3). View Top Customers for Loyalty Program.")
    print("4). View Discount Impact on Profit")
    print("5). Update employee information.")
    print("6). Log-out." )

def main():
    while True:
        command = input("Command: ")
        if command == "1":
            registration()
        elif command == "2":
            top_sales_region()
        elif command == "3":
            top_segment()
        elif command == "4":
            discount_eff()
        elif command =="5":
            update()
        elif command == "6":
            print("Bye!")
            break
        else: 
            print("Number does not exist. Enter 6 to exit")
main()
        
