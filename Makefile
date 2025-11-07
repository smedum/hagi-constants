.PHONY: check test clean install verify

check: install test
	@echo "✅ All HAGI verification checks passed"

install:
	pip install -r requirements.txt

test:
	pytest test_constants.py -v --tb=short

verify: check
	@echo "🎯 HAGI Constants implementation verified"

clean:
	rm -rf __pycache__ .pytest_cache
	find . -type f -name "*.pyc" -delete
