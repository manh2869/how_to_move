#!/bin/bash
set -e

# Biên dịch chương trình nếu chưa có hoặc có thay đổi
echo "Đang biên dịch main.cpp..."
g++ -Wall -std=c++17 -I./raylib/src main.cpp -o main -L./raylib/src -lraylib -lGL -lm -lpthread -ldl -lrt -lX11

echo "Chạy chương trình (sử dụng AMD iGPU để mở tức thì)..."
DRI_PRIME=0 ./main

