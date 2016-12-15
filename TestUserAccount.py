#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Two things are missing from the line below - fill them in
my_username="May"
my_password="1234"
my_secret="my secret is.."
my_user=UserAccount(my_username,my_password,my_secret)
#Call the print_secret method (function) - it takes one input - a guess for the password.
my_user.print_secret("126")
my_user.print_secret("1234")
#Use the wrong password as input here
#my_user.126

#Use the right password here
#my_user.1234
