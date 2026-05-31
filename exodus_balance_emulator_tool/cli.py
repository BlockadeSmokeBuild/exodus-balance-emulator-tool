import argparse
from decimal import Decimal

from .emulator import BalanceEmulator

def main():
    parser = argparse.ArgumentParser(description="Exodus Fake Balance Emulator Tool")
    parser.add_argument("--address", type=str, required=True, help="Wallet address to emulate")
    parser.add_argument("--min", type=float, default=0.01, help="Minimum fake balance amount")
    parser.add_argument("--max", type=float, default=100.0, help="Maximum fake balance amount")
    parser.add_argument("--seed", type=int, help="Random seed for reproducibility")

    args = parser.parse_args()

    emulator = BalanceEmulator(seed=args.seed)
    emulator.add_wallet(args.address)

    fake_balance = emulator.generate_fake_balance(
        args.address,
        Decimal(str(args.min)),
        Decimal(str(args.max))
    )

    print(f"Generated fake balance for {args.address}: {fake_balance}")

if __name__ == "__main__":
    main()