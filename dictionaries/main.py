#!/usr/local/bin/python3.5

import cgi
import math

def httpHeader():
    print ("""Content-type: text/html

""")

def htmlHeader():
    print ("""<html>
<head>

</head>
<body>
""")

def htmlFooter():
    print ("""
</body>
</html>""")

def htmlForm():
    print ("""

<table align='center'  bgcolor = 'antiquewhite'>

   <form method="POST">
     <tr>
        <td align='right'> Enter your input: </td>
        <td> 
            <textarea name='paragraph' rows='8' cols='40'></textarea>
        </td> 
     </tr>
     <tr>
        <td align='center' colspan='2'>
            <input type='submit' name='selection' value='input'/>
        </td>
     </tr>
   </form>

</table>
""")

#copied function for testing
def testTable(para):
    lines = para.splitlines()
    for line in lines:
        if line == "DUMP":
            print("Printing all variables:" + "<br>")
            for keys in table.keys():
                print(keys + " = " + str(table[keys]) + "<br>")
        else:
            words = line.split(" ")
            if words[2] in table:
                table[words[0]] = table[words[2]]
            else:
                table[words[0]] = int(words[2])
    print(table)

#function to split textarea, identify input and place into temporary table
def inputTable(para, table):
    #split textfield into lines
    lines = para.splitlines()
    for line in lines:
        #checks lines for DUMP 
        if line == "DUMP":
            print("Printing all variables:" + "<br>")
            for keys in table.keys():
                print(keys + " = " + str(table[keys]) + "<br>")
        #checks lines for non lowercase first letter
        elif line[0].isupper() == True:
            print("Vaiables must begin with a lower case letter: " + line + "<br>")
        else:
            #split each line into individual words
            words = line.split(" ")
            #checks to see if input after "=" exist in table; sets variable to existing table value
            if words[2] in table:
                table[words[0]] = table[words[2]]
            #checks if input is not a float; error statement
            elif isFloat(words[2]) == False:
                print("Error: " + str(words[2]) + " not defined" + "<br>")
            #checks if input is a float; inputs into table
            elif isFloat(words[2]) == True:
                table[words[0]] = float(words[2])
            #checks for unrecognized input type
            else:
                print("Input not Recongnized" + str(words[2]) + "<br>")
    print(table)

#from https://stackoverflow.com/questions/2356925/how-to-check-whether-string-might-be-type-cast-to-float-in-python
#takes a string arguement to see if it can be cast to a float
#isnumeric() does not work for floats
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

#
# The main routine starts here
#

httpHeader()
htmlHeader()

#get the form info
formInfo = cgi.FieldStorage()

# Get data from fields
paragraph = formInfo.getvalue('paragraph')
selection = formInfo.getvalue('selection')

#create empty table
tempTable = {}

htmlForm()

#invoke function with tempTable as target
if selection == "input":
    inputTable(paragraph, tempTable)

htmlFooter()