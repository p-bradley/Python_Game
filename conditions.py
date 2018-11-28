#print a message to the terminal window
print("Rules that govern the state of water")

# set up a variable to hold the temperature that we input
current_temp = False

while current_temp is False:
    current_temp = input ("Enter a temperature\n")
# see what current temp it is
print("you input" , current_temp)

# if the current temperature is at freezing or below, water is a solid
if (int(current_temp) < 0 or (int(current_temp) == 0)):
    print("water is a solid! cuz it's at or below freezing")
    current_temp = False
# else check another condition, if it's not freezing, is below boiling?
elif (int (current_temp) < 100):
    print("water is a liquid, because it's above freezing and below boiling")
    current_temp = False

# check if water is above boiling temp, water is a gas
elif (int(current_temp) > 100 or (int(current_temp) == 100)):
    print("water is a gas, cuz it's like, really hot")
    current_temp = False

