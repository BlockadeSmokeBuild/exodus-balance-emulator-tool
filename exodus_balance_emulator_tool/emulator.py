import random
from decimal import Decimal, getcontext
from typing import Dict, List, Optional

from .wallet import Wallet

getcontext().prec = 8

class BalanceEmulator:
    """Emulates fake balances for Exodus wallet addresses."""

    def __init__(self, seed: Optional[int] = None):
        self._rng = random.Random(seed)
        self._wallets: Dict[str, Wallet] = {}

    def add_wallet(self, address: str, initial_balance: Decimal = Decimal("0")) -> None:
        """Add a wallet to the emulator."""
        if address in self._wallets:
            raise ValueError(f"Wallet {address} already exists")
        self._wallets[address] = Wallet(address, initial_balance)

    def generate_fake_balance(self, address: str, min_amount: Decimal, max_amount: Decimal) -> Decimal:
        """Generate a fake balance for a wallet."""
        if address not in self._wallets:
            raise ValueError(f"Wallet {address} not found")

        fake_balance = Decimal(self._rng.uniform(float(min_amount), float(max_amount)))
        self._wallets[address].update_balance(fake_balance)
        return fake_balance

    def get_wallet(self, address: str) -> Wallet:
        """Get a wallet by address."""
        return self._wallets.get(address)

    def list_wallets(self) -> List[Wallet]:
        """List all wallets."""
        return list(self._wallets.values())