name = 'Hendriktio Freizello'
age = 21
height = 167
weight = 95
eyes = 'brown'
teeth = 'white'
hair = 'black'
c_height = height * 0.393701
c_weight = weight * 2.20462

print "let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d inch tall." % c_height
print "He's %d kilograms heavy." % weight
print "He's %d pounds heavy." % c_weight
print "actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

print "If I add %d, %d, and %d I get %d." % (
age , height, weight, age + height + weight)
