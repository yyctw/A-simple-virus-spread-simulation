#pragma once
#include "Parameter.hpp"

void ShowStatus(SimulationParameter &status, size_t mode);
void UpdateDirection(struct PersonStatus &p_stat, struct myBoundary &my_bound);
void Move(SimulationParameter &status);
void RecoveredOrDead(SimulationParameter &status);
void SpreadVirus(SimulationParameter &status);
void Run(SimulationParameter &status);
void InitSimulation(SimulationParameter &status);
void ClassifyPeople(SimulationParameter &status);
void RunStep(SimulationParameter &status);
