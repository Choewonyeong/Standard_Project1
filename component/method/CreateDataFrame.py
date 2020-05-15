from component.method.RunScoreCaseOne import RunScoreCaseOne
from component.method.RunScoreCaseTwo import RunScoreCaseTwo
from component.method.RunScoreCaseThree import RunScoreCaseThree
from component.method.RunScoreCaseFour import RunScoreCaseFour


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


def CreateScoreCaseTwo(priceMain, priceHigh, priceLow, PQ, rateReduce, point, otherInfo):
    runMain = RunScoreCaseTwo(priceMain, PQ, rateReduce, point)
    runHigh = RunScoreCaseTwo(priceHigh, PQ, rateReduce, point)
    runLow = RunScoreCaseTwo(priceLow, PQ, rateReduce, point)
    names = ['(주)스탠더드시험연구소']
    dataFrames = [[runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()]]
    del runMain, runHigh, runLow

    for info in otherInfo:
        name = info[0]
        priceHigh = info[1]
        priceLow = info[2]
        PQ = info[3]
        point = info[4]
        runMain = RunScoreCaseTwo(priceMain, PQ, rateReduce, point)
        runHigh = RunScoreCaseTwo(priceHigh, PQ, rateReduce, point)
        runLow = RunScoreCaseTwo(priceLow, PQ, rateReduce, point)
        names.append(name)
        dataFrames.append([runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()])
        del runMain, runHigh, runLow

    return names, dataFrames


def CreateScoreCaseThree(priceMain, priceHigh, priceLow, PQ, rateReduce, point, otherInfo):
    runMain = RunScoreCaseThree(priceMain, PQ, rateReduce, point)
    runHigh = RunScoreCaseThree(priceHigh, PQ, rateReduce, point)
    runLow = RunScoreCaseThree(priceLow, PQ, rateReduce, point)
    names = ['(주)스탠더드시험연구소']
    dataFrames = [[runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()]]
    del runMain, runHigh, runLow

    for info in otherInfo:
        name = info[0]
        priceHigh = info[1]
        priceLow = info[2]
        PQ = info[3]
        point = info[4]
        runMain = RunScoreCaseThree(priceMain, PQ, rateReduce, point)
        runHigh = RunScoreCaseThree(priceHigh, PQ, rateReduce, point)
        runLow = RunScoreCaseThree(priceLow, PQ, rateReduce, point)
        names.append(name)
        dataFrames.append([runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()])
        del runMain, runHigh, runLow

    return names, dataFrames


def CreateScoreCaseFour(priceMain, priceHigh, priceLow, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point, otherInfo):
    runMain = RunScoreCaseFour(priceMain, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point)
    runHigh = RunScoreCaseFour(priceHigh, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point)
    runLow = RunScoreCaseFour(priceLow, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point)
    names = ['(주)스탠더드시험연구소']
    dataFrames = [[runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()]]
    del runMain, runHigh, runLow

    for info in otherInfo:
        name = info[0]
        priceHigh = info[1]
        priceLow = info[2]
        rateStd = info[3]
        capital = info[4]
        asset = info[5]
        flowAsset = info[6]
        flowFan = info[7]
        point = info[8]
        runMain = RunScoreCaseFour(priceMain, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point)
        runHigh = RunScoreCaseFour(priceHigh, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point)
        runLow = RunScoreCaseFour(priceLow, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point)
        names.append(name)
        dataFrames.append([runMain.ReturnToDataFrame(), runHigh.ReturnToDataFrame(), runLow.ReturnToDataFrame()])
        del runMain, runHigh, runLow

    return names, dataFrames
