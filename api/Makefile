-include ./config/.env_{ENV}

confirm_env:
	@echo "####################"
	@echo "ENV: ${ENV}"
	@echo "CONF_FILE: ./config/.env_${ENV}"
	@echo "####################"
	@read -p "Are you sure? (y/n): " yn; \
	if [ "$$yn" != "y" ]; then \
		exit 0; \
	fi

dev: confirm_env
	ENV=${ENV} ./.venv/bin/uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
