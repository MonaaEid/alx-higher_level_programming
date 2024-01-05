#!/bin/bash
response_body=$(curl -s "$1")

body_size=${#response_body}
echo " ${body_size}"