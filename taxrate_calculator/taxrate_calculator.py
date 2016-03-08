"""
programe:taxrate_calucator.py
Author:Chinmay kumar Das


Computing the person's income tax.

1.Significant constants :
	tax rate
	Standard deduction 
	deduction per dependants
2.The inputs are :
	gross income
	no of dependants
3.Computation:
	taxable income =gross income-standard deduction- a deduction for each dependants
	income tax=a fixed percentage of taxable income(in this case 20%)
4.Outputs are :
	the income tax
"""


#Initialize  the constants
Tax_rate=0.2
Standard_deduction=10000
Dependants_deduction=3000
#Requesdt the input
Gross_income=float(input("PLEASE ENTER UR SALARY :"))
num_Dependants=int(input("enter the no of dependants  :"))

#Compute the income tax
taxable_income=Gross_income -Standard_deduction- Dependants_deduction*num_Dependants
income_tax=Tax_rate*taxable_income

#output
print"ur total tax is $"+str(income_tax)