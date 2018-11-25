#!/usr/bin/env bash

sudo add-apt-repository ppa:bitcoin/bitcoin -y
sudo apt-get update
sudo apt-get install libdb4.8-dev libdb4.8++-dev -y
sudo apt-get install db-util -y

mkdir ~/part2
mv part2.sh ~/part2/
mv break.pl ~/part2/
mv gen_idx.sh ~/part2/
chmod 733 ~/part2/*
