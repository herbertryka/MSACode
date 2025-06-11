#get plausible amounts
def get_hourly_wage():
    while True:
        try:
            hourly_wage = float(input("Enter your hourly wage: "))
            #validate hourly wage
            if hourly_wage <=0:
                print("ERROR: Enter a value greater than 0")
                continue
            else:
                break
        except:
            print("ERROR: Enter a number")
    return hourly_wage

def get_hours_worked():
    while True:
        try:
            hours_worked = float(input("Enter hours worked per day: "))
            #validate hours
            if hours_worked >=24:
                print("ERROR: Enter a value less than 24")
                continue
            if hours_worked <=0:
                print("ERROR: Enter a value greater than 0")
            else:
                break
        except:
            print("ERROR: Enter a number")
    return hours_worked

def get_yearly_income(hourly_wage, hours_worked):
    annual_income_before_taxes = hourly_wage * hours_worked * 350
   
    return annual_income_before_taxes
    



def main():
    hourly_wage = get_hourly_wage()
    hours_worked = get_hours_worked()
    annual_income_before_taxes = get_yearly_income(hourly_wage, hours_worked)
    #get tax amount
    tax_amount = annual_income_before_taxes * .12
    #get income after taxes
    income_after_taxes = annual_income_before_taxes - tax_amount
    print(f"Pay Advice\n---------\nHours Worked: {hours_worked}\nHourly Wage: {hourly_wage}\nIncome Before Taxes: {annual_income_before_taxes: .2f}\nTax Amount: {tax_amount: .2f}\nIncome After Taxes: {income_after_taxes: .2f}")
main()

