import re, os, utils, time as t

u = utils.utils()
u.printh("To change the MD file copy paste the file and update the file.md as your intended filename")

op = open("output.html", "w")
op.writelines("")
op.close()
markdown = open("file.md", "r")
op = open("output.html", "a")

md = markdown.readlines()

# ++++++++++++++ Heading ++++++++++++++++++++++
op.writelines("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body style="background-color: grey; margin: 0; padding: 0; scroll-behavior: smooth;">
""")
codeblock = False
head = False
head2 = True

md.append("ended")
md.append("\n")
print()
print()
length = len(md)

for j in range (len(md)+1):
    h = i = 0
    text = ''
    bold = 0
    
    links = ["[", "]", "(", ")"]
    if md[j] != "ended":
        if u.isHeading(md[j+1]):
            head = not head
            if head:
                op.writelines(f"""\n<div style="background-color: rgb(221, 221, 221); padding-bottom: 20px; border-radius: 25px; margin: 0rem 0rem">""")
            else:
                op.writelines("""</div>\n""")
    else:
        op.writelines(f"""</div>\n""")
        break    
    
    # ++++++++++++++ Heading ++++++++++++++++++++++
    if md[j][0] == '#':
        while md[j][i] == '#':
            h += 1
            i +=1
        md[j] = (md[j].replace("#",""))[1:-1]
        id = md[j].replace(" ", "-")
        id = id.lower()
        if h == 1:
            op.writelines(f"""\n<h{h} style=" text-align: center; background-color:black; color:white; padding: 25px;" id="{id}">{md[j]}</h{h}>\n""")
        else:
            op.writelines(f"""\n<h{h} style=" text-align: center; background-color:black; color:white; padding: 25px;" id="{id}">{md[j]}</h{h}>\n""")
        
    # ++++++++++++++ Links ++++++++++++++++++++++
    elif all(link in md[j] for link in links):
        for i in range (md[j].index("["), md[j].index("]")+1):
            text += md[j][i]
        under_ = text.replace(" ","-")
        under_ = under_.lower()
        op.writelines(f"""<h4  style="text-align: center;"><a style="text-decoration: none; color: blue; " href="#{under_[1:-1]}">{text[1:-1]}</a></h4>\n""")

    # ++++++++++++++ CodeBlock ++++++++++++++++++++++
    elif "```" in md[j]:
        codeblock = not codeblock
        if codeblock:
            j += 1
            op.writelines(f"""<h4 style="background-color: rgb(99, 99, 99); color: white; margin: 0.2rem 10rem; padding: 5px; border-radius: 5px; text-align: center;">{md[j]}</h4>\n""")
            md[j] = md[j].replace(md[j], " ")
        else:
            continue
            
    elif "***" in md[j]:
        start, end, starBeg, starEnd  = u.findPos(md[j], "*")
        str = md[j].replace(md[j][starBeg:starEnd+start], md[j][start:end])
        op.writelines(f"""<em><strong style="margin-left: 10%;">{str}</strong></em>""")
        
    elif "**" in md[j]:
        start, end, starBeg, starEnd  = u.findPos(md[j], "*")
        str = md[j].replace(md[j][starBeg:starEnd+start], md[j][start:end])
        op.writelines(f"""<strong style="margin-left: 25%;">{str[:-1]}</strong>""")
        
    elif "*" in md[j]:
        start = md[j].index("*")
        str = md[j][start:]
        end = str.index("*")
        op.writelines(f"""<em>{str}</em>""")
    
    else:
        if md[j] == "" or md[j] == " " or md[j] == "\n":
            continue
        op.writelines(f"""\n<p style="align-items: center"><p style=" text-align: center;">&emsp;{md[j]}</p></p>\n""")
    t.sleep(0.01)
    u.printc(f"""procecessing the line : {j} of {length-2}""")
op.writelines("""
</body>
</html>""")
print()
print()
u.printh(f"""procecessing completed : {j} of {length-2}""")
