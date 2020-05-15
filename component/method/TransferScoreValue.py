def TransferPrice(price):
    try:
        price = price.replace(',', '')
        price = int(price)
        return price
    except:
        return 0


def TransferPoint(point):
    try:
        point = float(point)
        return point
    except:
        return 0
