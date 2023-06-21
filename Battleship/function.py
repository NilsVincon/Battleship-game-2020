# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:46:53 2021

@author: nilsv
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:32:58 2021

@author: natho
"""

def placement_bateau(long,tab,tableau,window,textetoprint):
    """
    

    long,tab,tableau,window,textetoprint
    ----------
    long : int
        longueur bateau
    tab : tableau de str
        tableau de A à J
    tableau : tableau de int
        matrice 10x10
    window : pysimplegui
        fenetre permettant d'afficher le placement sur Pysimplegui
    textetoprint : str
        affiche le message au joueur

    tableau,window
    -------
    tableau : tableau de int
        matrice 10x10 
    window : pysimplegui
        fenetre permettant d'afficher le placement sur Pysimplegui

    """
    positionC = False
    while positionC == False :
        sens=str(input(textetoprint))
        if sens== "H":
            croiseurC=str(input("Colonne"))
            croiseurL=str(input("Ligne"))
            iline = int(croiseurL) - 1
            j = tab.index(croiseurC)
            for i in range (j,j+long):
                positionC = True
                icol = i
                if tableau[iline][icol] == 1 :
                   print("Impossible de placer ici, emplacement déja pris")
                   for k in range (j,i):
                       icol= k
                       tableau[iline][icol] = 0
                       window[tab[k]+croiseurL].Update('')      
                   positionC = False
                   break    
                else :   
                    tableau[iline][icol] = 1
                    window[tab[i]+croiseurL].Update('\u2b24')    
                
            
        if sens == "V":
            croiseurC=str(input("Colonne"))
            croiseurL=int(input("Ligne"))
            icol = tab.index(croiseurC)
            for i in range (croiseurL,croiseurL+long):
                positionC = True
                if tableau[i-1][icol] == 1 :
                    print("Impossible de placer ici, emplacement déja pris")
                    for k in range(croiseurL,i):
                        tableau[k-1][icol] = 0
                        window[croiseurC+str(k)].Update('')
                    positionC = False
                    break    
                else :
                    tableau[i-1][icol] = 1
                    window[croiseurC+str(i)].Update('\u2b24')    
                
    return tableau,window

def placement_ordi(long,tab,tableau1):
    """
    

    long,tab,tableau1
    ----------
    long : int
        longueur bateau
    tab : tableau de str
        tableau de A à J
    tableau1 : tableau de int
        matrice 10x10.

    tableau1
    -------
    tableau1 : int
         matrice 10x10.

    """
    from random import randint
    positionCordi=False
    while positionCordi == False :
            sens2=randint(1,2)
            if sens2== 1:
                croiseurC=str(tab[randint(1,10-long)])
                croiseurL=str(randint(1,10))
                iline = int(croiseurL) - 1
                j = tab.index(croiseurC)
                for i in range (j,j+long):
                    positionCordi = True
                    icol = i
                    if tableau1[iline][icol] == 1 :
                       for k in range (j,i):
                           icol= k
                           tableau1[iline][icol] = 0
                       positionCordi = False
                       break    
                    else :   
                        tableau1[iline][icol] = 1    
                        
                    
                
            if sens2 == 2:
                croiseurC=str(tab[randint(0,9)])
                croiseurL=int(randint(1,10-long))
                icol = tab.index(croiseurC)
                for i in range (croiseurL,croiseurL+long):
                    positionCordi = True
                    if tableau1[i-1][icol] == 1 :
                        for k in range(croiseurL,i):
                            tableau1[k-1][icol] = 0
                        positionCordi = False
                        break    
                    else :
                        tableau1[i-1][icol] = 1 
    return tableau1