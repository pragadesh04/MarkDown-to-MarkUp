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

# ++++++++++++++ Heading ++++++++++++++++++++++
op.writelines("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body style="background-color: grey; margin: 0; padding: 0;">
""")
codeblock = False

for j in range (len(md)):
    h = i = 0
    text = ''
    
    links = ["[", "]", "(", ")"]
    
    # ++++++++++++++ Heading ++++++++++++++++++++++
    if md[j][0] == '#':
        while md[j][i] == '#':
            h += 1
            i +=1
        md[j] = (md[j].replace("#",""))[1:-1]
        id = md[j].replace(" ", "_")
        op.writelines(f"""<h{h} style=" text-align: center; background-color:black; color:white;" id="#{id}">{md[j]}</h{h}>\n""")
        
    # ++++++++++++++ Links ++++++++++++++++++++++
    if all(link in md[j] for link in links):
        print(md[j])
        for i in range (md[j].index("["), md[j].index("]")+1):
            text += md[j][i]
        under_ = text.replace(" ","_")
        op.writelines(f"""<h4  style="text-align: center;"><a style="text-decoration: none; color: skyblue;" href="#{under_[1:-1]}">{text[1:-1]}</a></h4>\n""")
    # ++++++++++++++ CodeBlock ++++++++++++++++++++++
    if "```" in md[j]:
        codeblock = not codeblock
        j += 1
        if codeblock:
            op.writelines(f"""<h4 style="background-color: white; padding: 5px; border-radius: 5px; text-align: center;">{md[j]}</h4>\n""")
    
op.writelines("""
</body>
</html>""")