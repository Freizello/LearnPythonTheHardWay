def cheese_and_crackers(cheese_count, box_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d box of crackers!" %box_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly :"
cheese_and_crackers(30,40)

print "OR, we can use variables from our script :"
amount_of_cheese = 10
amount_of_crackers = 90
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "AND we can combine the two, variables and math :"
cheese_and_crackers(amount_of_cheese+20, amount_of_crackers+10)
