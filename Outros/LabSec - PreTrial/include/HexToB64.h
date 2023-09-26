#ifndef HEXTOB64_H_
#define HEXTOB64_H_

#include <iostream> // std::cout
#include <string>   // std::string
#include <vector>   // std::vector

int resolveC1();
std::string BytesToBase64(const std::vector<char> &bytes);
std::vector<char> HexToBytes(const std::string &hex);

#endif