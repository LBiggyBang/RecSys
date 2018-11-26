# Bryan BESSAUD           #
# 22/11/2018              #
# RecSys Competition 2018 #
# Politecnico di Milano   #

# mandatory imports
from Utils import CSVinteraction
from Utils import formatting

# csv file with the target playlists 
targetsCSV = "target_playlists.csv"
# csv file for submissions
submissionCSV = "submission.csv"
# csv file for interactions, used to build the URM
interactionsCSV = "train.csv"
# csv file for tracks, used to get the number of tracks
tracksCSV = "tracks.csv"
#extracting the interactions into a list
interationsList = CSVinteraction.fromCSVtoList(interactionsCSV)


##########
# creation of the binarized and summed URM

# emptu URM
urm = []*(CSVinteraction.getCSVtotalRows(tracksCSV) - 1)              

# summinng the encounters of each track in the playlists
for index in range(1, len(interationsList)) :
    urm[interationsList[1]] += 1


##########
# building the recommendations
    
# initial recommendations to be changed
topPop = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# searching the 10 most popular tracks (skipping the first 10 ones already in the recommendations)
for track in range(10, len(urm)) :
    ranking = 0
    while(ranking < 10 and urm[track] > urm[topPop[ranking]]) :
        if ranking == 0 :
            topPop[ranking] = track
            ranking += 1
        else :
            swapVariable = topPop[ranking]
            topPop[ranking - 1] = swapVariable
            topPop[ranking] = track
            ranking += 1
    
# putting the list into the right order
finalTopPop = []*10
for index in range(0, 10) :
    finalTopPop[index] = topPop[9 - index]

##########○
# establishing the csv file for submissions

# transforming the list of recommendations into a unique string
recommendationsString = 
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