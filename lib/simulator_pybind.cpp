#include <iostream>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "MySimulator.hpp"
#include "Parameter.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_simulator, m) {
  m.doc() = "test my simulator";
  m.def("Move", &Move, "Everyone move once");
  m.def("SpreadVirus", &SpreadVirus,
        "After move once, the infected_people have probability to spread the "
        "virus.");
  m.def("RecoveredOrDead", &RecoveredOrDead,
        "After a day, the infected_people have probability change to recovered "
        "or dead.");
  m.def("ClassifyPeople", &ClassifyPeople,
        "Classify People for visualization.");
  m.def("RunStep", &RunStep, "Run one step of simulation.");

  py::class_<PersonStatus>(m, "PersonStatus")
      .def(py::init<size_t, std::pair<float, float>, std::pair<float, float>,
                    size_t, size_t, float, float>())
      .def_property_readonly("index", &PersonStatus::index)
      .def_property_readonly("coord_x", &PersonStatus::coord_x)
      .def_property_readonly("coord_y", &PersonStatus::coord_y)
      .def_property_readonly("status", &PersonStatus::status);

  py::class_<SimulationState>(m, "SimulationState")
      .def(py::init<size_t, size_t, size_t, float, float, float, int, float,
                    float, float, float, size_t, size_t, float, float, size_t>())
      // read parameter
      .def_property_readonly("total_num_people",
                             &SimulationState::total_num_people)
      .def_property_readonly("infected_people",
                             &SimulationState::infected_people)
      .def_property_readonly("move_speed", &SimulationState::move_speed)
      .def_property_readonly("infect_rate", &SimulationState::infect_rate)
      .def_property_readonly("mortality_rate",
                             &SimulationState::mortality_rate)
      .def_property_readonly("recovery_rate",
                             &SimulationState::recovery_rate)
      .def_property_readonly("healthcare_capacity",
                             &SimulationState::healthcare_capacity)
      .def_property_readonly("num_health", &SimulationState::num_health)
      .def_property_readonly("num_infected", &SimulationState::num_infected)
      .def_property_readonly("num_dead", &SimulationState::num_dead)
      .def_property_readonly("num_recovered",
                             &SimulationState::num_recovered)
      .def_property_readonly("lx_bound", &SimulationState::lx_bound)
      .def_property_readonly("rx_bound", &SimulationState::rx_bound)
      .def_property_readonly("uy_bound", &SimulationState::uy_bound)
      .def_property_readonly("dy_bound", &SimulationState::dy_bound)
      .def_property_readonly("dirty", &SimulationState::dirty)
      .def_property_readonly("simulation_step", &SimulationState::simulation_step)
      .def_property_readonly("mode", &SimulationState::mode)
      .def_property_readonly("policy", &SimulationState::policy)

      .def_property_readonly("print_status", &SimulationState::PrintStatus)

      .def_readwrite("g_person_status", &SimulationState::g_person_status)
      .def_readwrite("draw_health", &SimulationState::draw_health)
      .def_readwrite("draw_infected", &SimulationState::draw_infected)
      .def_readwrite("draw_recovered", &SimulationState::draw_recovered)
      .def_readwrite("draw_dead", &SimulationState::draw_dead);
}
