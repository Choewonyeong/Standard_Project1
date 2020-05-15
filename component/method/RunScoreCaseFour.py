# 예정가 고시금액 미만
from pandas import DataFrame


def returnManagementScore(rate):
    if rate >= 1:
        return 5
    elif rate >= 0.9:
        return 4.5
    elif rate >= 0.8:
        return 4
    elif rate >= 0.7:
        return 3.5
    elif rate < 0.7:
        return 3


class RunScoreCaseFour:
    limit = 0.87745               # 낙찰하한율

    def __init__(self, price, rateStd, capital, asset, flowAsset, flowFan, rateReduce, point):
        self.price = price
        self.rateStd = rateStd
        self.capital = capital
        self.asset = asset
        self.flowAsset = flowAsset
        self.flowFan = flowFan
        self.rateReduce = rateReduce
        self.point = {point > 3.5: 3.5, point < -4: -4}.get(True, point)
        self.__createRawData__()
        self.__createScoreData__()

    def __createRawData__(self):
        self.perRanges = []
        self.perPrices = []
        currentRate = 1
        while True:
            if currentRate <= self.limit:
                break
            else:
                self.perRanges.append(f"{round(currentRate*100, 3).__format__('.1f')}%")
                price = self.price*currentRate
                self.perPrices.append(format(int(price), ','))
            currentRate -= self.rateReduce

    def __createManagementScore__(self):
        rateAsset = (self.capital/self.asset)/self.rateStd
        rateFlow = (self.flowAsset/self.flowFan)/self.rateStd
        rateAssetScore = returnManagementScore(rateAsset)
        rateFlowScore = returnManagementScore(rateFlow)
        self.managementScore = rateAssetScore + rateFlowScore

    def __createScoreData__(self):
        def returnScore(p):
            priceRate = round(p/self.price, 4)
            if p <= self.price and priceRate >= 0.8825:
                return 85
            else:
                var = (0.88 - priceRate)*100
                var *= -1 if var < 0 else 1
                if 90 - 20*var <= 2:
                    return 2
                return 90 - 20*var
        self.priceScores = []
        self.totalScores = []
        for price in self.perPrices:
            price = int(price.replace(',', ''))
            score = returnScore(price) if returnScore(price) > 2 else 2
            total = score + self.managementScore + self.point
            self.priceScores.append(score.__format__('.2f'))
            self.priceScores.append(total.__format__('.3f'))

    def ReturnToDataFrame(self):
        df = DataFrame(data=self.perRanges, columns=['낙찰률'])
        df['낙찰가'] = self.perPrices
        df['가격점수'] = self.priceScores
        df['경영점수'] = self.managementScore.__format__('.3f')
        df['신인도점수'] = self.point.__format__('.1f')
        df['총점'] = self.totalScores
        return df