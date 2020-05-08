from threading import Thread
from pandas import DataFrame, cut
from random import sample


class RunExtract:
    priceExtracts = []
    priceRates = []  # 가격범위

    def __init__(self, options):
        self.cntLoop = int(options[0])
        self.colCntLoops = [i + 1 for i in range(self.cntLoop)]
        self.price = int(options[1])
        self.ratePlus = options[2]
        self.rangePlus = options[3]
        self.cntPlus = options[4]
        self.rateMinus = options[5]
        self.rangeMinus = options[6]
        self.cntMinus = options[7]
        self.rangeGap = options[8]
        self.cntTotal = options[9]

    # 실행시간 : 3.5초
    def ReturnExtract(self):
        def __run__(dfSource, start, end, price, rangePlus, cntPlus, rangeMinus, cntMinus, cntTotal):
            for cnt in range(start, end):
                extractPlus = sample(range(price, rangePlus), cntPlus)
                extractMinus = sample(range(rangeMinus, price), cntMinus)
                extractTotal = sample(extractPlus + extractMinus, cntTotal)
                average = int(sum(extractTotal) / cntTotal)
                dfSource.append([0] + extractPlus + extractMinus + extractTotal + [average])
                self.priceExtracts.append(format(average, ','))
                self.priceRates.append(round(average / price - 1, 8))

        result = []
        threadFirst = Thread(target=__run__, args=[result, 0, self.cntLoop // 4, self.price,
                                                   self.rangePlus, self.cntPlus,
                                                   self.rangeMinus, self.cntMinus,
                                                   self.cntTotal])
        threadSecond = Thread(target=__run__, args=[result, self.cntLoop // 4, self.cntLoop // 2, self.price,
                                                    self.rangePlus, self.cntPlus,
                                                    self.rangeMinus, self.cntMinus,
                                                    self.cntTotal])
        threadThird = Thread(target=__run__, args=[result, self.cntLoop // 2, self.cntLoop // 4 * 3, self.price,
                                                   self.rangePlus, self.cntPlus,
                                                   self.rangeMinus, self.cntMinus,
                                                   self.cntTotal])
        threadFourth = Thread(target=__run__, args=[result, self.cntLoop // 4 * 3, self.cntLoop, self.price,
                                                    self.rangePlus, self.cntPlus,
                                                    self.rangeMinus, self.cntMinus,
                                                    self.cntTotal])
        threadFirst.start()
        threadSecond.start()
        threadThird.start()
        threadFourth.start()
        threadFirst.join()
        threadSecond.join()
        threadThird.join()
        threadFourth.join()

        columns = ['반복횟수']
        for num in range(self.cntPlus):
            columns.append(f"추첨-상한가{num + 1}")
        for num in range(self.cntMinus):
            columns.append(f"추첨-하한가{num + 1}")
        for num in range(self.cntTotal):
            columns.append(f"추점-예정가{num + 1}")
        columns.append('산술평균가액')

        dfExtract = DataFrame(data=result, columns=columns)
        del result
        dfExtract['반복횟수'] = self.colCntLoops

        return columns, dfExtract

    # 실행시간 : 0.0001초
    def ReturnResult(self):
        # 범위 산출
        listRange = []
        cnt = 0
        while True:
            rates = round(float(self.ratePlus - self.rangeGap * cnt), 5)
            cnt += 1
            listRange.append(rates)
            if rates == -self.rateMinus:
                break
        listRange.reverse()

        # 범위별 수량 파악
        categoryRange = cut(self.priceRates, listRange)
        categoryCount = categoryRange.value_counts()
        del categoryRange
        dfCounts = categoryCount.to_frame()
        del categoryCount
        listRangeCount = dfCounts.iloc[:, 0].to_list()
        del dfCounts

        listRange = [f"{minus.__format__('.4f')} ~ {plus.__format__('.4f')}"
                     for (minus, plus) in zip(listRange[:-1], listRange[1:])]

        # 비율 산출
        countsRates = [float(round(value / self.cntLoop, 5)) for value in listRangeCount]

        # 누적 비율
        accumulateRate = 0
        accumulateRates = []
        for idx, rate in enumerate(countsRates):
            accumulateRate = round(accumulateRate + rate, 5)
            accumulateRates.append(accumulateRate.__format__('.5f'))
            countsRates[idx] = rate.__format__('.5f')
        del accumulateRate

        dfSource = []
        columns = ['차이범위', '산술평균가', '범위별수량', '비율', '비율(누적)']
        for values in zip(listRange,
                          self.priceExtracts,
                          listRangeCount,
                          countsRates,
                          accumulateRates):
            dfSource.append(list(values))
        dfResult = DataFrame(data=dfSource, columns=columns)
        del dfSource
        
        # 그래프 데이터 생성
        # 최댓값 산출
        copyRangeCount = listRangeCount[:]
        maxCounts = [max(copyRangeCount) if value == max(copyRangeCount) else 0 for value in copyRangeCount]
        maxIndex = copyRangeCount.index(max(copyRangeCount))
        copyRangeCount[maxIndex] = 0

        # 최댓값을 제외한 상위 5개 항목 산출
        subMaxValues = []
        subMaxIndexes = []
        for cnt in range(5):
            subMaxValue = max(copyRangeCount)
            subMaxIndex = copyRangeCount.index(subMaxValue)
            subMaxIndexes.append(subMaxIndex)
            copyRangeCount[subMaxIndex] = 0
            subMaxValues.append(subMaxValue)
        subMaxCounts = [value if value in subMaxValues else 0 for value in listRangeCount]
        Indexes = [maxIndex, subMaxIndexes]
        del maxIndex, subMaxIndexes, subMaxValues, copyRangeCount

        dfMaxSource = []
        dfSubMaxSource = []
        for rangeValue, maxValue, subMaxValue in zip(listRange,
                                                     maxCounts,
                                                     subMaxCounts):
            dfMaxSource.append([rangeValue, maxValue])
            dfSubMaxSource.append([rangeValue, subMaxValue])
        dfMaxCount = DataFrame(data=dfMaxSource, columns=columns[:3:2])
        dfSubMaxCount = DataFrame(data=dfSubMaxSource, columns=columns[:3:2])
        dfSubResults = [columns[:3:2], dfMaxCount, dfSubMaxCount]
        del dfMaxSource, dfSubMaxSource, dfMaxCount, dfSubMaxCount

        return columns, dfResult, Indexes, dfSubResults
