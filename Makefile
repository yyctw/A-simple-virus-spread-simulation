.PHONY: all test benchmark clean run re

CC = clang++-11
CFLAGS = -Wall -std=c++17 -O3 -m64 -fPIC

INCLUDE = -Iinclude \
		  -I./

PYTHON = python3

OBJS = lib/MySimulator.cpp

EXEC = MySimulator

TARGET = _simulator

all: $(TARGET).*.so $(EXEC)

$(EXEC): lib/MySimulator.o
	$(CC) $(CFLAGS) $^ -o $(EXEC)

%.o: %.cpp
	$(CC) $^ -o $@ $(CFLAGS) $(INCLUDE) -c

$(TARGET).*.so: lib/MySimulator.cpp lib/simulator_pybind.cpp
	$(CC) $(CFLAGS) $(INCLUDE) -shared `$(PYTHON) -m pybind11 --includes` $^ -o $(TARGET)`$(PYTHON)-config --extension-suffix`

test: all
	$(PYTHON) -m pytest -v

run: all
	./$(EXEC)

re:
	make clean
	make
	make run

benchmark:
	$(PYTHON) benchmark.py

clean:
	$(RM) lib/*.o $(TARGET).*.so $(EXEC)
	$(RM) -r __pycache__/
