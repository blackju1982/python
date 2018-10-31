#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

import cgi
from graph import Graph

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


#function to split textarea, identify input and place into temporary memory
def inputGraph(para):
    lines = para.split("\n")
    vertexPoints = []
    connections = []
    input_edges = False
    for line in lines:
        if line.strip() == "#end":
            input_edges = True
        elif input_edges == True:
            edge = line.split(",")
            connections.append((edge[0].strip(),edge[1].strip()))
        else:
            vertexPoints.append(line.strip())
    return (vertexPoints, connections)

#take input and create table based on connected points
def adjacencyMap(vertexPoints, connections):
    graph = Graph(True)
    tempMap = {}
    for i in vertexPoints:
        tempMap[i] = graph.insert_vertex(i)
    for (a,b) in connections:
        graph.insert_edge(tempMap[a],tempMap[b])
    print("<table border='1'><tr><td align='center'> Point: </td><td align='center'> Connects To: </td></tr>")
    for i in vertexPoints:
        print("<tr><td align='center'>", i, "</td><td align='center'>")
        connectsTo = []
        for e in graph.incident_edges(tempMap[i]):
            connectsTo.append((e.endpoints()[1]).element())
        if connectsTo == []:
            print("None </td> </tr>")
        else:
            print(", ".join(connectsTo) + "</td></tr>")
    print("</table>")

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

#invoke function to format data; create map table
if selection == "input":
    (vertexPoints, connections) = inputGraph(paragraph)

    # for i in vertexPoints:
    #     print(str(i) + ", ")
    # for i in connections:
    #     print(str(i) + ", ")

    adjacencyMap(vertexPoints, connections)


htmlFooter()