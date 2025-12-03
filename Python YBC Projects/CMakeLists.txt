cmake_minimum_required(VERSION 4.0)
project(Python_YBC_Projects)

set(CMAKE_CXX_STANDARD 14)

include_directories("CSP-S C++")

add_executable(Python_YBC_Projects
        "CSP-S C++/test.cpp")
add_executable(Python_YBC_Projects "question2.ccp")

