#include "algorithms.h"

double getCycleLen(const std::array<std::array<int, 2>, N>& nodes, const std::vector<uint32_t>& cycle) {
  double sum = 0;
  uint32_t prevNode = cycle[0];
  for (const uint32_t& currNode: cycle) {
    sum += sqrt(pow(nodes[currNode][1] - nodes[prevNode][1], 2) + pow(nodes[currNode][0] - nodes[prevNode][0], 2));
    prevNode = currNode;
  }
  return sum + sqrt(pow(nodes[cycle[0]][1] - nodes[prevNode][1], 2) + pow(nodes[cycle[0]][0] - nodes[prevNode][0], 2));
}

void swapEdgesOpt2(uint32_t ab, uint32_t cd, std::vector<uint32_t>& cycle) {
  uint32_t tmp;
  if (cd < ab) {
    tmp = ab;
    ab = cd;
    cd = tmp;
  }

  for(uint32_t iter = 0; iter < static_cast<uint32_t>(ceil((static_cast<double>(cd) - ab) / 2)); iter++) {
    tmp = cycle[ab + iter];
    cycle[ab + iter] = cycle[cd - iter];
    cycle[cd - iter] = tmp;
  }
}

void saveToFile(const std::string& filename, const std::array<std::array<int, 2>, N>& nodes, const std::vector<uint32_t>& cycle, double cycleLen) {
  std::ofstream outFile(filename);
  if (!outFile.is_open()) {
    std::cerr << "File cannot be loaded.\n";
    exit(1);
  } else {
    outFile << "x " << cycleLen << std::endl;
    for (const uint32_t& node_id: cycle) {
      outFile << nodes[node_id][0] << " " << nodes[node_id][1] << std::endl;
    }
    outFile << nodes[cycle[0]][0] << " " << nodes[cycle[0]][1] << std::endl;
  }
  outFile.close();
}

std::vector<uint32_t> simulatedAnnealing(const std::string& filename, const std::array<std::array<int, 2>, N>& V) {
  std::vector<uint32_t> P(N);
  std::vector<uint32_t> newP(N);
  double PLen, newPLen, r, T = 0.;
  uint32_t ABEdge = 0, CDEdge = 0;

  std::iota(P.begin(), P.end(), 0);
  std::random_device rd;
  std::mt19937 g(rd());
  std::shuffle(P.begin(), P.end(), g);


  PLen = getCycleLen(V, P);
  saveToFile("before" + filename + ".dat", V, P, PLen);
  std::cout << "\n Initial cycle length  (" + filename + "): " << PLen << std::endl;
  
  
  for (uint32_t i = MIN_IT_T_LOWERING; i >= 1; i--) {
    T = T_MODIFIER * pow(static_cast<double>(i), 2);
    for (uint32_t it = 0; it < MAX_IT; it++) {
      ABEdge = 0, CDEdge = 0;
      while(abs((int)ABEdge - (int)CDEdge) <= 1 || (ABEdge == 0 && CDEdge == N - 1) || (ABEdge == N - 1 && CDEdge == 0)) {
        ABEdge = rand() % N;
        CDEdge = rand() % N;
      }

      newP = P;

      swapEdgesOpt2(ABEdge, CDEdge, newP);

      PLen = getCycleLen(V, P);
      newPLen = getCycleLen(V, newP);
      if (newPLen < PLen) {
        P = newP;
      } else {
        r = ((double) rand() / (RAND_MAX));
        if (r < exp((newPLen - PLen) / -T)) {
          P = newP;
        }
      }
    }
  }

  saveToFile("after" + filename + ".dat", V, P, PLen);
  std::cout << "\n Optimized cycle length (" + filename + "): " << getCycleLen(V, P) << std::endl;
  return P;
}