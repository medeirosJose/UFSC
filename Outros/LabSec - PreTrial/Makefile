# Declaration of variables
CPP = g++
CPPFLAGS = -std=c++11

EXE = main

SOURCES = ./src/HexToB64.cpp ./src/FixedXOR.cpp ./src/XORCypher.cpp ./src/single-charXOR.cpp ./src/main.cpp
HEADERS = ./include/HexToB64.h ./include/FixedXOR.h ./include/XORCypher.h ./include/single-charXOR.h
OBJECTS = $(SOURCES:.cpp=.o)

$(EXE): $(OBJECTS)
	@echo "-> COMPILING FILES"
	$(CPP) $(CPPFLAGS) -o $@ $(OBJECTS)
	@echo "-> DONE!"
	@echo "-> Run './$(EXE)' to execute the code"

	rm -f ./src/*.o 

$(OBJECTS): $(SOURCES) $(HEADERS) Makefile

clean:
	rm -f *~ $(EXE)
