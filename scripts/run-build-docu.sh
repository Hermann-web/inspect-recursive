#!/bin/bash

poetry export -f requirements.txt --output ./docs/requirements.txt --without-hashes --with buildthedocs
cd docs
make html
cd ..
