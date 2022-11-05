''' 10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
 9:00 PM)'''

from datetime import datetime
dte=datetime.today()
print(dte)   #current date and time print
d=dte.strftime("%d-%m-%Y and %I:%M %p")
print(d)