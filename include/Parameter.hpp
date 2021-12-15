#pragma once

#include <vector>
#include <utility>
#include <math.h>

struct PersonStatus {
  // all need status of one person
  // person number
  size_t m_index;
  // current location for the points.
  std::pair<float, float> m_coordinate;
  // current move direction
  std::pair<float, float> m_direction_vector;
  // move speed
  size_t m_move_speed;
  // health status 0: health, 1: infected, 2: recovered, -1: dead.
  size_t m_status;
  // recovery_rate
  float m_recovery_rate;
  // morality_rate
  float m_mortality_rate;
};

struct myBoundary {
  // data
  float left_x;
  float right_x;
  float up_y;
  float down_y;
};

class SimulationParameter {

public:
  // Custom constructor
  // default constructor
  SimulationParameter(size_t total_num_people, size_t infected_people,
                      size_t move_speed, float infect_rate, float mortality_rate,
                      float recovery_rate, size_t healthcare_capacity, float lx, float rx, float uy, float dy)
      : m_total_num_people(total_num_people),
        m_infected_people(infected_people), m_move_speed(move_speed),
        m_infect_rate(infect_rate), m_mortality_rate(mortality_rate),
        m_recovery_rate(recovery_rate),
        m_healthcare_capacity(healthcare_capacity),
        g_person_status(total_num_people) {
          g_boundary.left_x = lx;
          g_boundary.right_x = rx;
          g_boundary.up_y = uy;
          g_boundary.down_y = dy;
        }

  // copy constructor
  SimulationParameter(const SimulationParameter &s)
      : m_total_num_people(s.m_total_num_people),
        m_infected_people(s.m_infected_people), m_move_speed(s.m_move_speed),
        m_infect_rate(s.m_infect_rate), m_mortality_rate(s.m_mortality_rate),
        m_recovery_rate(s.m_recovery_rate),
        m_healthcare_capacity(s.m_healthcare_capacity) {}

  // TODO
  // move constructor
  // SimulationParameter(SimulationParameter &&s)
  // Print current status
  void PrintStatus() {
    std::cout << "total number of people = " << this->m_total_num_people
              << std::endl;
    std::cout << "infected people = " << this->m_infected_people << std::endl;
    std::cout << "moving speed of people = " << this->m_move_speed << std::endl;
    std::cout << "infected rate = " << this->m_infect_rate << std::endl;
    std::cout << "mortality rate = " << this->m_mortality_rate << std::endl;
    std::cout << "recovery rate = " << this->m_recovery_rate << std::endl;
    std::cout << "healthcare capacity = " << this->m_healthcare_capacity
              << std::endl;
  }

  // member function for read data
  size_t total_num_people() const { return m_total_num_people; }
  size_t infected_people() const { return m_infected_people; }
  size_t move_speed() const { return m_move_speed; }
  float infect_rate() const { return m_infect_rate; }
  float mortality_rate() const { return m_mortality_rate; }
  float recovery_rate() const { return m_recovery_rate; }
  size_t healthcare_capacity() const { return m_healthcare_capacity; }

  // all input parameter
  // total number of people for simulation(optional, default = 1000(<= 2000))
  size_t m_total_num_people = 1000;
  // init number of infected people (percentage or int) (optional, default = 1%)
  size_t m_infected_people = 0.01 * m_total_num_people;
  // moving speed of people (optional, default = 1)
  size_t m_move_speed = 1;
  // virus infection rate (optional, default = 70%)
  float m_infect_rate = 0.7;
  // virus mortality rate (optional, default = 30%)
  float m_mortality_rate = 0.3;
  // recovery rate (optional, default = 30%)
  float m_recovery_rate = 0.3;
  // healthcare capacity (optional, default = 100, The mortality rate is
  // halved.)
  size_t m_healthcare_capacity = 100;

  // parameter during simulation (global status)
  // the global number of health people.
  size_t g_num_health = m_total_num_people - m_infected_people;
  // the global number of infected people.
  size_t g_num_infected = m_infected_people;
  // the global number of dead people.
  size_t g_num_dead = 0;
  // the global number of recovered people.
  size_t g_num_recovered = 0;


  // global parameter
  myBoundary g_boundary;
  std::vector<PersonStatus> g_person_status;
};
