#include "algorithms.h"


int main(int argc, char const *argv[])
{
  srand(time(NULL));
  std::array<std::array<int, 2>, N> data_arr;
  int value = 0;
  std::ifstream data("input_150.txt");
  uint32_t pos = 0;
  if(!data.is_open())
    std::cout<<"File not open!!!!\n";
  while (data.is_open()) {
    data >> value;
    if (data) {
      data_arr[pos/2][pos%2] = value;
      pos++;
    } 
    else {
      break;
    }
  }
  data.close();


  for (int i = 0; i < 5; i++) {
    simulatedAnnealing(std::to_string(i), data_arr);
  }
  
  return 0;
}