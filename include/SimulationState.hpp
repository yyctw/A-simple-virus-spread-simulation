#pragma once

#include <math.h>
#include <utility>
#include <vector>
#include <random>
#include <ctime>
#include <unordered_map>
#include <map>


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
  // health status 0: health, 1: infected, 2: recovered, 3: dead.
  size_t m_status;
  // recovery_rate
  float m_recovery_rate;
  // morality_rate
  float m_mortality_rate;
  // quarantine bound
  float m_quar_bound;
  // bound
  float lx;
  float rx;
  size_t m_quar = 0;

  // member function for read data
  size_t index() const { return m_index; }
  float coord_x() const { return m_coordinate.first; }
  float coord_y() const { return m_coordinate.second; }
  size_t status() const { return m_status; }
};

struct myBoundary {
  // data
  float left_x;
  float right_x;
  float up_y;
  float down_y;
};

class SimulationState {

public:
  // Custom constructor
  // default constructor
  SimulationState(size_t total_num_people, size_t infected_people,
                      size_t move_speed, float infect_rate,
                      float mortality_rate, float recovery_rate,
                      size_t healthcare_capacity, float lx, float rx, float uy,
                      float dy, size_t simulation_step, size_t mode, float move_step,
                      float spread_range, size_t policy)
      : m_total_num_people(total_num_people),
        m_infected_people(infected_people), m_move_speed(move_speed),
        m_infect_rate(infect_rate), m_mortality_rate(mortality_rate),
        m_recovery_rate(recovery_rate),
        m_healthcare_capacity(healthcare_capacity), m_simulation_step(simulation_step),
        m_mode(mode), m_move_step(move_step), m_spread_range(spread_range),
        m_policy(policy), g_person_status(total_num_people), draw_health(total_num_people - infected_people),
        draw_infected(infected_people), draw_recovered(0), draw_dead(0) {
    g_boundary.left_x = lx;
    g_boundary.right_x = rx;
    g_boundary.up_y = uy;
    g_boundary.down_y = dy;
    m_InitSimulation(*this);
  }


  // init the status of all people
  void m_InitSimulation(SimulationState &uninit_state){
    // init everyone status
    std::default_random_engine generator(time(NULL));
    float my_left_x = uninit_state.g_boundary.left_x;
    if(uninit_state.m_policy == 2) {
      my_left_x = 0.5;
    }
    std::uniform_real_distribution<float> unif_x(my_left_x,
                                                 uninit_state.g_boundary.right_x);
    std::uniform_real_distribution<float> unif_y(uninit_state.g_boundary.down_y,
                                                 uninit_state.g_boundary.up_y);

    for (size_t i = 0; i < uninit_state.m_total_num_people; ++i) {
      uninit_state.g_person_status[i].m_index = i; // x coord.
      uninit_state.g_person_status[i].m_coordinate.first =
          unif_x(generator); // x coord.
      uninit_state.g_person_status[i].m_coordinate.second =
          unif_y(generator); // y coord.
      float direct_angle = generator() % 360;
      uninit_state.g_person_status[i].m_direction_vector.first =
          cos(direct_angle * M_PI / 180) *
          uninit_state.m_move_step; // the move vector of x component
      uninit_state.g_person_status[i].m_direction_vector.second =
          sin(direct_angle * M_PI / 180) *
          uninit_state.m_move_step; // the move vector of y component
      uninit_state.g_person_status[i].m_move_speed = uninit_state.m_move_speed;
      uninit_state.g_person_status[i].m_status = 0;
      uninit_state.g_person_status[i].m_recovery_rate =
          uninit_state.m_recovery_rate;
      uninit_state.g_person_status[i].m_mortality_rate =
          uninit_state.m_mortality_rate;
      uninit_state.g_person_status[i].lx = my_left_x;
      uninit_state.g_person_status[i].rx = uninit_state.g_boundary.right_x;
      uninit_state.g_person_status[i].m_quar = 0;
    }


    if (uninit_state.m_policy == 2) {
      std::uniform_real_distribution<float> unif(0, 1);
      float prob = unif(generator);
      if(prob <= uninit_state.m_accept_isolation_rate){
        for (size_t i = 0; i < uninit_state.m_infected_people; ++i) {
          uninit_state.g_person_status[i].m_quar = 1;
          uninit_state.g_person_status[i].m_direction_vector.first =
                cos(180 * M_PI / 180) *
                uninit_state.m_move_step; // the move vector of x component
          uninit_state.g_person_status[i].m_direction_vector.second =
                sin(180 * M_PI / 180) *
                uninit_state.m_move_step; // the move vector of y component
          uninit_state.g_person_status[i].m_move_speed *= 2;
        }
      }
    }

    else if (uninit_state.m_policy == 3) {
      // 60% can not move
      for (size_t i = uninit_state.m_total_num_people; i > uninit_state.m_total_num_people * 0.4; --i){
        uninit_state.g_person_status[i].m_move_speed = 0;
      }
    }
    else if (uninit_state.m_policy == 4) {
      // 90% can not move
      for (size_t i = uninit_state.m_total_num_people; i > uninit_state.m_total_num_people * 0.1; --i){
        uninit_state.g_person_status[i].m_move_speed = 0;
      }
    }

    // set init infected people
    for (size_t i = 0; i < uninit_state.m_infected_people; ++i) {
      uninit_state.g_person_status[i].m_status = 1;
      uninit_state.g_infected_people.insert({uninit_state.g_person_status[i].m_index, uninit_state.g_person_status[i]});
    }

    // set init health people
    //for (size_t i = uninit_state.m_infected_people; i < uninit_state.m_total_num_people; ++i) {
    //}

  }

  // Print current status
  void PrintStatus() {
    std::cout << "===== Init Config =====" << std::endl;
    std::cout << "total number of people = " << this->m_total_num_people
              << std::endl;
    std::cout << "infected people = " << this->m_infected_people << std::endl;
    std::cout << "moving speed of people = " << this->m_move_speed << std::endl;
    std::cout << "infected rate = " << this->m_infect_rate << std::endl;
    std::cout << "mortality rate = " << this->m_mortality_rate << std::endl;
    std::cout << "recovery rate = " << this->m_recovery_rate << std::endl;
    std::cout << "healthcare capacity = " << this->m_healthcare_capacity
              << std::endl;
    std::cout << "===== Global Status =====" << std::endl;
    std::cout << "total number of people = " << this->m_total_num_people
              << std::endl;
    std::cout << "health people =  " << this->g_num_health << std::endl;
    std::cout << "infected people =  " << this->g_num_infected << std::endl;
    std::cout << "recovered people =  " << this->g_num_recovered << std::endl;
    std::cout << "dead people =  " << this->g_num_dead << std::endl;
  }

  // member function for read data
  size_t total_num_people() const { return m_total_num_people; }
  size_t infected_people() const { return m_infected_people; }
  size_t move_speed() const { return m_move_speed; }
  float infect_rate() const { return m_infect_rate; }
  float mortality_rate() const { return m_mortality_rate; }
  float recovery_rate() const { return m_recovery_rate; }
  size_t healthcare_capacity() const { return m_healthcare_capacity; }
  // global info
  size_t num_health() const { return g_num_health; }
  size_t num_infected() const { return g_num_infected; }
  size_t num_dead() const { return g_num_dead; }
  size_t num_recovered() const { return g_num_recovered; }
  float lx_bound() const { return g_boundary.left_x; }
  float rx_bound() const { return g_boundary.right_x; }
  float uy_bound() const { return g_boundary.up_y; }
  float dy_bound() const { return g_boundary.down_y; }
  bool dirty() const { return dirty_bit; }
  size_t simulation_step() const { return m_simulation_step; }
  size_t mode() const { return m_mode; }
  size_t policy() const { return m_policy; }

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
  // simulation steps
  size_t m_simulation_step = 10000;
  // mode
  size_t m_mode = 0;
  // the length of step per time
  float m_move_step = 0.001;
  // the effective virus spread range
  float m_spread_range = 0.02;
  // policy
  size_t m_policy = 0;
  // the probability of accepting isolation
  float m_accept_isolation_rate = 0.95;

  // parameter during simulation (global status)
  // the global number of health people.
  size_t g_num_health = m_total_num_people - m_infected_people;
  // the global number of infected people.
  size_t g_num_infected = m_infected_people;
  // the global number of dead people.
  size_t g_num_dead = 0;
  // the global number of recovered people.
  size_t g_num_recovered = 0;
  // dirty bit = 1 if data have been modified.
  bool dirty_bit = 1;

  // global parameter
  myBoundary g_boundary;
  std::vector<PersonStatus> g_person_status;
  //std::map<size_t, PersonStatus> g_health_people;
  std::map<size_t, PersonStatus> g_infected_people;
  std::vector<std::pair<float, float>> draw_health;
  std::vector<std::pair<float, float>> draw_infected;
  std::vector<std::pair<float, float>> draw_recovered;
  std::vector<std::pair<float, float>> draw_dead;
};
