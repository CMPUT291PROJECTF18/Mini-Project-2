#!/usr/bin/env bash

sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get install libdb4.8-dev libdb4.8++-dev
sudo apt-get install db-util

mkdir ~/part2
mv part2.sh ~/part2/
mv break.pl ~/part2/
chmod 733 ~/part2/*
