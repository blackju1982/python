#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

import cgi
import collections

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
# def testFunction(para):


#function to split textarea, identify input and place into temporary tables
def inputTable(para):
    frequency = {}
    codes = {}

    frequency = collections.Counter(para)
    orderedFrequency = collections.OrderedDict(sorted(frequency.items(), key=lambda t: t[1]))
    print(orderedFrequency)
    print("<br>")

    while len(orderedFrequency) > 1:
    #access keys/values of dictionary
        key1 = str(list(orderedFrequency.keys())[0])
        key2 = str(list(orderedFrequency.keys())[1])
        value1 = list(orderedFrequency.values())[0]
        value2 = list(orderedFrequency.values())[1]

        frequency[str(key1 + key2)] = value1 + value2

        # codes generation
        for letter in key1:
            if letter in codes:
                codes[letter] = "0" + str(codes[letter])
            else:
                codes[letter] = "0"
        for letter in key2:
            if letter in codes:
                codes[letter] = "1" + str(codes[letter])
            else:
                codes[letter] = "1"

        del frequency[key1]
        del frequency[key2]
        
        orderedFrequency = collections.OrderedDict(sorted(frequency.items(), key=lambda t: t[1]))

    results = collections.OrderedDict(sorted(codes.items()))

    for keys in results.keys():
        if keys == " ":
            print("space" + " = " + str(codes[keys]) + "<br>")
        else:
            print(keys + " = " + str(codes[keys]) + "<br>")

    # print(codes)



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

htmlForm()

#invoke function
if selection == "input":
    inputTable(paragraph)

htmlFooter()