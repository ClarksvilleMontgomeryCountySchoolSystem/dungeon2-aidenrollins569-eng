good = (r"""
 ,
 \`.__.
  `._,'
""")

bad = (r"""
               _                     
              | |                    
 ___  __ _  __| |_ __   ___  ___ ___ 
/ __|/ _` |/ _` | '_ \ / _ \/ __/ __|
\__ \ (_| | (_| | | | |  __/\__ \__ \
|___/\__,_|\__,_|_| |_|\___||___/___/                                     
""")

escaped = True
if escaped:
    outcome = "Legend: Fruits and berries"
    print(good)
else:
    outcome = "Doom: Lost cause"
    print(bad)
print(outcome)