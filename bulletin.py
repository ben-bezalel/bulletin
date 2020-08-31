import jinja2
import markdown2
import pdfkit

#look at including images. 

first = ""
second = ""
ref = [0]
sections = []

##with open('testbulletin.md', 'r') as f:
lines = open('testbulletin.md', 'r').readlines()
if "COLUMNBREAK\n" in lines:
    i=0
    while i < len(lines):
        if lines[i] == "COLUMNBREAK\n":
            ref.append(i)
        i += 1
    j=0
    ref.append(len(lines))
    while j < len(ref)-1:
        if j>0:
            sections.append(lines[ref[j]+1:ref[j+1]])
        else:
            sections.append(lines[ref[j]:ref[j+1]])
        j +=1
    k=0
    while k < len(sections): 
        sections[k] = markdown2.markdown("\n".join(sections[k]))
        k +=1

#have breaks for email and breaks for print

loader = jinja2.FileSystemLoader(searchpath="templates")
env = jinja2.Environment(loader=loader)

#I could probably remove jinja and replace with an ordered list...
printtemplate = env.get_template("print.html.jinja")
emailtemplate = env.get_template("email.html.jinja")
printhtml = open ("print.html","w")

printhtml.write(printtemplate.render(first=sections[0], second=sections[2], third=sections[1]))

printhtml.close()

emailhtml = open ("email.html","w")

emailhtml.write(emailtemplate.render(first=sections[0], second=sections[2], third=sections[1]))

emailhtml.close()

options = {
        'page-size':'A4',
        'orientation':'Landscape',
        'enable-local-file-access': None # so that external css files can be used to style
        }

pdfkit.from_file("print.html", "print.pdf", options=options)

#NOTES
#deactive a pipenv environment by typing deactivate
#wkhtmltopdf.org needs to be installed for script to work (or you can save to pdf from html)
#start up pipenv by running pipenv shell
#za to toggle folds in vim, ctrl-shift to move between cmd tabs, :b to move between vim buffers
