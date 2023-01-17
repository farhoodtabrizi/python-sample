# Your function for calculating payment goes here
def calculating_payment (principal, annual_interest_rate, duration):
    n=duration*12
    r=(annual_interest_rate/100)/12
    if r==0:
        monthly_payment=principal/n
    monthly_payment=(principal*(r*(1+r)**n))/((1+r)**n-1)
    return monthly_payment

# Your function for calculating remaining balance goes here
def calculating_remaining (principal, annual_interest_rate, duration , number_of_payments):
    n=duration*12
    r=(annual_interest_rate/100)/12
    p=number_of_payments
    if r==0:
        remaining_loadn_balance=principal-(principal*(p/n))
    remaining_loadn_balance=(principal*((1+r)**n-(1+r)**p))/((1+r)**n-1)
    return remaining_loadn_balance         

# Your main program goes here
# Input
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
# Calculating part
monthly_payment=calculating_payment (principal, annual_interest_rate, duration)
print ('LOAN AMOUNT:', int(principal), 'INTEREST RATE (PERCENT):', int(annual_interest_rate))
print ('DURATION (YEARS):', int(duration), 'MONTHLY PAYMENT:', int(monthly_payment))
y=range (1,(duration+1))
for i in y:
        number_of_payments=i*12
        a=monthly_payment*number_of_payments
        remaining_loadn_balance=calculating_remaining (principal, annual_interest_rate, duration , number_of_payments)
        print ('YEAR: ',i, 'BALANCE: ',int(remaining_loadn_balance), 'TOTAL PAYMENT ',int(a))
       
