# q7_generate_payroll.py
# program to generate payroll

name = input("Enter name: ")
hours = float(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: $"))
cpf = float(input("Enter CPF contribution rate(%): "))

gross = hours*rate
cpfcon = cpf/100*gross
net = gross-cpfcon

print("Payroll statement for", name)
print("Number of hours worked per week:", hours)
print("Hourly pay rate: ${0}".format(rate))
print("Gross pay = ${0}".format(gross))
print("Cpf contribution at {0}% = ${1:.2f}".format(cpf, cpfcon))
