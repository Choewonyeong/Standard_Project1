# 예정가 5억원 이상
from pandas import DataFrame


class RunScoreCaseTwo:
    limit = 0.85495               # 낙찰하한율

    def __init__(self, price, PQ, rateReduce, point):
        self.price = price
        self.PQ = round(PQ*0.5, 3)
        self.rateReduce = rateReduce
        self.point = {point > 1: 1, point < -4: -4}.get(True, point)
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

    def __createScoreData__(self):
        def returnScore(p):
            priceRate = round(p/self.price, 4)
            if p <= self.price and priceRate >= 0.905:
                return 45
            else:
                var = (0.88 - priceRate)*100
                var *= -1 if var < 0 else 1
                if 50 - 2*var <= 2:
                    return 2
                return 50 - 2*var
        self.priceScores = []
        self.totalScores = []
        for price in self.perPrices:
            price = int(price.replace(',', ''))
            score = returnScore(price) if returnScore(price) > 2 else 2
            total = score + self.PQ + self.point
            self.priceScores.append(score.__format__('.2f'))
            self.totalScores.append(total.__format__('.3f'))

    def ReturnToDataFrame(self):
        df = DataFrame(data=self.perRanges, columns=['낙찰률'])
        df['낙찰가'] = self.perPrices
        df['가격점수'] = self.priceScores
        df['기술점수'] = self.PQ.__format__('.3f')
        df['신인도점수'] = self.point.__format__('.1f')
        df['총점'] = self.totalScores
        return df