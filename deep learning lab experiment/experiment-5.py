import numpy as np

usd_prices = np.array([10, 20, 30, 40, 50])

exchange_rate = 83.5
discount = 10 / 100

inr_prices = usd_prices * exchange_rate
discounted_prices = inr_prices * (1 - discount)

print("USD Prices:", usd_prices)
print("INR Prices:", inr_prices)
print("Discounted Prices:", discounted_prices)

expected_prices = 0.9 * 83.5 * usd_prices

print("Check:", np.allclose(discounted_prices, expected_prices))
