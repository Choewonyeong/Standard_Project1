def TranPQScore(priceMain, priceSub, score):
    # 추정가격 10억원 이상 => PQ * 0.7
    if priceMain >= 1000000000:
        print("1", priceMain, round(score*0.7, 3))
        return round(score*0.7, 3)
    # 추정가격 5억원 이상 => PQ * 0.5
    elif priceMain >= 500000000:
        print("2", priceMain, round(score*0.5, 3))
        return round(score*0.5, 3)
    # 추정가격 고시금액 이상 => PQ * 0.3
    elif priceMain >= priceSub:
        print("3", priceMain, round(score*0.3, 3))
        return round(score*0.3, 3)
    # 추정가격 고시금액 미만
    else:
        print("4", priceMain, round(score*0.1, 3))
        return round(score*0.1, 3)