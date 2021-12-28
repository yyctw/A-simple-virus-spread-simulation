#pragma once

#include "SimulationState.hpp"

void ShowStatus(SimulationState &status, size_t mode);
void UpdateDirection(struct PersonStatus &p_stat, struct myBoundary &my_bound);
void Move(SimulationState &status);
void RecoveredOrDead(SimulationState &status);
void SpreadVirus(SimulationState &status);
void Run(SimulationState &status);
void ClassifyPeople(SimulationState &status);
void RunStep(SimulationState &status);

