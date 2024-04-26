#!/bin/bash

poetry export -f requirements.txt --output ./docs/requirements.txt --without-hashes --with buildthedocs

# sphinx-apidoc ./statanalysis/ -o ./docs/source/statanalysis/ -f -E

cd docs
make html
cd ..
open docs/build/html/index.html
