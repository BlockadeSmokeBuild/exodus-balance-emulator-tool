#include "emulator.h"
#include <random>

Emulator::Emulator(const Config& config) : config(config) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(config.minBalance, config.maxBalance);
    balance = dis(gen);
}

double Emulator::getBalance() const {
    return balance;
}

void Emulator::updateBalance(double amount) {
    balance += amount;
}