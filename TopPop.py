import csv

## creation de l'URM binaire sommée

# nombre de tracks
N = 20635
# nom du fichier csv des interations 
interactions = "train.csv"
# nom du fichier csv des playlist cibles 
targets = "target_playlists.csv"
# nom du fichier csv de soumission 
submissions = "top_pop_submission01.csv"
# liste des tracks
L = []                                  

# initialisation de la liste d'utilisation des tracks
for loop in range(N):
    L.append(0);
    
# ouverture du csv en lecture
fi = open(interactions, 'r')
cri = csv.reader(fi)

# variable de suivi d'itération (+ première itération à sauter car str)
iterationRead = -1

for row in cri :
    if iterationRead == -1 :
        iterationRead += 1
    else :
        L[int(row[1])] += 1
        iterationRead += 1
        
fi.close()

print (L)
print ("\nNombre d'itérations :", iterationRead)



## recherche et classement des 10 tacks les plus populaires

topPop = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for track in range(10, len(L)) :
    classement = 0
    while(classement < 10 and L[track] > L[topPop[classement]]) :
        if classement == 0 :
            topPop[classement] = track
            classement += 1
        else :
            a = topPop[classement]
            topPop[classement - 1] = a
            topPop[classement] = track
            classement += 1
    
print("\nClassement croissant :", topPop)

isFirstLign = True
recommendations = ""

for loop in range (len(topPop) - 1, -1, -1) :
    track_final = topPop[loop]
    if isFirstLign :
        recommendations += str(track_final)
        isFirstLign = False
    else :
        recommendations = recommendations + " " + str(track_final)
    
print(recommendations)

ft = open(targets, 'r')
fs = open(submissions, 'w+', newline='')
crt = csv.reader(ft)
crs = csv.writer(fs)

isFirstLign = True

for row in crt :
    if isFirstLign :
        row.append("track_ids")
        crs.writerow(row)
        isFirstLign = False
    else :
        row.append(recommendations)
        crs.writerow(row)
        
ft.close()
fs.close() 