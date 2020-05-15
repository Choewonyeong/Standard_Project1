from component.method.RunScoreCaseOne import RunScoreCaseOne


def CreateScoreCaseOne(priceMain, priceHigh, priceLow, PQ, rateReduce, point, otherInfo):
    runMain = RunScoreCaseOne(priceMain, PQ, rateReduce, point)
    runHigh = RunScoreCaseOne(priceHigh, PQ, rateReduce, point)
    runLow = RunScoreCaseOne(priceLow, PQ, rateReduce, point)
    names = ['(주)스탠더드시험연구소']
    dataFrames = [[runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()]]
    del runMain, runHigh, runLow

    for info in otherInfo:
        name = info[0]
        priceHigh = info[1]
        priceLow = info[2]
        PQ = info[3]
        point = info[4]
        runMain = RunScoreCaseOne(priceMain, PQ, rateReduce, point)
        runHigh = RunScoreCaseOne(priceHigh, PQ, rateReduce, point)
        runLow = RunScoreCaseOne(priceLow, PQ, rateReduce, point)
        names.append(name)
        dataFrames.append([runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()])
        del runMain, runHigh, runLow

    return names, dataFrames


"""
for x, name in enumerate(names):
    for y, dataFrame in enumerate(dataFrames):
        print(dataFrames[y][x])
        
A1
B1
C1
A2
B2
C2
A3
B3
C3
"""