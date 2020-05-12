class RunScore:
    def __init__(self, price, minRate, rate, perRange, PQTran, point):
        self.price = price # 예정가격
        self.minRate = minRate # 낙찰 하한률 -> 얘도 금액별 다름
        self.rate = rate # 추첨률
        self.perRange = perRange # 낙찰률 감소율
        self.PQTran = PQTran # 기술 점수
        self.point = point # 신인도 점수
        self.result = []

    # 낙찰율 감소율, 낙찰가 산출
    def __perRangesAndPrices__(self):
        self.perRanges = []
        self.prices = []
        perRange = 1
        while True:
            if perRange <= self.minRate:
                break
            else:
                perRange -= self.perRange
                self.perRanges.append(perRange)
                price = self.price*perRange
                self.prices.append(price)

    # 가격점수
    def __priceScores__(self):
        self.priceScores = []

    # 추정가격 10억원 이상
    def __firstCase__(self, price):
        priceRate = round(price/self.price, 4)
        if priceRate >= 0.96:
            score = 22
        else:
            var = (0.88 - priceRate)*100
            var *= -1 if var < 0 else 1
            score = 30 - var
        return score
    
    # 추정가격 5억원 이상 10억원 미만
    def __SecondCase__(self, price):
        priceRate = round(price/self.price, 4)
        if priceRate >= 0.905:
            score = 45
        else:
            var = (0.88 - priceRate)*100
            var *= -1 if var < 0 else 1
            score = 50 - 2*var
        return score

    # 추정가격 고시금액 이상 5억원 미만
    def __ThirdCase__(self, price):
        priceRate = round(price/self.price, 4)
        if priceRate >= 0.8928:
            score = 65
        else:
            var = (0.88 - priceRate)*100
            var *= -1 if var < 0 else 1
            score = 70 - 4*var
        return score
    
    # 추정가격 고시금액 미만
    def __FourthCase__(self, price):
        priceRate = round(price/self.price, 4)
        if priceRate >= 0.8825:
            score = 85
        else:
            var = (0.88 - priceRate)*100
            var *= -1 if var < 0 else 1
            score = 90 - 20*var
        return score

    # 최저평점 2점
    def __LastCase__(self, score):
        return 2 if score <= 2 else score
