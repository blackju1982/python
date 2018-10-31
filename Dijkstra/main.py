#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

import cgi, cgitb
from graph import Graph
from shortest_paths import *
cgitb.enable()

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
def inputGraph(lines):
    graph = Graph(True)
    inputEdges = False

    for i in lines:
        if i == "#end":
            inputEdges = True
        elif inputEdges is False:
            graph.insert_vertex(i)
            # print("|" + i + "|")
        elif inputEdges is True:
            edge = i.split()
            a = searchForVertex(graph, edge[0].replace(",", ""))
            b = searchForVertex(graph, edge[1].replace(",", ""))
            weight = int(edge[2])
            graph.insert_edge(a, b, weight)
            # print(str(a) + "|" + str(b) + "|" + str(weight))
    return graph

def searchForVertex(graph, point):
    #to connect vertices each edge must be a vertex object
    for i in graph.vertices():
        if i.element() == point:
            return i
    #if vertex does not exist argument is false
    return False
   
def adjacencyMatrix(graph): # accepts a Graph object, prints adjacency matrix as a HTML table
    vertices = graph.vertices()
    print("<table border='1'>")
    print("<tr>")
    print("<td></td>")
    print("<td colspan='" + str(graph.vertex_count()+1) + "' align='center'> From vertex </td>")
    print("</tr>")
    print("<tr>")
    print("<td rowspan='" + str(graph.vertex_count()+1) + "'> To vertex </td>")
    print("<td></td>")
    for i in vertices:
            print("<td align='center'>" + str(i) + "</td>")
    print("</tr>")
    for i in vertices:
            print("<tr><td align='center'>" + str(i) + "</td>")
            for j in vertices:
                    if graph.get_edge(i, j) is not None:
                            print("<td align='center'>1</td>")
                    else:
                            print("<td align='center'>0</td>")
            print("</tr>")
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
    lines = paragraph.splitlines()
    graph = inputGraph(lines)


    #check for shortest if START and END exists
    discovered = {}
    start = searchForVertex(graph, "START")
    end = searchForVertex(graph, "END")
    if (start != False and end != False):
        print("Path from START to END (distance traveled, vertex): ")
        shortPath = shortest_path_lengths(graph, start)
        shortPathTree = shortest_path_tree(graph, start, shortPath)


        #for edges in shortPathTree print each point as they are handled by function
        #modified shortest_path_lengths() to have print(pqlocator[u]) line 47
        
        print("<br />")

        print("Total weight of the path is " + str(shortPath[end]) )




htmlFooter()