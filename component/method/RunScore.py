class RunScore:
    score = 0  # 가격점수
    limit = 0  # 낙찰하한율
    priceRate = 0 # 낙찰가/예정가
    rateSelfCapital = 0 # 자기자본비율
    rateFlowAsset = 0 # 유동비율

    def __init__(self,
                 price,
                 priceSub,
                 PQ,
                 rateReduce,
                 point,
                 rateS=0,       # 기준비율
                 selfCapital=0, # 자기자본
                 totalAsset=0,  # 총자산
                 flowAsset=0,   # 유동자산
                 flowFan=0):    # 유동부채
        self.price = price # 에정가격
        self.priceSub = priceSub # 고시금액
        self.pointMain = PQ # 기술(PQ)점수 또는 경영점수
        self.pointSub = point # 신인도점수
        self.rateReduce = rateReduce
        self.result = []
        self.rateS = rateS
        self.selfCapital = selfCapital
        self.totalAsset = totalAsset
        self.flowAsset = flowAsset
        self.flowFan = flowFan

        # 예정가에 따른 낙찰하한가 산정 및 기술(PQ)점수 환산
    def __setLimit__(self):
        if self.price >= 1000000000:
            self.limit = 0.79995
            self.PQ = self.PQ*0.7
        elif self.price >= 500000000:
            self.limit = 0.85495
            self.PQ = self.PQ*0.5
        elif self.price >= self.priceSub:
            self.limit = 0.86475
            self.PQ = self.PQ*0.3
        elif self.price < self.priceSub:
            self.limit = 0.87745
            self.PQ = 1

    # 낙찰율 감소율에 따른 낙찰가 산출
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
