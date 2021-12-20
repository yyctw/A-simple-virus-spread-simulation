#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>

#include "Parameter.hpp"
#include "MySimulator.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_simulator, m) {
  m.doc() = "test my simulator";
  m.def("InitSimulation", &InitSimulation, "After Read Config file, init the environment of simulation");
  m.def("Move", &Move, "Everyone move once");
  m.def("SpreadVirus", &SpreadVirus, "After move once, the infected_people have probability to spread the virus.");
  m.def("RecoveredOrDead", &RecoveredOrDead, "After a day, the infected_people have probability change to recovered or dead.");
  m.def("ClassifyPeople", &ClassifyPeople, "Classify People for visualization.");

  py::class_<PersonStatus>(m, "PersonStatus")
    .def(py::init<size_t, std::pair<float, float>, std::pair<float, float>, size_t, size_t, float, float>())
    .def_property_readonly("index", &PersonStatus::index)
    .def_property_readonly("coord_x", &PersonStatus::coord_x)
    .def_property_readonly("coord_y", &PersonStatus::coord_y)
    .def_property_readonly("status", &PersonStatus::status);

  py::class_<SimulationParameter>(m, "SimulationParameter")
    .def(py::init<size_t, size_t, size_t, float, float, float, int, float, float, float, float, size_t, size_t, float, float>())
    // read parameter
    .def_property_readonly("total_num_people", &SimulationParameter::total_num_people)
    .def_property_readonly("infected_people", &SimulationParameter::infected_people)
    .def_property_readonly("move_speed", &SimulationParameter::move_speed)
    .def_property_readonly("infect_rate", &SimulationParameter::infect_rate)
    .def_property_readonly("mortality_rate", &SimulationParameter::mortality_rate)
    .def_property_readonly("recovery_rate", &SimulationParameter::recovery_rate)
    .def_property_readonly("healthcare_capacity", &SimulationParameter::healthcare_capacity)
    .def_property_readonly("num_health", &SimulationParameter::num_health)
    .def_property_readonly("num_infected", &SimulationParameter::num_infected)
    .def_property_readonly("num_dead", &SimulationParameter::num_dead)
    .def_property_readonly("num_recovered", &SimulationParameter::num_recovered)
    .def_property_readonly("lx_bound", &SimulationParameter::lx_bound)
    .def_property_readonly("rx_bound", &SimulationParameter::rx_bound)
    .def_property_readonly("uy_bound", &SimulationParameter::uy_bound)
    .def_property_readonly("dy_bound", &SimulationParameter::dy_bound)
    .def_property_readonly("dirty", &SimulationParameter::dirty)
    .def_property_readonly("simu_step", &SimulationParameter::simu_step)
    .def_property_readonly("mode", &SimulationParameter::mode)

    .def_property_readonly("print_status", &SimulationParameter::PrintStatus)

    .def_readwrite("g_person_status", &SimulationParameter::g_person_status)
    .def_readwrite("draw_health", &SimulationParameter::draw_health)
    .def_readwrite("draw_infected", &SimulationParameter::draw_infected)
    .def_readwrite("draw_recovered", &SimulationParameter::draw_recovered)
    .def_readwrite("draw_dead", &SimulationParameter::draw_dead);
}
