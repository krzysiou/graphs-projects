#pragma once

#include <iostream>
#include <fstream>
#include <array>
#include <numeric>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <random>

#define N 150
#define MAX_IT 1000
#define MIN_IT_T_LOWERING 200
#define T_MODIFIER 0.001

double getCycleLen(const std::array<std::array<int, 2>, N>&, const std::vector<uint32_t>&);

void swapEdgesOpt2(uint32_t, uint32_t, std::vector<uint32_t>&);

void saveToFile(const std::string&, const std::array<std::array<int, 2>, N>&, const std::vector<uint32_t>&, double);

std::vector<uint32_t> simulatedAnnealing(const std::string&, const std::array<std::array<int, 2>, N>&);