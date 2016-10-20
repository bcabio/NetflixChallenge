from __future__ import division
import os
import math

numValues = 0
sumSquaredValues = 0
totalRating = 0
movies = 0

driverDir = os.path.dirname(__file__)
print driverDir
trainingSetDir = os.path.join(driverDir, 'training_set')
for filename in os.listdir(trainingSetDir):
    with open(os.path.join(trainingSetDir, filename), "r") as f:
        for line in f:
            if line.find(":") != -1:
                print line
            else:
                date = line[line.find(",")+3:]
                # print date
                movies += 1
                ratingPre = line[line.find(",")+1:]
                ratingFinal = ratingPre[:ratingPre.find(",")]
                totalRating += int(ratingFinal)
                # print totalRating
                averageRatingPerMovie = totalRating/movies
                # print str(averageRatingPerMovie) + "movie"

                delta = int(ratingFinal) - averageRatingPerMovie
                numValues += 1
                sumSquaredValues += delta*delta



        movies = 0
        totalRating = 0


print numValues
print math.sqrt(sumSquaredValues/numValues)
# #
# with open("qualifying.txt") as f:
#     for line in f:
#         print line
#


# with open('probe.txt') as f:
#     for line in f:
#         if ":" in line:
#             print(line)
