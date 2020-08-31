import jinja2
import markdown2
import pdfkit
import io
#this script should take formatted markdown and insert it into the correct parts of the template. 

#look at including images. 

first = ""
second = ""
ref = 0

##with open('testbulletin.md', 'r') as f:
lines = open('testbulletin.md', 'r').readlines()
if "## Thought for the week" in lines:
    while i < len(lines):
        if s == "## Thought for the week":
            ref = i-1
            break
first = lines[0:ref]
second = lines[ref:-1]
        
firsthtml = markdown2.markdown("\n".join(first))
secondhtml = markdown2.markdown("\n".join(second))

loader = jinja2.FileSystemLoader(searchpath="templates")
env = jinja2.Environment(loader=loader)

printtemplate = env.get_template("print.html.jinja")

printhtml = open ("print.html","w")

printhtml.write(printtemplate.render(first=firsthtml, second=secondhtml))

printhtml.close()

options = {
        'page-size':'A4',
        'orientation':'Landscape'
        }

pdfkit.from_file("print.html", "print.pdf", options=options)
