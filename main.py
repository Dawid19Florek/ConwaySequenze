def generate_conway_sequence(n):
    sequence = "09"  #erste sequenz / zahl eingeben
    print(sequence) #stratsequenz ausgeben
#str wandelt zahl in string
#len wie count in c#


    for _ in range(n - 1):   # die anzahl der generationen -1 da wir die erste schon haben
        new_sequence = ""    #eine neue leere sequenz erstellen
        count = 1            #count auf 1 setzen da eine zahl auf jeden fall vorhanden ist

        for i in range(1, len(sequence)):       #for von 1 bis anzahl der zeichen im string
            if sequence[i] == sequence[i - 1]:  #falls i in der sequenz diesselbe zahl wie die vorcherige wird count+1 gerechnet
                count += 1
            else:
                new_sequence += str(count) + sequence[i - 1] #den count und die dazugehörige zahl in die new sequenc eingeben
                count = 1# count wieder auf 1 setzen

        new_sequence += str(count) + sequence[-1]#letzte sequenz wird zu der sequenz hinzugefügt
        sequence = new_sequence
        print(sequence)


generation_count = 19 #wie oft möchte ich das ausgeben

generate_conway_sequence(generation_count)#aufrufen der methode



