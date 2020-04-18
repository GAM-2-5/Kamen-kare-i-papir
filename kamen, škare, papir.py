import random #otvaramo 'random' knjižnicu

print('Pravila igre:\n'
      +'KAMEN vs PAPIR -> PAPIR pobjeđuje\n'
      +'KAMEN vs ŠKARE -> KAMEN pobjeđuje\n'
      +'PAPIR vs ŠKARE -> ŠKARE pobjeđuju\n') #na početku ispisana pravila za igru

while True: #beskonačna petlja
    
    print('Unesi svoj izbor: \n 1. KAMEN \n 2. PAPIR \n 3. ŠKARE \n') #mogućnosti odabira

    izbor = int(input('Sad je tvoj red: ')) #unos odabira (ako je odabir izvan domene, ponoviti odabir)
    while izbor > 3 or izbor < 1: 
        izbor = int(input('Unesi svoj izbor ovdje:'))
        
    if izbor == 1: 
        izbor_i = 'KAMEN'
            
    elif izbor == 2:
        izbor_i = 'PAPIR'

    else:
        izbor_i = 'ŠKARE' #svakom broju pridodajemo mogućnost


    print('Tvoj izbor je: ' + izbor_i) #ispis izbora, nakon kojeg je red na kompjuteru
    print('\nSad je red na kompjuteru... ') 


    kompjuter_izbor = random.randint(1, 3) #pomoću ove funkcije kompjuter nasumučno odabere jedan od tri broja

    if kompjuter_izbor == 1:
        kompjuter_izbor_i = 'KAMEN'

    elif kompjuter_izbor == 2:
        kompjuter_izbor_i = 'PAPIR'

    else:
        kompjuter_izbor_i = 'ŠKARE' #svakom izboru kompjutera pridodajemo mogućnost

    print('Kompjuterov izbor je: ' + kompjuter_izbor_i) #ispis izbora
    print(izbor_i + ' vs. ' + kompjuter_izbor_i)


    #određivanje i ispis rezultata     
    if (( izbor == 1 and kompjuter_izbor == 2) or (izbor == 2 and kompjuter_izbor == 1)):
        print ('\nPAPIR pobjeđuje ->', end='')
        rezultat='PAPIR'


    elif((izbor == 1 and kompjuter_izbor == 3) or (izbor == 3 and kompjuter_izbor ==1)):
        print ('\nKAMEN pobjeđuje ->', end = '')
        rezultat= 'KAMEN'

    elif (kompjuter_izbor == izbor):
          rezultat = '0'

    else:
        print('ŠKARE pobjeđuju ->', end = '')
        rezultat = 'ŠKARE'


    #određivanje i ispis pobjednika
    if rezultat == izbor_i:
            print (' POBIJEDIO SI')

    elif rezultat == kompjuter_izbor_i:
            print( 'IZGUBIO SI')

    else:
        print('\nIZJEDNAČENO JE')
        
    print('\nŽeliš igrati ponovo? (d/n)') #upit za nastavak igre
    odg = input()

    if odg == 'n' or odg == 'N':
        print('\nHVALA NA SUDJELOVANJU!')
        break #ukoliko je odgovor ne ispisuje se gornja poruka i igra završava naredbom break

   
    


    



            
    
