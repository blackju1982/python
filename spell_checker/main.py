#!/usr/local/bin/python3.5
#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

import cgi
from avl_tree import AVLTreeMap

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


#function to split textarea; search dictionary for word; print mispelled words
def spellCheck(para):
    #read text area; define empty dictionary; empty list for notWords
    words = para.split()
    dictionary = AVLTreeMap()
    notWords = []

    #reads in dictionary; creates tree
    for i in open("/home/staff/kurban/public/lists/web2.txt").read().lower().split():
        dictionary.__setitem__(i, i)
    
    #find each word in dictionary
    for j in words:
        word = j.lower()
        findWord = dictionary.find_position(word)
        if findWord.key() != word:
            notWords.append(word)

    #print mispelled words
    if len(notWords) == 0:
        print("No words were mispelled")
    else:
        for k in notWords:
            print(k + "</br>")





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
    spellCheck(paragraph)

htmlFooter()