good = (r"""
            xxxxxxx                 mmmmmmmmmmmm               
           xxx   xxx               mmm        mmm              
      xxxxxxx     xxxxxxx         mm            mm             
      xx   xxx   xxx   xx         mm            mm             
     xx     xxxxxxx     xx       mm              mm            
      xx   xxxxxxxxx   xx        mm              mm            
       xxxxx xxxxx xxxxx         mm              mm            
             xxxxx               mm              mm            
             xxxxx              UUUUUUUUUUUUUUUUUUUU           
             xxxxx              UUUUUUUUUUUUUUUUUUUU           
             xxxxx              UUUUUUUUU   UUUUUUUU           
             xxxxx              UUUUUUUU     UUUUUUU           
             xxxxx              UUUUUUUUU   UUUUUUUU           
             xxxxx               UUUUUUUI   IUUUUUU            
             xxxxx               UUUUUUUI   IUUUUUU            
          xxxxxxxx                UUUUUUUuuuUUUUUU             
          xxxxxxxx                 UUUUUUUUUUUUUU              
             xxxxx                                             
          xxxxxxxx          L O C K   a n d   K E Y            
          xxxxxxxx                                                       
             xxxxx                  
""")

bad = (r"""
             \|/
            .-*-         
           / /|\         
          _L_            
        ,"   ".          
    (\ /  O O  \ /)      
     \|    _    |/       
       \  (_)  /         
       _/.___,\_         
      (_/ alf \_)      
""")
has_key = True
if has_key:
    outcome = "Click: flicker on"
    print(good)
else:
    outcome = "Doom: Doomer shoomer"
    print(bad)
print(outcome)