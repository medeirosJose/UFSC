#ifndef XORCYPHER_H_
#define XORCYPHER_H_

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include "HexToB64.h"
int resolveC3();

double scoreHEX(const std::string &text);
std::string XORWithKey(const std::vector<char> &input, char key);
void XORdecypher(const std::string &HEX);

#endif