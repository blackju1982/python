#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

import cgi
from collections import Counter

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


#function to split textarea; count frequency of words; sort by value then key
def inputTable(para):
    #splits initial textfield
    frequency = para.split()

    #count the number of occurances each word has in the textfield
    cnt = Counter(frequency)

    #sort results by the value, then the key
    results = sorted(cnt.items(), key=lambda x:(-x[1], x[0]))[:20] # Limit to 20 top words. [:20] works as it is sorted by the value first
    
    print(results)





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