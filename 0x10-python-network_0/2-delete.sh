#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument, displays body of response
curl -s "$1" -X DELETE
