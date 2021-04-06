#!/usr/bin/python
import getpass

username = raw_input("Enter a username: ")
print "Welcome,", username
print "Enter a password"
pass1 = getpass.getpass()
print "Confirm password"
pass2 = getpass.getpass()
if pass1 == pass2:
    print "User ", username, " registered"
else:
    print "Registration failed. Passwords do not match"
