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
        <td align='right'> Enter your paragraph: </td>
        <td> 
            <textarea name='paragraph' rows='8' cols='40'></textarea>
        </td> 
     </tr>
     <tr>
        <td align='center' colspan='2'>
            <input type='submit' name='selection' value='Solve'/>

        </td>
     </tr>
   </form>

</table>
""")

def parse(userInput):
    alist = userInput.split()

def theGame(alist, placeHolder):
    numberList = alist
    currentPos = placeHolder
    currentValue = numberList[currentPos]
    fwd = numberList[currentPos + currentValue]
    rwd = numberList[currentPos - currentValue]

    if currentValue == 0:
        return "You have lost due to lack of moves"
    elif (fwd > len(numberList) - 1) and (rwd < 0):
        return "You have gone out of bounds and lost"
    elif currentPos == (len(numberList) - 1):
        return "You have reached the end and won!"
    elif fwd <= (len(numberList) - 1):
        currentPos = fwd
        theGame(numberList, currentPos)
    elif rwd >= 0:
        currentPos = rwd
        theGame(numberList, currentPos)


#Main
httpHeader()
htmlHeader()

htmlForm()

formInfo = cgi.FieldStorage()

numbers = str(formInfo.getvalue('Solve'))

numberList = parse(numbers)

theGame(numberList, 0)

htmlFooter()