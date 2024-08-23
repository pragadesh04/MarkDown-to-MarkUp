import re
import time as t
import utils
import os

print(os.getcwd())

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
u.printf("Cleared: the file")

op = open("output.html", "a+")
f = open("file.md", "r")
lines = f.readlines()

inside_code_block = False  # Flag to track if we're inside a code block
j = 1

for i in range(len(lines)):
    try:
        if "```" in lines[i]:
            inside_code_block = not inside_code_block  # Toggle the flag
            if inside_code_block:
                i += 1
                op.writelines(f"""<p style="background-color: lightgrey; padding: 10px; border-radius: 5px;"><code>{lines[i]}</code></p>\n""")
            else:
                i+=1
                op.writelines(f"""<p>{lines[i]}</p>\n""")
    
        # Replace spaces with underscores
        lines[i] = lines[i].replace(' ', '_')
        
        if lines[i][0] == '#':
            while True:
                if lines[i][j] == '#':
                    j += 1
                else:
                    break
            lines[i] = lines[i].replace('#', '')
            lines[i] = lines[i].replace(' ', '')
            if j == 1 or j == 2:
                op.writelines(f"""<h{j} style="text-align: center" id="{lines[i][1:-1]}">{lines[i][1:-1]}</h{j}>\n""")
            else:
                op.writelines(f"""<h{j} style="text-align: left" id="{lines[i][1:-1]}">{lines[i][1:-1]}</h{j}>\n""")
        elif lines[i][0] == '`':
            lines[i] = lines[i].replace("`", "")
            print()
        else:
            try:
                c = re.compile(r'\[(.*?)\]')
                val = c.findall(lines[i])
                if val:
                    op.writelines(f"""<a href="#{val[0]}"><h4>{val[0]}</h4></a>\n""")
            except Exception as e:
                u.printf(f"Error: {e}")
    except Exception as e:
        u.printf(f"Error processing line {i}: {e}")
    op.writelines(f"""<p>{lines[i]}</p>""")
# Debugging: Print all written lines to ensure correctness
op.seek(0)
for line in op:
    print(line)

op.close()
f.close()
