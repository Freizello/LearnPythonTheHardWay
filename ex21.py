def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subs(a, b):
    print "SUBSTRACTIN %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" %(a, b)
    return a * b

def div(a, b):
    print "DIVIDING %d * %d" %(a, b)
    return a / b

print "LET'S DO SOME MATH WITH JUST FUNCTIONS!"

age = add(30,5)
height = subs(78, 4)
weight = multiply(90,2)
iq = div(100,2)

print "Age : %d, Height : %d, Weight : %d, IQ : %d" %(age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subs(height, multiply(weight, div(iq,2))))

print "That becomes: ", what, "Caranya?"

print "\n\n", add(30,5), "Tahun"
