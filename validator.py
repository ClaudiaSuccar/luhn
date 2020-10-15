#Import the Z Open Automation Utilities libraries we need
from zoautil_py import MVSCmd, Datasets
from zoautil_py.types import DDStatement
# Import datetime, needed so we can format the report
from datetime import datetime
# Import os, needed to get the environment variables
import os

#Take the contents of this data set and read it into cc_contents
cc_contents = Datasets.read("MTM2020.PUBLIC.CUST16")

USERID = os.getenv("USER")
output_dataset=USERID+".OUTPUT.CCINVALD"
#Delete the output dataset if it already exists
if Datasets.exists(output_dataset):
    Datasets.delete(output_dataset)

Datasets.create(output_dataset, "SEQ")
# Create a new SEQUENTIAL DATA SET with the name of output_dataset


#A function that checks to see if the number passed to it is even. Returns True or False (Boolean)
def is_even(num_to_check):              # this is a function. num_to_check is what gets sent to it
    if ((num_to_check % 2) == 0):       # a simple check to see if num_to_check is even.
        result = True                   # We set result to True
        return result                   # and then return it.
    else:                               # if it isn't
        result = False                  # set return to False
        return result                   # and return that.

def luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number) # digits is set to the card number
    odd_digits = digits[-1::-2] # find odd numbers
    even_digits = digits[-2::-2] # find even number
    checksum = 0
    checksum += sum(odd_digits) #checksum adds the sum of all odd digits
    for d in even_digits: # for every even number, apply the luhn equation and add to checksum
        checksum += sum(digits_of(d*2))
    return (checksum % 10) # return the simplified checksum number

cc_list = cc_contents.splitlines()      # take that giant string and turn it into a List
invalid_cc_list = []                    # A second list to hold invalid entries
for cc_line in cc_list:                 # do everything here for every item in that List
    cc_digits = int(cc_line[2:21])      # Just grabbing some digits. Not a full CC number (HINT!)/ (SOLVED)
    if (luhn(cc_digits)):           # If the card number is INVALID
        invalid_cc_list.append(cc_line) #append to our invalid list

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
report_output = '\n'.join(invalid_cc_list)
report_output = "INVALID CREDIT CARD REPORT FOR " + dt_string + '\n\n' + report_output
print(report_output)  # Print it out to the screen. 
Datasets.write(output_dataset,report_output)