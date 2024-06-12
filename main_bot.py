import requests


def get_crypto_prices():
    # List of cryptocurrency symbols to fetch prices for
    crypto_symbols = ["bitcoin", "ethereum", "litecoin", "ripple"]

    # API endpoint URL
    api_url = "https://api.coingecko.com/api/v3/simple/price"

    # Fetch data from the API
    params = {
        "ids": ",".join(crypto_symbols),
        "vs_currencies": "usd"
    }
    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Print the prices
        print("Cryptocurrency Exchange Rates:")
        for symbol in crypto_symbols:
            price = data[symbol]["usd"]
            print(f"{symbol.upper()}: ${price:.2f}")
    else:
        print("Failed to fetch cryptocurrency prices.")


# Call the function to get and display the prices
get_crypto_prices()
