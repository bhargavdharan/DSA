'''
store apples stock price for 5 days,
1.What was the price on day1?
2.what was the price on day3?

'''

import array as stockPrices

stockPrices = [298,305,320,301,292]

print("Element in first position:",stockPrices[0]) # price on day 1
print("Element in the last position:",stockPrices[2]) # price on day 3

print("The new created array is:",end = " ")
for i in range(0,5):
    print(stockPrices[i],end = " ")
print()

