#include "config.h"
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

Config loadConfig(const std::string& filename) {
    std::ifstream file(filename);
    json data = json::parse(file);

    Config config;
    config.minBalance = data["minBalance"];
    config.maxBalance = data["maxBalance"];
    config.currency = data["currency"];

    return config;
}