import re
import time as t

print("Opening files")
t.sleep(0.2)
clear = open("output.html", "w")
print("Clearing existing texts")
t.sleep(0.5)
clear.writelines("")
print("Cleared files")
t.sleep(0.5)
clear.close()
print("Cleared:the file")

op = open("output.html", "a+")
f = open("file.md", "r")

j= 1
for i in f:
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

print(j)

for i in op:
    print(i)