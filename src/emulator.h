#pragma once
#include "config.h"
#include <string>

class Emulator {
public:
    Emulator(const Config& config);
    double getBalance() const;
    void updateBalance(double amount);

private:
    double balance;
    Config config;
};