# A-cryptocurrency-exchange-rate

A Python program that can fetch cryptocurrency exchange rates from the CoinGecko API and display them to the user<br/>

Here's how the program works:
<br/>
The get_crypto_prices() function is defined, which will fetch and display the cryptocurrency prices.<br/>
A list of cryptocurrency symbols crypto_symbols is created, containing the symbols of the cryptocurrencies for which we want to fetch prices.<br/>
The API endpoint URL api_url is defined as "https://api.coingecko.com/api/v3/simple/price".<br/>
The params dictionary is created, which contains the required parameters for the API request. The ids parameter is a comma-separated string of the cryptocurrency symbols, and vs_currencies specifies the currency in which we want the prices (USD in this case).<br/>
The requests.get() function is used to send a GET request to the API endpoint with the specified parameters.<br/>
The program checks if the request was successful (status code 200) using an if statement.<br/>
If the request was successful, the response data is parsed as JSON using response.json().<br/>
The program iterates over the crypto_symbols list and prints the symbol and corresponding price for each cryptocurrency.<br/>
If the request failed, an error message is printed.<br/>
Finally, the get_crypto_prices() function is called to fetch and display the cryptocurrency prices.<br/>
Note that this program uses the requests library to make HTTP requests to the CoinGecko API. You'll need to install the requests library if you haven't already done so. You can install it using pip:<br/>

```
pip install requests
```
<br/>
When you run the program, it will display the current exchange rates for the specified cryptocurrencies (Bitcoin, Ethereum, Litecoin, and Ripple) in USD.
