import re, os, utils, time as t

u = utils.utils()
u.printh("To change the MD file copy paste the file and update the file.md as your intended filename")

# Clear the output HTML file
op = open("output.html", "w")
op.writelines("")
op.close()

# Open markdown file and output HTML file for writing
markdown = open("file.md", "r")
op = open("output.html", "a")

# Read markdown lines
md = markdown.readlines()

# Write initial HTML boilerplate
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
head = False

# Append an "ended" marker to md list
md.append("ended")

# Processing markdown lines
length = len(md)
for j in range(len(md)):
    text = ''
    
    # Debug: Print current line
    print(f"Processing line {j}: {md[j].strip()}")
    
    # Skip if the current line is empty
    if md[j].strip() == "":
        continue

    # Check for the next line and toggle heading state
    if md[j + 1] != "ended" and u.isHeading(md[j + 1]):
        head = not head
        if head:
            op.writelines(f"""\n<div style="background-color: white; padding-bottom: 20px; border-radius: 25px; margin: 0rem 0rem">""")
        else:
            op.writelines("""</div>\n""")
    else:
        op.writelines(f"""</div>\n""")
        continue    

    # ++++++++++++++ Heading ++++++++++++++++++++++
    if md[j][0] == '#':
        h = md[j].count('#')  # Count the number of `#` to determine heading level
        md[j] = (md[j].replace("#", "")).strip()
        id = md[j].replace(" ", "-").lower()  # Generate ID for the heading
        op.writelines(f"""\n<h{h} style="text-align: center; background-color:black; color:white; padding: 25px;" id="{id}">{md[j]}</h{h}>\n""")

    # ++++++++++++++ Links ++++++++++++++++++++++
    elif all(link in md[j] for link in ["[", "]", "(", ")"]):
        start = md[j].index("[")
        end = md[j].index("]")
        text = md[j][start+1:end]  # Extract the link text
        under_ = text.replace(" ", "-").lower()  # Create an ID
        op.writelines(f"""<h4 style="text-align: center;"><a style="text-decoration: none; color: blue;" href="#{under_}">{text}</a></h4>\n""")

    # ++++++++++++++ CodeBlock ++++++++++++++++++++++
    elif "```" in md[j]:
        codeblock = not codeblock
        if codeblock:
            j += 1
            op.writelines(f"""<h4 style="background-color: rgb(99, 99, 99); color: white; margin: 0.2rem 10rem; padding: 5px; border-radius: 5px; text-align: center;">{md[j].strip()}</h4>\n""")
        else:
            continue
    
    # ++++++++++++++ Bold and Italics ++++++++++++++++++++++
    elif "***" in md[j] or "**" in md[j] or "*" in md[j]:
        start, end, starBeg, starEnd  = u.findPos(md[j], "*")
        str_ = md[j].replace(md[j][starBeg:starEnd+start], md[j][start:end])
        if "***" in md[j]:
            op.writelines(f"""<em><strong style="margin-left: 10%;">{str_}</strong></em>""")
        elif "**" in md[j]:
            op.writelines(f"""<strong style="margin-left: 25%;">{str_[:-1]}</strong>""")
        elif "*" in md[j]:
            op.writelines(f"""<em>{str_}</em>""")

    # ++++++++++++++ Regular Paragraphs ++++++++++++++++++++++
    else:
        op.writelines(f"""\n<p style="text-align: center;">&emsp;{md[j].strip()}</p>\n""")

    t.sleep(0.01)
    u.printc(f"""Processing line {j} of {length-2}""")

# Close the HTML tags
op.writelines("""
</body>
</html>""")

# Close files
markdown.close()
op.close()

print()
u.printh(f"""Processing completed: {length-2} lines""")
