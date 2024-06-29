# Write a program to display Good Mr=orning, Good afternoon or Good Evening or Good night to the user

import time

timestamp = (time.strftime('%H: %M: %S'))
print("Time: ", timestamp)

timestamp_hour = int(time.strftime('%H'))
if(timestamp_hour < 12):
    print("Good Mornig, Samyam")
elif (timestamp_hour >= 12 & timestamp_hour <=16):
    print("Good Afternoon, Samyam")
elif( timestamp_hour >= 16 & timestamp_hour <= 20):
    print("Good Evening, Samyam")
else:
    print("Good Night, Samyam")



