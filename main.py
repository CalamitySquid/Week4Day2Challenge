# Names:Gerado Pinada, Sebatian Wang, Jesus Ruiz "Chewy"
salesperson_name = input("What is your name? ")
total_sales = int(input("How many sells did you make this month? "))
commissions = round(((total_sales * 13) / 100),2)
# print(commissions)
print(f"{salesperson_name} this month you made {total_sales} sales and your commission is ${commissions}.")


