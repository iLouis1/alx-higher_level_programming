#!/bin/bash
# This script takes an URL, shows the Allowed OPTIONS
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
