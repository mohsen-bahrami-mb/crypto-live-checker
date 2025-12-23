"""Crypto price checker module using Binance WebSocket API with symbol validation."""

import json
import sys
import websocket
import requests
from typing import Optional


class CryptoPriceChecker:
    """Real-time cryptocurrency price checker using Binance WebSocket with validation."""

    BASE_WS_URL = "wss://stream.binance.com:9443/ws/"
    EXCHANGE_INFO_URL = "https://api.binance.com/api/v3/exchangeInfo"

    def __init__(self, asset_id: str):
        """
        Initialize the price checker.

        Args:
            asset_id: The trading pair symbol (e.g., 'btcusdt', 'ethusdt')
        """
        self.asset_id = asset_id.lower()
        self.ws_url = f"{self.BASE_WS_URL}{self.asset_id}@trade"
        self.ws: Optional[websocket.WebSocketApp] = None
        self.last_price: Optional[str] = None

    def validate_symbol(self) -> bool:
        """Check if the symbol is valid on Binance."""
        try:
            response = requests.get(self.EXCHANGE_INFO_URL, timeout=1)
            data = response.json()
            symbols = [item['symbol'].lower() for item in data['symbols']]
            if self.asset_id in symbols:
                return True
            else:
                self._print_error(
                    f"Symbol '{self.asset_id}' is not valid. "
                    "Please check the trading pair on Binance."
                )
                return False
        except Exception as e:
            self._print_error(f"Failed to validate symbol: {e}")
            return False

    def _on_message(self, ws: websocket.WebSocketApp, message: str) -> None:
        """Handle incoming WebSocket messages."""
        try:
            data = json.loads(message)
            price = data.get("p")  # 'p' is the price field in Binance
            if price:
                self.last_price = price
                self._update_display(price)
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            self._print_error(f"Error parsing message: {e}")

    def _on_error(self, ws: websocket.WebSocketApp, error: Exception) -> None:
        """Handle WebSocket errors."""
        self._print_error(f"WebSocket error: {error}")

    def _on_close(self, ws: websocket.WebSocketApp, close_status_code: int, close_msg: str) -> None:
        """Handle WebSocket connection close."""
        print("\nConnection closed.")

    def _on_open(self, ws: websocket.WebSocketApp) -> None:
        """Handle WebSocket connection open."""
        print(f"\nConnected to Binance WebSocket for {self.asset_id.upper()}")
        print("Press Ctrl+C to stop\n")

    def _update_display(self, price: str) -> None:
        """Update the price display in-place."""
        price_str = f"\rPrice: ${price} | Asset: {self.asset_id.upper()}"
        print(price_str, end="", flush=True)

    def _print_error(self, message: str) -> None:
        """Print error message on a new line."""
        print(f"\n{message}")

    def start(self) -> None:
        """Start the WebSocket connection and begin receiving price updates."""
        if not self.validate_symbol():
            return  # Stop if symbol is invalid

        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        try:
            self.ws.run_forever()
        except KeyboardInterrupt:
            print("\n\nStopped. Goodbye!")


def main():
    """Main entry point for the crypto price checker."""
    if len(sys.argv) > 1:
        asset_id = sys.argv[1]
    else:
        asset_id = input(
            "Enter trading pair symbol (e.g., btcusdt, ethusdt): ").strip()

    if not asset_id:
        print("Error: Symbol cannot be empty.")
        sys.exit(1)

    checker = CryptoPriceChecker(asset_id)
    checker.start()


if __name__ == "__main__":
    main()
