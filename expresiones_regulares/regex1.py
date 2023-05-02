import re
text = "The quick brown fox jumps pver the lazy dog"

# ^ ->Significa que cuando comienza la linea con ...
x = re.search("^The.*dog$", text)

if x:
    print("YES")
else:
    print("NO")
