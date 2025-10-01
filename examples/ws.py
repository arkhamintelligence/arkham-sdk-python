#!/usr/bin/env python3
"""
Example usage of the Arkham Exchange WebSocket Client

This example demonstrates:
- Connecting to the WebSocket
- Subscribing to real-time trades
- Executing blocking commands
- Proper cleanup
"""

import time
from typing import Union

from arkham_sdk_python.models import (
    WebsocketTradesSnapshot,
    WebsocketTradesUpdate,
)
from arkham_sdk_python.ws_client import ArkhamWebSocket


def main():
    # Initialize WebSocket client with API credentials
    # Replace with your actual API key and secret
    ws = ArkhamWebSocket(
        # api_key=<YOUR_API_KEY>,
        # api_secret=<YOUR_API_SECRET>,
    )

    try:
        # Connect to WebSocket server
        print("Connecting to WebSocket...")
        ws.connect()
        print("Connected!")

        # Define a handler for trade data
        def handle_trade(data: Union[WebsocketTradesUpdate, WebsocketTradesSnapshot]):
            if data["type"] == "snapshot":
                for trade in data["data"]:
                    print(f"Trade snapshot received: {trade}")
            else:
                print(f"Trade update received: {data['data']}")

        def handle_ticker(data):
            print(f"Ticker update: {data}")

        # Subscribe to trades for BTC_USDT (non-blocking)
        print("Subscribing to BTC_USDT trades...")
        unsubscribe_trades = ws.subscribe_trades({"symbol": "BTC_USDT", "snapshot": True}, handle_trade)

        # Subscribe to ticker updates
        print("Subscribing to BTC_USDT ticker...")
        unsubscribe_ticker = ws.subscribe_ticker({"symbol": "BTC_USDT", "snapshot": True}, handle_ticker)

        # Let it run for a bit to see some data
        print("Listening for real-time data... (will run for 5 seconds)")
        time.sleep(5)

        try:
            print("Executing cancel all orders command...")
            result = ws.cancel_all(
                {
                    "symbol": "ZRO_USDT",
                }
            )
            print(f"✅ Command result: {result}")
        except Exception as e:
            print(f"❌ Command failed: {e}")

        # Show connection health
        latency = ws.get_latency()
        if latency:
            print(f"🏓 Average latency: {latency:.2f}ms")

        # Unsubscribe from channels
        print("Unsubscribing from channels...")
        unsubscribe_trades()
        unsubscribe_ticker()

        print("Example completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        # Always close the connection
        print("Closing WebSocket connection...")
        ws.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
