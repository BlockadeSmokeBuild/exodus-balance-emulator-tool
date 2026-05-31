#include <iostream>
#include "emulator.h"
#include "config.h"

int main() {
    std::cout << "Exodus Fake Balance Emulator Tool\n";
    std::cout << "Loading configuration...\n";

    Config config = loadConfig("config.json");
    Emulator emulator(config);

    std::cout << "Emulator started with balance: " << emulator.getBalance() << "\n";
    std::cout << "Press Enter to exit...\n";
    std::cin.get();

    return 0;
}