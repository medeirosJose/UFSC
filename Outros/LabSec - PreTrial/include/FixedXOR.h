#ifndef FIXEDXOR_H_
#define FIXEDXOR_H_

#include <iostream>
#include <string>
#include <vector>
#include "HexToB64.h"

int resolveC2();
std::string BytesToHex(const std::vector<char> &bytes);
std::vector<char> FixedXOR(std::vector<char> &bytes1, std::vector<char> &bytes2);

#endif