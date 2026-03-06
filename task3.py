good = (r"""
     _               _               
    | |             | |              
 ___| |__   __ _  __| | _____      __
/ __| '_ \ / _` |/ _` |/ _ \ \ /\ / /
\__ \ | | | (_| | (_| | (_) \ V  V / 
|___/_| |_|\__,_|\__,_|\___/ \_/\_/  
""")

bad = (r"""
  __ _       _     _   
 / _(_)     | |   | |  
| |_ _  __ _| |__ | |_ 
|  _| |/ _` | '_ \| __|
| | | | (_| | | | | |_ 
|_| |_|\__, |_| |_|\__|
        __/ |          
       |___/        
""")
guard_awake = False
if not guard_awake:
    outcome = "Shadow: Attack and run"
    print(good)
else:
    outcome = "Doom: Doom and despair"
    print(bad)
print(outcome)