#  If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. 
# 
# If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?

weight_earth = int(input("Enter your weight in Earth:\n"))
weight_moon = weight_earth * 0.165
every_year = 1
new_year = weight_moon

for x in range (1,16):
    y = x * 0.165 + weight_moon   
    print('My moon weight each year will be %s kg on year %s' % (y, x))


