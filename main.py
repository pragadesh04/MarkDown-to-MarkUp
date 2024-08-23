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
for i in range :
    try:
        bg = re.compile(r'\`(.*?)\`')
        val = bg.findall(i)
        if val: print(val)
    except:
        u.printf("cant compare")
    i = i.replace(' ','_')
    if i[0] == '#':
        while True:
            if i[j] == '#':
                j+=1
            else:
                break
        i = i.replace('#', '')
        k=0
        i = i.replace(' ','')
        # i = i.replace(' ','_')
        if j == 1 or j == 2:
            op.writelines(f"""<h{j}  style="text-align: center" id="{i[1:-1]}">{i[1:-1]}</h{j}>\n""")
        else:
            op.writelines(f"""<h{j} style="text-align: left" id="{i[1:-1]}">{i[1:-1]}</h{j}>\n""")
    elif i[0] == '`':
        i.replace("`","")
        print()
    else:
        try:
            c = re.compile(r'\[(.*?)\]')
            val = c.findall(i)
            if val[0] is not None:
                # print(val)
                op.writelines(f"""<a href="#{val[0]}"><h4>{val[0]}</h4></a>\n""")
        except:
            continue
    # else:
    #     op.writelines(f"<p>{i}</p>\n")

for i in op:
    print(i)