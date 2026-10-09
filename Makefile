CXX = g++
CXXFLAGS = -Wall -std=c++17 -I./raylib/src
LDFLAGS = -L./raylib/src -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
SRC = main.cpp
TARGET = main

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET) $(LDFLAGS)

run: $(TARGET)
	DRI_PRIME=0 ./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all run clean

