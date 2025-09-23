# create an electricity bill estimator
print("Electricity bill estimator")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
while True: # keeps looping until valid tariff is entered
    tariff_choice = input("Which tariff? (11 or 31):")
    # set cent price based on tariff chosen
    if tariff_choice == "11":
        price_kwh_cents = TARIFF_11
        break # breaks stop the loop
    elif tariff_choice == "31":
        price_kwh_cents = TARIFF_31
        break
    else:
        print("Invalid tariff selected. Default selected (11)")
        price_kwh_cents = TARIFF_11

daily_kwh_use = float(input("Enter daily use in kWh:"))
number_of_billing_days = int(input("Enter number of billing days:"))
bill_estimate = price_kwh_cents * daily_kwh_use * number_of_billing_days
print(f"The electricity bill estimate is:${bill_estimate:.2f}")