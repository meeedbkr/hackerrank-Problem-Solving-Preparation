def birthdayCakeCandles(candles):
    # Get the maximum height of the candles
    m = max(candles)
    # Return the number of candles with the maximum height
    return candles.count(m)
