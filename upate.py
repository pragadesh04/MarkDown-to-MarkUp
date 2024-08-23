import re
import time as t
import utils

u = utils.utils()

u.printf("Opening files")
t.sleep(0.2)
clear = open("output.html", "w")
u.printf("Clearing existing texts")
t.sleep(0.5)
clear.writelines("")
u.printf("Cleared files")
t.sleep(0.5)
clear.close()
u.printf("Cleared:the file")

op = open("output.html", "a+")
f = open("file.md", "r")
lines = f.readlines()

j= 1
for i in range (len(lines)):
    try:
        if "```" in lines[i]:
            i+=1
            op.writelines(f"""<p style="background-color: lightgrey;">{lines[i]}</p>\n""")
            
    except:
        u.printf("cant compare")
        
    lines[i] = lines[i].replace(' ','_')
    if lines[i][0] == '#':
        while True:
            if lines[i][j] == '#':
                j+=1
            else:
                break
        lines[i] = lines[i].replace('#', '')
        k=0
        lines[i] = lines[i].replace(' ','')
        # lines[i] = lines[i].replace(' ','_')
        if j == 1 or j == 2:
            op.writelines(f"""<h{j}  style="text-align: center" id="{lines[i][1:-1]}">{lines[i][1:-1]}</h{j}>\n""")
        else:
            op.writelines(f"""<h{j} style="text-align: left" id="{lines[i][1:-1]}">{lines[i][1:-1]}</h{j}>\n""")
    elif lines[i][0] == '`':
        lines[i].replace("`","")
        print()
    else:
        try:
            c = re.compile(r'\[(.*?)\]')
            val = c.findall(lines[i])
            if val[0] is not None:
                # print(val)
                op.writelines(f"""<a href="#{val[0]}"><h4>{val[0]}</h4></a>\n""")
        except:
            continue
    # else:
    #     op.writelines(f"<p>{lines[i]}</p>\n")

for i in op:
    print(i)