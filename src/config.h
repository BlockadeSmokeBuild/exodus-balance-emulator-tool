#pragma once
#include <string>

struct Config {
    double minBalance;
    double maxBalance;
    std::string currency;
};

Config loadConfig(const std::string& filename);