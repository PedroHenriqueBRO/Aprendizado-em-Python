prices={
    'ACME':150.56,
    'AAPL':170.45,
    'IBM':430
}
min_price=min(zip(prices.values(),prices.keys()))
print(min_price)
max_price=max(zip(prices.values(),prices.keys()))
print(max_price)
print(min(prices,key=lambda k:prices[k]))