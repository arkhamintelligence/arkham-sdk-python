#!/usr/bin/env python3
"""
Example usage of the Arkham Exchange WebSocket Client

This example demonstrates:
- Getting a list of all pairs
- Fetching order book data for a specific pair
- Placing and cancelling orders
"""
from arkham_sdk_python.client import Arkham
from arkham_sdk_python.models import OrderSide, OrderType


def main():
    # Initialize WebSocket client with API credentials
    # Replace with your actual API key and secret
    client = Arkham(
        # api_key=<YOUR_API_KEY>,
        # api_secret=<YOUR_API_SECRET>,
    )

    # Get a list of all trading pairs
    print("Fetching all trading pairs...")
    pairs = client.get_pairs()
    print(f"✅ Trading pairs: {pairs}")

    # Fetch order book data for a specific pair
    print("Fetching order book for BTC_USDT...")
    order_book = client.get_book("BTC_USDT")
    print(f"✅ Order book: {order_book}")

    # Place a new order
    print("Placing a new order...")
    order = client.create_order(
        {
            "symbol": "BTC_USDT",
            "side": OrderSide.Buy,
            "type": OrderType.LimitGtc,
            "size": "0.0001",
            "price": "30000",
        }
    )
    print(f"✅ Order placed: {order}")

    # Cancel the order
    print("Cancelling the order...")
    result = client.cancel_order(
        {
            "orderId": order["orderId"],
        }
    )
    print(f"✅ Order cancelled: {result}")


if __name__ == "__main__":
    main()
