# Telegram Crypto Trading Bot

## Overview

This Telegram bot serves as a powerful tool for cryptocurrency trading, providing users with real-time price alerts and technical analysis features. Built using the Aiogram framework, the bot allows users to connect to various cryptocurrency exchanges and monitor specific trading pairs.

## Features

- **Real-time Price Alerts**: Get instant notifications about price movements for selected cryptocurrency pairs.
- **Simple Moving Average (SMA) Calculation**: Automatically calculates the SMA for a specified period and trading pair.
- **Historical Data Processing**: The bot can process historical candle data to provide insights into past price movements.
- **WebSocket Connection**: Maintains a live connection to cryptocurrency exchanges to fetch real-time data without the need for constant polling.
- **Customizable Settings**: Users can easily configure the bot with different exchanges, trading pairs, periods, and intervals.
- **Asynchronous Operations**: Utilizes asynchronous programming for efficient handling of multiple connections and events.
- **Database Storage for Trades**: All executed trades and related data (e.g., entry price, stop loss, take profit) will be securely stored in a database for future reference and analysis.

## Planned Features

- **Additional Indicators**: Support for a wider range of technical indicators, such as EMA, RSI, MACD, and others.
- **Custom Trading Strategies**: Users will be able to define and deploy their own trading strategies directly through the bot.
- **Automated Trading**: Implementing automated order placement, including Stop Loss and Take Profit, with real-time tracking and management.
- **Strategy Backtesting**: Users will have the ability to backtest their custom strategies against historical data to evaluate performance.
- **Comprehensive Trade Data Management**: Expansion of the database to store detailed trade data, including timestamps, profit/loss calculations, and strategy performance metrics.

## Installation

1. Clone the repository:

   ```bash
    git clone git@github.com:0x746865736861726b79736861726b/whisper.git
   ```
2. Navigate to the project directory:

    ```bash
    cd <project-repo>
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure your Telegram bot token and exchange settings in the `config/settings.py` file.

## Usage

1. Start the bot by running:
    ```bash
    python main.py
    ```
2. Open your Telegram app and search for your bot.

3. Use the `/start` command to begin interacting with the bot.
4. Use the `/sma <exchange_name> <symbol> <period> <interval>` command to get the `SMA` for a specific trading pair.

## Example

To get the SMA for the trading pair LTCUSDT on Binance with a period of 5 and an interval of 1 minute, you would send the following command in your Telegram chat with the bot:

```
/sma binance LTCUSDT 5 1m
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.