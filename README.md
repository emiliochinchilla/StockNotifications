Stock Alert & News Notification System

This Python project is designed to monitor stock price changes for Tesla Inc. (or any other stock) and send notifications via WhatsApp using Twilio's API. If the stock price fluctuates by more than 5% compared to the previous day's close, it retrieves the top 3 news articles related to Tesla Inc. from the NewsAPI and sends a WhatsApp message summarizing the stock change and related news.
Features

    Monitors daily stock price fluctuations using Alpha Vantage API.
    Fetches news articles related to the stock using NewsAPI.
    Sends a WhatsApp message through Twilio if the stock price changes by more than 5%.
    Configurable to monitor other stocks and companies by changing environment variables.

Technologies Used

    Python: Core programming language.
    Twilio API: Sends WhatsApp messages.
    Alpha Vantage API: Provides stock price data.
    NewsAPI: Fetches news articles related to the stock.
    dotenv: Loads environment variables from a .env file.
    requests: Makes API requests.

Prerequisites

To run this project, you need:

    Python 3.x installed on your system.
    A Twilio account for sending WhatsApp messages.
    An Alpha Vantage API key for retrieving stock data.
    A NewsAPI key for fetching news articles.
    A .env file to securely store API keys and other credentials.

Environment Variables

Create a .env file in the root of the project and add the following environment variables:

plaintext

STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_newsapi_key
account_sid=your_twilio_account_sid
auth_token=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_whatsapp_number
RECIPIENT=recipient_whatsapp_number

Installation

    Clone the repository to your local machine:

bash

git clone https://github.com/yourusername/stock-alert-news-notification.git
cd stock-alert-news-notification

    Install the required Python packages:

bash

pip install requests python-dotenv twilio

    Create a .env file to store your API keys and Twilio credentials as described above.

How It Works

    Stock Price Monitoring: The script retrieves the stock price for Tesla Inc. from the Alpha Vantage API for the last two trading days.

    Percentage Change Calculation: It calculates the percentage change in the stock price between the last two days.

    Threshold Check: If the stock price changes by more than 5% (either increase or decrease), the system triggers a news search.

    News Fetching: The script uses the NewsAPI to search for Tesla-related news articles published on the most recent trading day.

    WhatsApp Message: A WhatsApp message is sent using the Twilio API, containing a brief summary of the top 3 news articles and the percentage change in stock price.

Usage

Run the script with:

bash

python stock_alert.py

Make sure your Twilio account is set up properly to send WhatsApp messages. The messages will be sent to the recipient's WhatsApp number configured in the .env file.
Example Output

WhatsApp message sent:

vbnet

TSLA up by 5%
Headline: Tesla releases new Model X. 
Brief: Tesla has announced the release of the updated Model X, featuring an improved battery.

Notes

    The script is set up to monitor Tesla Inc. by default, but you can change the STOCK and COMPANY_NAME variables to monitor other stocks.
    Be sure to check your Twilio account limits, as message sending can incur costs if limits are exceeded.
