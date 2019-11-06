cmake_minimum_required(VERSION 2.8)
project(a2-ece650)

## ECE650 Specific configuration start here
## Project specific configurations go here

# enable c++11 support
#set (CMAKE_CXX_FLAGS "-std=c++11 -Wall ${CMAKE_CXX_FLAGS}")

# create the main executable
## add additional .cpp files if needed
add_executable(a2-ece650 a2-ece650.cpp )

# create the executable for tests
#add_executable(tests test.cpp)
