
CONDA_ENV_NAME ?= routedrone

#===== Dev Environment =====

env-create:
	conda env create -n $(CONDA_ENV_NAME) -f environment_dev.yml

env-remove:
	conda env remove -n $(CONDA_ENV_NAME)

env-update: env-remove env-create
