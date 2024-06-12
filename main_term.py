import requests
import json

def get_exchange_rates():
    """
    Fetch the current exchange rates of various cryptocurrencies.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "1h,24h,7d"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def display_exchange_rates(data):
    """
    Display the current exchange rates of the top 10 cryptocurrencies.
    """
    print("Top 10 Cryptocurrency Exchange Rates:")
    print("+--------------+---------------+-------------+-------------+-------------+")
    print("| Name         | Price (USD)   | 1h Change   | 24h Change  | 7d Change   |")
    print("+--------------+---------------+-------------+-------------+-------------+")
    for coin in data:
        name = coin["name"]
        price = f"{coin['current_price']:,.2f}"
        price_change_1h = f"{coin['price_change_percentage_1h_in_currency']:.2f}%"
        price_change_24h = f"{coin['price_change_percentage_24h_in_currency']:.2f}%"
        price_change_7d = f"{coin['price_change_percentage_7d_in_currency']:.2f}%"
        print(f"| {name:<12} | {price:>12} | {price_change_1h:>12} | {price_change_24h:>12} | {price_change_7d:>12} |")
    print("+--------------+---------------+-------------+-------------+-------------+")

def main():
    """
    Main function to fetch and display the current exchange rates.
    """
    data = get_exchange_rates()
    display_exchange_rates(data)

if __name__ == "__main__":
    main()
