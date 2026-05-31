cmake_minimum_required(VERSION 3.10)
project(exodus-balance-emulator-tool)

set(CMAKE_CXX_STANDARD 17)

add_executable(exodus-emulator
    src/main.cpp
    src/emulator.cpp
    src/config.cpp
)

target_include_directories(exodus-emulator PRIVATE src)
target_link_libraries(exodus-emulator PRIVATE nlohmann_json)