.PHONY: all test benchmark clean

CC = clang++-11
CFLAGS = -Wall -std=c++17 -O3 -m64 -fPIC

INCLUDE = -Iinclude

PYTHON = python3

OBJS = lib/MySimulator.cpp

EXEC = MySimulator

TARGET = _simulator

all: $(TARGET).*.so $(EXEC)

$(EXEC): lib/MySimulator.o
	$(CC) $(CFLAGS) $^ -o $(EXEC)

%.o: %.cpp
	$(CC) $^ -o $@ $(CFLAGS) $(INCLUDE) -c

$(TARGET).*.so: lib/MySimulator.cpp simulator_pybind.cpp
	$(CC) $(CFLAGS) -shared `$(PYTHON) -m pybind11 --includes` $^ -o $(TARGET)`$(PYTHON)-config --extension-suffix`

test: all
	$(PYTHON) -m pytest -v

benchmark:
	$(PYTHON) benchmark.py

clean:
	$(RM) lib/*.o $(TARGET).*.so $(EXEC)
