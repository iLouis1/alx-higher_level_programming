#!/bin/bash
# this displays only status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
