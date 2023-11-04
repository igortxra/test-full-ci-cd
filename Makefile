# Code quality
test:
	coverage run

test-coverage:
	coverage report

coverage-browser:
	 coverage html && cd htmlcov && python -m webbrowser index.html && cd ..

lint:
	pylint --recursive=y app/ tests/

format:
	pyink -q . && isort .

security-checks:
	bandit -c pyproject.toml -r app
