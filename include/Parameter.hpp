#pragma once

class SimulationParameter {

public:
  // Custom constructor
  // default constructor
  SimulationParameter(size_t total_num_people, size_t infected_people,
                      size_t move_speed, float infect_rate, float morality_rate,
                      size_t recovery_time, size_t healthcare_capacity)
      : m_total_num_people(total_num_people),
        m_infected_people(infected_people), m_move_speed(move_speed),
        m_infect_rate(infect_rate), m_mortality_rate(morality_rate),
        m_recovery_time(recovery_time),
        m_healthcare_capacity(healthcare_capacity) {}

  // copy constructor
  SimulationParameter(const SimulationParameter &s)
      : m_total_num_people(s.m_total_num_people),
        m_infected_people(s.m_infected_people), m_move_speed(s.m_move_speed),
        m_infect_rate(s.m_infect_rate), m_mortality_rate(s.m_mortality_rate),
        m_recovery_time(s.m_recovery_time),
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
    std::cout << "morality rate = " << this->m_mortality_rate << std::endl;
    std::cout << "recovery time = " << this->m_recovery_time << std::endl;
    std::cout << "healthcare capacity = " << this->m_healthcare_capacity
              << std::endl;
  }

  // member function for read data
  size_t total_num_people() const { return m_total_num_people; }
  size_t infected_people() const { return m_infected_people; }
  size_t move_speed() const { return m_move_speed; }
  float infect_rate() const { return m_infect_rate; }
  float mortality_rate() const { return m_mortality_rate; }
  size_t recovery_time() const { return m_recovery_time; }
  size_t healthcare_capacity() const { return m_healthcare_capacity; }

  // all need parameter
  // total number of people for simulation(optional, default = 1000(<= 2000))
  size_t m_total_num_people;
  // init number of infected people (percentage or int) (optional, default = 1%)
  size_t m_infected_people;
  // moving speed of people (optional, default = 1)
  size_t m_move_speed;
  // virus infection rate (optional, default = 70%)
  float m_infect_rate;
  // virus mortality rate (optional, default = 30%)
  float m_mortality_rate;
  // recovery time (optional, default = 5 day)
  size_t m_recovery_time;
  // healthcare capacity (optional, default = 100, The mortality rate is
  // halved.)
  size_t m_healthcare_capacity;
};
