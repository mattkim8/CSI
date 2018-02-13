
#cash = raw_input("Money amount: ")
#percent = raw_input("Percent tip: ")
#def tip(cash, percent):
#    total = ((float(percent)/100) * float(cash)) + float(cash)
#    return total 
#print tip(cash, percent)
# ^ wrong

def tip(total, percent):
    return total * percent
total_bill = 90
percent = .15
tip(total_bill, percent)
test_tip = tip(total_bill, percent)

def tip2(total,percent = .2):
    return total * percent
total_bill = 90
print tip(total_bill) 
