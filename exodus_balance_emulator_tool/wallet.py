from decimal import Decimal

class Wallet:
    """Represents a wallet with address and balance."""

    def __init__(self, address: str, balance: Decimal = Decimal("0")):
        self.address = address
        self.balance = balance

    def update_balance(self, new_balance: Decimal) -> None:
        """Update the wallet balance."""
        self.balance = new_balance

    def __repr__(self) -> str:
        return f"Wallet(address='{self.address}', balance={self.balance})"