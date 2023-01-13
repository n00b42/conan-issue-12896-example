cmake_minimum_required(VERSION 3.20)

project(MyProject)

add_executable(myexample main.cpp)

install(TARGETS myexample RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
