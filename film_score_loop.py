# Online Python - IDE, Editor, Compiler, Interpreter


# lav tæller
def tæl(film_antal,score_antal):
    
    counter_1 = 1
    for i in range(film_antal):
        
        #definer starts counter
        counter_2 = 1
        
        # lav loop, der gentager sig et bestemt antal gange
        for j in range(score_antal):
            
            # print counter
            label = "film_" + str(counter_1) + "_score_" + str(counter_2)
    
            print(label)
            
            # Tilføj 1 i slutning af loop.
            counter_2 = counter_2 + 1


        counter_1 = counter_1 + 1
        
# Aktiver tæller       
tæl(2, 5)



