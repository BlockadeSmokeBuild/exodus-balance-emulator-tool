import unittest
from decimal import Decimal

from exodus_balance_emulator_tool.emulator import BalanceEmulator

class TestBalanceEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = BalanceEmulator(seed=42)
        self.test_address = "0x123abc"

    def test_add_wallet(self):
        self.emulator.add_wallet(self.test_address)
        self.assertIn(self.test_address, self.emulator._wallets)

    def test_generate_fake_balance(self):
        self.emulator.add_wallet(self.test_address)
        balance = self.emulator.generate_fake_balance(
            self.test_address,
            Decimal("0.1"),
            Decimal("10.0")
        )
        self.assertTrue(Decimal("0.1") <= balance <= Decimal("10.0"))

    def test_get_wallet(self):
        self.emulator.add_wallet(self.test_address)
        wallet = self.emulator.get_wallet(self.test_address)
        self.assertEqual(wallet.address, self.test_address)

if __name__ == "__main__":
    unittest.main()