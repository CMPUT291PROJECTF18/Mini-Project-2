#!/usr/bin/env bash

sort -t : -u $1 | ~/part2/break.pl | db_load -T -t $2 $3
