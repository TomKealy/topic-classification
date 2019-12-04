.PHONY: lint build run push collect-data train-propensity train-proximity score-propensity score-proximity test

ifneq (,$(findstring $(firstword $(MAKECMDGOALS)), run))
RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)
endif

#################################################################################
# GLOBALS                                                                       #
#################################################################################

export PYTHONPATH = $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

REPO = /topic-classification

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Lint using flake8
lint:
	pip install -r lint-requirements.txt
	flake8 --ignore=E501 ds_reactivations

## Test
test:
	echo to-do

## Build docker container
build:
	docker build .

## Run scripts in docker container
run:
	docker run --rm $(RUN_ARGS)