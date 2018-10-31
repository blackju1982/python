#!/usr/local/bin/python3.5

import cgi
from statistics import mean

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
        <td align='right'> Enter your paragraph: </td>
        <td> 
            <textarea name='paragraph' rows='8' cols='40'></textarea>
        </td> 
     </tr>
     <tr>
        <td align='center' colspan='2'>
            <input type='submit' name='selection' value='parse'/>
            <input type='submit' name='selection' value='sortWords'/>
            <input type='submit' name='selection' value='wordCount'/>
            <input type='submit' name='selection' value='letterCount'/>
            <input type='submit' name='selection' value='everyThing'/>
        </td>
     </tr>
   </form>

</table>
""")

def parse(para):
    words = para.split()
    for word in words:
        print (word + ", ")

def sortWords(para):
    words = para.split()
    words.sort()
    for word in words:
        print (word + ", ")

def wordCount(para):
    words = para.split()
    print("Number of words: " + str(len(words)))


def letterCount(para):
    letterCount = []
    words = para.split()
    for word in words:
        letterCount.append(len(word))
    print("Average Number of letters per word: " + str(mean(letterCount)))

def everyThing(para):
    letterCount = []
    words = para.split()
    words.sort()
    for word in words:
        letterCount.append(len(word))
        print (word + ", ")
    print("<br>" + "Number of words: " + str(len(words)))
    print("<br>" + "Average Number of letters per word: " + str(mean(letterCount)))

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

#check to see what submit was pressed
if selection == "parse":
    parse(paragraph)
elif selection == "sortWords":
    sortWords(paragraph)
elif selection == "wordCount":
    wordCount(paragraph)
elif selection == "letterCount":
    letterCount(paragraph)
elif selection == "everyThing":
    everyThing(paragraph)


htmlForm()


htmlFooter()
