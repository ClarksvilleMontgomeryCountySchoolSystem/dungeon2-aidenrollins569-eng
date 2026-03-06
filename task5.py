good = (r"""
Legend: Fruits and berries
 ,
 \`.__.
  `._,'
""")

bad = (r"""
Doom: Lost cause
               _                     
              | |                    
 ___  __ _  __| |_ __   ___  ___ ___ 
/ __|/ _` |/ _` | '_ \ / _ \/ __/ __|
\__ \ (_| | (_| | | | |  __/\__ \__ \
|___/\__,_|\__,_|_| |_|\___||___/___/                                     
""")

escaped = True
if escaped:
    outcome = good
else:
    outcome = bad
print(outcome)