 #Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and 
#compute simple interest:  SI = (P ∗ R ∗ T )/100

P=float(input("Enter the principal amount(in rupees):"))
R=float(input("Enter the rate of interest(in %):"))
T=float(input("Enter the time period(in years):"))

simple_interest=(P*R*T)/100
print("The Simple Interest is(in rupees):", simple_interest)