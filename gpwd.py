from random import randrange

def verification(nbr):
        veri = False 
        if type(nbr) == type(1):
            veri = True
            
        return veri
    
class  Gpwd:
    
    def __init__(self, nbrc):
        self.nbrc = nbrc
        
    def gpwds(self):
        
        if verification(self.nbrc):  
            AlphabetMag =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            AlphabetMin =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            Numerique = [0,1,2,3,4,5,6,7,8,9]
            Caracterespeciale = ['{','=','+','_','-',')','(','*','&','^','%','$','#','@','!','~']
            pwd = []
            for i in range(self.nbrc):
                r1 = randrange(5)
                if r1 == 1 :
                    r2 = randrange(26)
                    pwd.append(AlphabetMag[r2])
                elif r1 == 2 :
                    r2 = randrange(26)
                    pwd.append(AlphabetMin[r2])
                elif r1 == 3 :
                    r2 = randrange(10)
                    pwd.append(Numerique[r2])
                else :
                    r2 = randrange(16)
                    pwd.append(Caracterespeciale[r2])
            
            spwd = ""
            for f in pwd:
                spwd = spwd + str(f) 
            
            return spwd
        
    
   