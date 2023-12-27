.PHONY: run
run:
	poetry run uvicorn src.core:app --reload