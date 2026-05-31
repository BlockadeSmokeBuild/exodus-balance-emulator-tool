#include <gtest/gtest.h>
#include "../src/emulator.h"
#include "../src/config.h"

TEST(EmulatorTest, InitialBalanceInRange) {
    Config config{100.0, 10000.0, "USD"};
    Emulator emulator(config);

    double balance = emulator.getBalance();
    EXPECT_GE(balance, config.minBalance);
    EXPECT_LE(balance, config.maxBalance);
}

TEST(EmulatorTest, UpdateBalance) {
    Config config{0.0, 0.0, "USD"};
    Emulator emulator(config);

    emulator.updateBalance(50.0);
    EXPECT_DOUBLE_EQ(emulator.getBalance(), 50.0);
}