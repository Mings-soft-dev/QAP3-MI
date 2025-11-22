#A simple python program to keep track of sales for Harry's Used Car Lot
#Morgan Ings
#nov 17 2025


# Define required libraries.
import datetime


# Define program constants.
HST = 0.15
LICENSEFEE = 75
LICENSEFEEMORE = 165
LUXURYTAX = 0.016
FINANCINGFEE = 39.99

# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    print()
    print()
    print("Harry's Used Car Sales Invoice Generator")
    print()

    FName = input("Enter the buyer's first name(or End, to exit program): ").title()
    if FName == 'End':
        break
    elif FName == '':
        print("First name cannot be blank.")
        
    LName = input("Enter the buyer's last name: ").title()
    if LName == '':
        print("Last name cannot be blank.")

    PhoneNum = input("Enter the buyer's phone number (xxx-xxx-xxxx): ")
    if PhoneNum == '':
        print("Phone number cannot be blank.")
    elif len(PhoneNum) != 10:
        print("Phone number must be 10 digits long.")

    PlateNum = input("Enter the car's plate number (XXX123): ").upper()
    if PlateNum == '':
        print("Plate number cannot be blank.")
    elif len(PlateNum) != 6:
        print("Plate number must be 6 characters long.")

    CarMake = input("Enter the car's make: ").title()
    
    CarModel = input("Enter the car's model: ").title()
    
    CarYear = input("Enter the car's year (YYYY): ")
    
    SalePrice = float(input("Enter the sale price of the car: "))
    if SalePrice > 50000:
        print("Sale price cannot exceed $50,000.00 for used cars.")

    TradeInValue = float(input("Enter the trade-in value of the buyer's old car: "))
    if TradeInValue > SalePrice:
        print("Trade-in value cannot exceed the sale price of the car.")
    
    SalesPersonName = input("Enter the sales person's name: ").title()
    if SalesPersonName == '':
        print("Sales person's name cannot be blank.")


    #Get current date
    InvoiceDate = datetime.date.today()

    #First payment date
    FirstPaymentMonth = InvoiceDate.month + 1
    
    FirstPaymentYear = InvoiceDate.year
   
    if InvoiceDate.day > 25:
        FirstPaymentMonth += 1
    if FirstPaymentMonth > 12:
        FirstPaymentMonth = 1
        FirstPaymentYear += 1


    #Generate customer name and receipt ID
    CustomersName = FName[0] + ". " + LName

    ReceiptID = FName[0] + LName[0] + "-" + PlateNum[3:6] + "-" + PhoneNum[6:10]

    # Perform required calculations.
    PricePostTrade = SalePrice - TradeInValue

    #Calculateing License Fee
    if SalePrice <= 15000:
        LicenseFee = LICENSEFEE
    elif SalePrice >= 15001:
        LicenseFee = LICENSEFEEMORE

    #Caluclating Transfer fee
    if SalePrice <=20000:
        TransferFee = 0.01 * SalePrice
    elif SalePrice >=20001:
        TransferFee = (0.01 * SalePrice) + (LUXURYTAX * SalePrice)
    
    #Calculating totals
    SubTotal = PricePostTrade + LicenseFee + TransferFee
    
    HSTAmount = HST * SubTotal
    
    TotalAmount = SubTotal + HSTAmount

    
    #Format values for display
    SalePriceDsp = "${:,.2f}".format(SalePrice)
    TradeInValueDsp = "${:,.2f}".format(TradeInValue)
    PricePostTradeDsp = "${:,.2f}".format(PricePostTrade)
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    TransferFeeDsp = "${:,.2f}".format(TransferFee)
    SubTotalDsp = "${:,.2f}".format(SubTotal)
    HSTAmountDsp = "${:,.2f}".format(HSTAmount)
    TotalAmountDsp = "${:,.2f}".format(TotalAmount)
    
    
    InvoiceDateDsp = InvoiceDate.strftime("%m-%d-%Y")

    # Display results
    print()
    print()
    print(f"--------------------------------------------------------------------------------")
    print(f"Honest Harry's Car Sales                        Invoice Date:    {InvoiceDateDsp}")
    print(f"Used Car Sales Receipt                          Receipt No:       {ReceiptID}")
    print()
    print(f"                                         Sale price:             {SalePriceDsp}")
    print(f"Sold to:                                 Trade Allowance:        {TradeInValueDsp}")
    print(f"                                         --------------------------------------")
    print(f"     {CustomersName:<32s}    Price after Trade:      {PricePostTradeDsp}")
    print(f"      {PhoneNum:<32s}   License Fee:            {LicenseFeeDsp}")
    print(f"                                         Transfer Fee:           {TransferFeeDsp}")
    print(f"                                         --------------------------------------")
    print(f"Car Details:                             Subtotal:               {SubTotalDsp}")
    print(f"                                         HST:                    {HSTAmountDsp}")
    print(f"     {CarYear:<4s} {CarMake:<13s} {CarModel:<10s}   --------------------------------------")
    print(f"                                         Total sales amount:     {TotalAmountDsp}")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"                               Financing     Total        Monthly")
    print(f"     # Years    # Payments        Fee        Price        Payment")
    print(f"     ---------------------------------------------------------------------      ")
    #Payment Schedule Loop
    for years in range (1, 5):
        NumPayments = years * 12

        FinancingFeePerYear = FINANCINGFEE * years
        FinancingFeePerYearDsp = "${:,.2f}".format(FinancingFeePerYear)

        TotalPrice = TotalAmount + FinancingFeePerYear
        TotalPriceDsp = "${:,.2f}".format(TotalPrice)

        MonthlyPayment = TotalPrice / NumPayments
        MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)

        print(f"        {years:<4d}           {NumPayments:<2d}        {FinancingFeePerYearDsp:<5s}     {TotalPriceDsp:<8s}   {MonthlyPaymentDsp:<8s}")
    print(f"     ---------------------------------------------------------------------      ")
    print(f"     First payment date: 01-{FirstPaymentMonth}-{FirstPaymentYear}")
    print(f"--------------------------------------------------------------------------------")
    print(f"                    Best used cars at the best prices!")


    # Write the values to a data file for storage.



#Any housekeeping duties at the end of the program