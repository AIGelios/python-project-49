install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain-games --cov-report xml

lint:
	poetry run flake8 brain-games

selfcheck:
	poetry check

check:
	selfcheck
	test
	lint

build:
	check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

update:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall
