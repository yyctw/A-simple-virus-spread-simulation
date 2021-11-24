#include <iostream>
#include <stdexcept>

#include "../include/Parameter.hpp"

int main() {
  SimulationParameter default_data(1000, 1, 1, 0.7, 0.3, 5, 100);
  default_data.PrintStatus();
  return 0;
}
