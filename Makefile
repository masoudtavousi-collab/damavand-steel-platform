.PHONY: help setup validate test

help:
	@echo "setup     Prepare local environment (placeholder)"
	@echo "validate  Validate repository scaffold"
	@echo "test      Run Product foundations, Atlas, and scaffold validation"

setup:
	@./scripts/setup.sh

validate:
	@./scripts/validate.sh

test:
	@./scripts/test.sh
