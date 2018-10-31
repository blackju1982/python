#!/usr/local/bin/python3.5
#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

import cgi

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
        <td align='right'> Enter your word to search for: </td>
        <td> 
            <input type="text" name='word' />
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

def KMPmatch(pattern, text):
    for i in pattern:
        Prefix.append(-1)
    return match(pattern, 0, text, 0)

def match(pattern, m, text, n):
    if (m == len(pattern)):
        return(n - m)
    if (n == len(text)):
        return (-1)
    return match(pattern, extend(pattern, m, text[n]), text, n + 1)

def extend(pattern, j, char):
    if pattern[j] == char:
        return j + 1
    if j == 0:
        return 0
    return extend(pattern, prefix(pattern, j), char)

def prefix(pattern, i):
    if Prefix[i] == -1:
        if i == 1:
            Prefix[i] = 0
        else:
            Prefix[i] = extend(pattern, prefix(pattern, i - 1), pattern[i - 1])
    return Prefix[i]



#
# The main routine starts here
#

httpHeader()
htmlHeader()

#get the form info
formInfo = cgi.FieldStorage()

# Get data from fields
paragraph = formInfo.getvalue('paragraph')
word = formInfo.getvalue('word')
selection = formInfo.getvalue('selection')

htmlForm()

#create Prefix
Prefix = []

#invoke functiom
if selection == "input":
    # print(str(KMPmatch(word, paragraph)))
    print(str(word) + " was found at position " + str(KMPmatch(word, paragraph)))

htmlFooter()