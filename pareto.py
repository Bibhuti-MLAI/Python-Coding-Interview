
exposure = {"C101": 120, "C102": 15, "C103": 340, "C104": 60,
            "C105": 25, "C106": 210, "C107": 10, "C108": 220}   # Rs lakh

items = sorted(exposure.items() , key = lambda kv: kv[1] , reverse =True)
total = sum(exposure.values())
running = 0
choosen = []
for cust,amt in items:
    running += amt
    choosen.append(cust)
    if running >= 0.8* total:
        break
print("total_exposure = ", total)
print("running_exposure = ", running)
print("share covered: ", round(100*running/total,2), "%")

months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]   
revenue = [8,9,7,10,12,11,9,14,13,15,16,26]
half = sum(revenue)/2
cum =0
crossing = None

for m,r in zip(months,revenue):
    cum += r
    if cum >= half and crossing is None:
        crossing = m
print("Month of crossing: ", sum(revenue), "Half revenue: ", "| half :",half)
print("50% crossed in ;",crossing[0],"with cumulative" , crossing[1])
