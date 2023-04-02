

VIRTUALENV_PATH=./venv

REQUIREMENTS_FILE_PATH=./requirements.frozen
TEST_REQUIREMENTS_FILE_PATH=./requirements.test.frozen


install_git_hooks:
	pre-commit install


run_git_hooks:
	pre-commit run --all-files


create_virtualenv:
	@echo "Creating virtualenv..."
	python3 -m venv "${VIRTUALENV_PATH}"
	@echo "Done!"


install_requirements:
	@echo "Installing requirements..."
	${VIRTUALENV_PATH}/bin/pip install -r "${REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_test_requirements:
	@echo "Installing test requirements..."
	${VIRTUALENV_PATH}/bin/pip install -r "${TEST_REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_all_requirements: install_requirements install_test_requirements


run_unit_tests:
	@echo "Running unit tests..."
	@. ${VIRTUALENV_PATH}/bin/activate && \
	cd audio_to_chatgpt && \
	python -m unittest discover -s . -p '*_test.py' && \
	cd ..
	@echo "Done!"


docker_build:
	docker build -t audio_to_chatgpt .


docker_run:
	docker run -it audio_to_chatgpt


docker_build_and_run: docker_build docker_run
