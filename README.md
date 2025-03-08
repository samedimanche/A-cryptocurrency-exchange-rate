# Cryptocurrency Exchange Rate Parser

This project consists of two Python scripts (`main_bot.py` and `main_term.py`) that fetch and display cryptocurrency exchange rates using the **CoinGecko API**. These scripts provide real-time data on cryptocurrency prices and their percentage changes over different time periods, making them useful tools for tracking market trends. This project was developed **for educational purposes only** and is not intended for commercial use.

---

## Overview

### `main_bot.py`
This script fetches and displays the current exchange rates for a predefined list of cryptocurrencies (Bitcoin, Ethereum, Litecoin, and Ripple) in USD. It is a simple and lightweight tool for quickly checking cryptocurrency prices.

### `main_term.py`
This script fetches and displays the top 10 cryptocurrencies by market capitalization, including their current prices and percentage changes over the last hour, 24 hours, and 7 days. It provides a more detailed and formatted output, making it ideal for users who want a comprehensive overview of the cryptocurrency market.

---

## Features

### `main_bot.py`
- Fetches real-time prices for Bitcoin, Ethereum, Litecoin, and Ripple.
- Displays prices in USD.
- Simple and straightforward output.

### `main_term.py`
- Fetches the top 10 cryptocurrencies by market capitalization.
- Displays current prices and percentage changes over 1 hour, 24 hours, and 7 days.
- Formatted table output for easy readability.

---

## How It Works

### `main_bot.py`
1. **API Request**: Sends a GET request to the CoinGecko API endpoint (`https://api.coingecko.com/api/v3/simple/price`) with the specified parameters.
2. **Parameter Configuration**:
   - `ids`: A comma-separated list of cryptocurrency symbols (e.g., `bitcoin,ethereum,litecoin,ripple`).
   - `vs_currencies`: The currency in which prices are displayed (e.g., `usd`).
3. **Response Handling**:
   - If the request is successful (status code 200), the program parses the JSON response and extracts the prices.
   - If the request fails, an error message is displayed.
4. **Output**: Prints the cryptocurrency symbols and their corresponding prices in USD.

### `main_term.py`
1. **API Request**: Sends a GET request to the CoinGecko API endpoint (`https://api.coingecko.com/api/v3/coins/markets`) with the specified parameters.
2. **Parameter Configuration**:
   - `vs_currency`: The currency in which prices are displayed (e.g., `usd`).
   - `order`: Orders cryptocurrencies by market capitalization in descending order.
   - `per_page`: Limits the results to the top 10 cryptocurrencies.
   - `price_change_percentage`: Fetches percentage changes over 1 hour, 24 hours, and 7 days.
3. **Response Handling**:
   - If the request is successful, the program parses the JSON response and extracts the required data.
4. **Output**: Displays a formatted table with the cryptocurrency name, current price, and percentage changes.

---

## Technologies Used

- **Python**: The core programming language used to build the scripts.
- **CoinGecko API**: Provides real-time cryptocurrency exchange rate data.
- **Requests Library**: Used to send HTTP requests to the CoinGecko API.
- **JSON**: Used to parse the API response data.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/A-cryptocurrency-exchange-rate.git
   cd A-cryptocurrency-exchange-rate
   ```

2. **Install Dependencies**:
   - Install the `requests` library if not already installed:
     ```bash
     pip install requests
     ```

3. **Run the Scripts**:
   - To run `main_bot.py`:
     ```bash
     python main_bot.py
     ```
   - To run `main_term.py`:
     ```bash
     python main_term.py
     ```

---

## Example Output

### `main_bot.py`
```
Cryptocurrency Exchange Rates:
BITCOIN: $29,500.00
ETHEREUM: $1,800.00
LITECOIN: $90.00
RIPPLE: $0.50
```

### `main_term.py`
```
Top 10 Cryptocurrency Exchange Rates:
+--------------+---------------+-------------+-------------+-------------+
| Name         | Price (USD)   | 1h Change   | 24h Change  | 7d Change   |
+--------------+---------------+-------------+-------------+-------------+
| Bitcoin      |     29,500.00 |       -0.50% |       -1.20% |       -2.50% |
| Ethereum     |      1,800.00 |       -0.30% |       -0.80% |       -1.50% |
| Binance Coin |        300.00 |       -0.20% |       -0.60% |       -1.00% |
| Cardano      |          1.20 |       -0.10% |       -0.40% |       -0.80% |
| Dogecoin     |          0.10 |       -0.05% |       -0.20% |       -0.50% |
| XRP          |          0.50 |       -0.15% |       -0.30% |       -0.70% |
| Polkadot     |         15.00 |       -0.25% |       -0.50% |       -1.20% |
| Litecoin     |         90.00 |       -0.10% |       -0.40% |       -0.90% |
| Chainlink    |         20.00 |       -0.30% |       -0.70% |       -1.50% |
| Stellar      |          0.30 |       -0.05% |       -0.10% |       -0.40% |
+--------------+---------------+-------------+-------------+-------------+
```

---

## Disclaimer

This project was developed **for educational purposes only**. It is not intended for commercial use, and no part of this project is monetized. The data and images used in this project are sourced from publicly available APIs and the Internet, and they are used solely for learning and demonstration purposes.

---

## Contribution

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Thank you for your interest in this project! For more details, feel free to explore the repository and reach out with any questions.
