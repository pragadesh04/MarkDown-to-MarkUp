import re, os, utils, time as t

u = utils.utils()
u.printh(os.getcwd())

op = open("output.html", "w")
op.writelines("")
op.close()

markdown = open("file.md", "r")
op = open("output.html", "a")

md = markdown.readlines()


print()


for line in md:
    h = i = 0
    text = '' 
    links = ["[", "]", "(", ")"]
    
    # ++++++++++++++ Heading ++++++++++++++++++++++
    if line[0] == '#':
        while line[i] == '#':
            h += 1
            i +=1
        line = (line.replace("#",""))[1:-1]
        id = line.replace(" ", "_")
        op.write(f"""<h{h} id="#{id}">{line}</h{h}>\n""")
        
    # ++++++++++++++ Links ++++++++++++++++++++++
    if all(link in line for link in links):
        print(line)
        # sb = line.index("[")
        for i in range (line.index("["), line.index("]")+1):
            text += line[i]
        u.printh(text)
        under_ = text.replace(" ","_")
        op.writelines(f"""<a href="#{under_[1:-1]}">{text[1:-1]}</a><br/>\n""")