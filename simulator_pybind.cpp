#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>

#include "include/Parameter.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_simulator, m) {
  m.doc() = "test my simulator";

  py::class_<SimulationParameter>(m, "SimulationParameter")
    .def(py::init<size_t, size_t, size_t, float, float, float, size_t, float, float, float, float>())
    // read parameter
    .def_property_readonly("total_num_people", &SimulationParameter::total_num_people)
    .def_property_readonly("infected_people", &SimulationParameter::infected_people)
    .def_property_readonly("move_speed", &SimulationParameter::move_speed)
    .def_property_readonly("infect_rate", &SimulationParameter::infect_rate)
    .def_property_readonly("mortality_rate", &SimulationParameter::mortality_rate)
    .def_property_readonly("recovery_rate", &SimulationParameter::recovery_rate)
    .def_property_readonly("healthcare_capacity", &SimulationParameter::healthcare_capacity)
    .def_property_readonly("print_status", &SimulationParameter::PrintStatus);
}
