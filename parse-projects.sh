#!/bin/bash

echo -n '[' > ./docs/projects.json
git config --file .gitmodules --get-regexp path | awk '{ print "\"" $2 "\"," }' >> ./docs/projects.json
sed -i '$ s/,$//' paths.json
echo ']' >> ./docs/projects.json
