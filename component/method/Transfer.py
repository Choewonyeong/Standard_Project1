def TransferCntLoop(cntLoop, caution):
    cntLoop = cntLoop.replace(',', '')
    try:
        cntLoop = int(cntLoop)
        return cntLoop
    except:
        if cntLoop == '':
            caution.setVisible(True)
            caution.setText('총 반복수를 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0


def TransferPrice(price, caution):
    price = price.replace(',', '')
    try:
        cntLoop = int(price)
        return price
    except:
        if price == '':
            caution.setVisible(True)
            caution.setText('예비가격 기초금액을 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0


def TransferRatePlus(rate, caution):
    rate = rate.replace(',', '')
    rate = rate.replace('%', '')
    try:
        rate = float(rate)
        return rate
    except:
        if rate == '':
            caution.setVisible(True)
            caution.setText('상한율을 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0


def TransferCntPlus(cnt, caution):
    cnt = cnt.replace('개', '')
    try:
        cnt = int(cnt)
        return cnt
    except:
        if cnt == '':
            caution.setVisible(True)
            caution.setText('상한범위 추첨수를 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0


def TransferRateMinus(rate, caution):
    rate = rate.replace(',', '')
    rate = rate.replace('%', '')
    try:
        rate = float(rate)
        return rate
    except:
        if rate == '':
            caution.setVisible(True)
            caution.setText('하한율을 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0


def TransferCntMinus(cnt, caution):
    cnt = cnt.replace('개', '')
    try:
        cnt = int(cnt)
        return cnt
    except:
        if cnt == '':
            caution.setVisible(True)
            caution.setText('하한범위 추첨수를 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0


def TransferCntTotal(cnt, caution):
    cnt = cnt.replace('개', '')
    try:
        cnt = int(cnt)
        return cnt
    except:
        if cnt == '':
            caution.setVisible(True)
            caution.setText('예정가액 추첨수를 입력하세요.')
        else:
            caution.setVisible(True)
            caution.setText('형식이 맞지 않습니다.')
        return 0
