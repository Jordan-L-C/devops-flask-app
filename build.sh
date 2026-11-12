#!/usr/bin/env bash
set -euo pipefail

# 1. Update the machine
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update
sudo apt-get dist-upgrade -y

# 2. Install build tools
sudo apt-get install -y build-essential git

# 3. Build
make

# 4. Copy the executable somewhere to collect it
mkdir -p dist
cp conway dist/
