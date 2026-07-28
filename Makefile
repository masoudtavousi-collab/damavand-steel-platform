.PHONY: help setup validate test

help:
	@echo "setup     Prepare isolated local validation environment"
	@echo "validate  Validate repository scaffold"
	@echo "test      Run unified repository and BP1 validation"

setup:
	@./scripts/setup.sh

validate:
	@./scripts/validate.sh

test:
	@./scripts/test.sh
