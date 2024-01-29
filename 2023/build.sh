#!/bin/bash

DEBUGARGS="-g3 -Wall -Wextra -Wconversion -Wdouble-promotion -Wno-unused-parameter -Wno-unused-function -Wno-sign-conversion"

build () {
  gcc main.c ../regex.c $DEBUGARGS
}

for DAY in {01..25}
do
    if [ -d $DAY ]; then
      cd $DAY
      if [ -e main.c ]; then
        echo "$DAY: Building"
        build

        echo "$DAY: Testing ... "
        ./a.out >/dev/null 2>&1
        if [ $? = 0 ]; then
          echo "  Success!"
        else
          echo "  Failure!"
        fi
      fi
      cd ..
    fi
done

