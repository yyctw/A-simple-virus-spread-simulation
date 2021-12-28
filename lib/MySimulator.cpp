#include <ctime>
#include <iostream>
#include <random>
#include <stdexcept>
#include <vector>

#include "MySimulator.hpp"
#include "SimulationState.hpp"

size_t SIMU_BOUND_SIZE = 4; // 4km^2 range

void ShowStatus(SimulationState &status, size_t mode) {
  if (mode == 1) {
    for (size_t i = 0; i < status.m_total_num_people; ++i) {
      std::cout << "===== Person info =====" << std::endl;
      std::cout << "Person " << status.g_person_status[i].m_index << ": ("
                << status.g_person_status[i].m_coordinate.first << ", "
                << status.g_person_status[i].m_coordinate.second << ")"
                << std::endl;
      std::cout << "move direction vector: ("
                << status.g_person_status[i].m_direction_vector.first << ", "
                << status.g_person_status[i].m_direction_vector.second << ")"
                << std::endl;
      std::cout << "move speed: " << status.g_person_status[i].m_move_speed
                << std::endl;
      std::cout << "status: " << status.g_person_status[i].m_status
                << std::endl;
    }
  }
  std::cout << "===== Global info =====" << std::endl;
  std::cout << "Total people: " << status.m_total_num_people << std::endl;
  std::cout << "Health people: " << status.g_num_health << std::endl;
  std::cout << "Infected people: " << status.g_num_infected << std::endl;
  std::cout << "Dead people: " << status.g_num_dead << std::endl;
  std::cout << "Recovered people: " << status.g_num_recovered << std::endl;
}

// after moving, check the boundary and update the moving direction if needed.
void UpdateDirection(struct PersonStatus &p_stat, struct myBoundary &my_bound) {
  // x coordinate out of bound (x < left_x)
  if (p_stat.m_coordinate.first < p_stat.lx) {
    p_stat.m_coordinate.first = 2 * p_stat.lx - p_stat.m_coordinate.first;
    p_stat.m_direction_vector.first = -1 * p_stat.m_direction_vector.first;
  }
  // x > right_x
  else if (p_stat.m_coordinate.first > p_stat.rx) {
    p_stat.m_coordinate.first = 2 * p_stat.rx - p_stat.m_coordinate.first;
    p_stat.m_direction_vector.first = -1 * p_stat.m_direction_vector.first;
  }
  // y coordinate out of bound (y < down_y)
  if (p_stat.m_coordinate.second < my_bound.down_y) {
    p_stat.m_coordinate.second = 2 * my_bound.down_y - p_stat.m_coordinate.second;
    p_stat.m_direction_vector.second = -1 * p_stat.m_direction_vector.second;
  }
  // y > up_y
  else if (p_stat.m_coordinate.second > my_bound.up_y) {
    p_stat.m_coordinate.second = 2 * my_bound.up_y - p_stat.m_coordinate.second;
    p_stat.m_direction_vector.second = -1 * p_stat.m_direction_vector.second;
  }
}


// update the location and move direction of everyone after moving once.
void Move(SimulationState &status) {
  // reset dirty_bit bit
  status.dirty_bit = 0;
  for (size_t i = 0; i < status.m_total_num_people; ++i) {
    // if dead, don't move
    if (status.g_person_status[i].m_status == 3) {
      continue;
    }
    // move 1 m per step, boundary = 2km : 2, step = 1m : 0.001
    status.g_person_status[i].m_coordinate.first +=
        status.g_person_status[i].m_direction_vector.first *
        status.g_person_status[i].m_move_speed;
    status.g_person_status[i].m_coordinate.second +=
        status.g_person_status[i].m_direction_vector.second *
        status.g_person_status[i].m_move_speed;
    if (status.g_person_status[i].m_quar == 1) {
      if(status.g_person_status[i].m_coordinate.first < 0.5) {
        status.g_person_status[i].lx = status.g_boundary.left_x;
        status.g_person_status[i].rx = 0.5;
        status.g_person_status[i].m_move_speed /= 2;
        status.g_person_status[i].m_quar = 2;
        std::default_random_engine generator(time(NULL));
        int direct_angle = generator() % 360;
        status.g_person_status[i].m_direction_vector.first =
            cos(direct_angle * M_PI / 180) *
            status.m_move_step; // the move vector of x component
        status.g_person_status[i].m_direction_vector.second =
            sin(direct_angle * M_PI / 180) *
            status.m_move_step; // the move vector of y component

      }
    } else if (status.g_person_status[i].m_quar == 3) {
      if(status.g_person_status[i].m_coordinate.first >= 0.5) {
        status.g_person_status[i].lx = 0.5;
      }
    }
    UpdateDirection(status.g_person_status[i], status.g_boundary);
  }
}

// After a day(move 24 times), check whether infected_person's status needs to
// be changed.
void RecoveredOrDead(SimulationState &status) {
  std::default_random_engine generator(time(NULL));
  std::uniform_real_distribution<float> unif(0, 1);
  // Update recovered or dead.
  for (auto& i: status.g_infected_people) {
    float recovered_prob = unif(generator);
    float dead_prob = unif(generator);
    // recovered
    if (recovered_prob <= i.second.m_recovery_rate) {
      status.g_person_status[i.second.m_index].m_status = 2;
      i.second.m_status = 2;
      --status.g_num_infected;
      ++status.g_num_recovered;
      status.dirty_bit = 1;
      if (i.second.m_quar == 2 || i.second.m_quar == 1) {
        status.g_person_status[i.second.m_index].m_quar = 3;
        status.g_person_status[i.second.m_index].rx = status.g_boundary.right_x;
        status.g_person_status[i.second.m_index].m_direction_vector.first =
                    cos(0 * M_PI / 180) *
                    status.m_move_step; // the move vector of x component
      }
    }
    // dead
    else if (dead_prob <= i.second.m_mortality_rate) {
      status.g_person_status[i.second.m_index].m_status = 3;
      i.second.m_status = 3;
      --status.g_num_infected;
      ++status.g_num_dead;
      status.dirty_bit = 1;
    }
  }
  // update infected_person
  for (auto iter = status.g_infected_people.begin();
       iter != status.g_infected_people.end();) {
    if (iter->second.m_status != 1) {
      iter = status.g_infected_people.erase(iter);
    } else {
      ++iter;
    }
  }
}

// check all infected person and spread the virus.
void SpreadVirus(SimulationState &status) {
  // Update infected people
  std::default_random_engine generator(time(NULL));
  std::uniform_real_distribution<float> unif(0, 1);
  for (auto& i: status.g_infected_people) {
    for (size_t j = 0; j < status.m_total_num_people; ++j) {
      if (status.g_person_status[j].m_status == 0) {
        float dist = sqrt(pow(i.second.m_coordinate.first -
                                  status.g_person_status[j].m_coordinate.first,
                              2) +
                          pow(i.second.m_coordinate.second -
                                  status.g_person_status[j].m_coordinate.second,
                              2));
        if (dist <= status.m_spread_range) {
          float infected_prob = unif(generator);
          // been infected, set status = 1 and push it to infected_person.
          if (infected_prob <= status.m_infect_rate) {
            status.g_person_status[j].m_status = 1;
            --status.g_num_health;
            ++status.g_num_infected;
            status.dirty_bit = 1;
            // if policy = 2, 100% prob go to quarantine
            if (status.m_policy == 2) {
              float quar_prob = unif(generator);
              if (quar_prob <= status.m_accept_isolation_rate) {
                status.g_person_status[j].m_quar = 1;
                status.g_person_status[j].m_direction_vector.first =
                    cos(180 * M_PI / 180) *
                    status.m_move_step; // the move vector of x component
                status.g_person_status[j].m_direction_vector.second =
                    sin(180 * M_PI / 180) *
                    status.m_move_step; // the move vector of y component
                status.g_person_status[j].m_move_speed *= 2;
              }
            }
            status.g_infected_people.insert({status.g_person_status[j].m_index, status.g_person_status[j]});
          }
        }
      }
    }
  }
}

/* Running flow of Simulator(for c++)
 * 1. Everyone move once.
 * 2. Update everyone's status.
 *
 */
void Run(SimulationState &status) {
  size_t count = 100000;
  size_t m_hours = 0;
  while (--count) {
    Move(status);
    SpreadVirus(status);
    ++m_hours;
    // After a day(move 24 times), check whether infected_person's status needs
    // to be changed.
    if (m_hours % 24 == 0) {
      m_hours = 0;
      RecoveredOrDead(status);
    }
  }
}

void CheckPolicy(SimulationState &status) {
  if (status.m_policy == 0) {
    return;
  }
  else if (status.m_policy == 1) {
    size_t count = 0;
    for(auto iter = status.g_infected_people.begin(); iter != status.g_infected_people.end() && count < status.m_healthcare_capacity; ++iter) {
      status.g_person_status[iter->second.m_index].m_mortality_rate /= 2;
      iter->second.m_mortality_rate /= 2;
    }
  }
  else if (status.m_policy == 2) {
    // infected person have 95% prob go to quarantine
    return;
  }
}

// Running one round of simulator(for py)
void RunStep(SimulationState &status) {
  CheckPolicy(status);
  Move(status);
  SpreadVirus(status);
  RecoveredOrDead(status);
  ClassifyPeople(status);
}


void ClassifyPeople(SimulationState &status) {
  status.draw_health.clear();
  status.draw_infected.clear();
  status.draw_recovered.clear();
  status.draw_dead.clear();

  for (size_t i = 0; i < status.m_total_num_people; ++i) {
    if (status.g_person_status[i].m_status == 0) {
      status.draw_health.push_back(status.g_person_status[i].m_coordinate);
    } else if (status.g_person_status[i].m_status == 1) {
      status.draw_infected.push_back(status.g_person_status[i].m_coordinate);
    } else if (status.g_person_status[i].m_status == 2) {
      status.draw_recovered.push_back(status.g_person_status[i].m_coordinate);
    } else if (status.g_person_status[i].m_status == 3) {
      status.draw_dead.push_back(status.g_person_status[i].m_coordinate);
    }
  }
}

// just for test correctness in pure c++ environment.
int main() {
  // suppose that the simulate area is 2km * 2km = 4km^2, and the effective
  // range of infection is 2m. everyone move 1m during a time slice.
  SimulationState default_data(1000, 50, 1, 1.0, 0.05, 0.0, 100, 0.0, 2.0,
                                   2.0, 0.0, 1000, 1, 0.001, 0.02, 0);

  ShowStatus(default_data, 0);
  Run(default_data);
  ShowStatus(default_data, 0);
  return 0;
}
