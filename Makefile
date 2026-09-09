# ======================
# Project and Main Files
# ======================

NAME = community
SHELL := /bin/bash
.DEFAULT_GOAL = all

# ======================
# Rules
# ======================

all:  up

up:
	@docker compose up -d --build
	@echo "✅ ${NAME} is running at http://localhost:5000";

down:
	@docker compose down
	@echo "✅ ${NAME} has been stopped.";

clean:
	@docker compose down --rmi local --remove-orphans
	@echo "✅ ${NAME} has been cleaned.";

fclean:
	@docker compose down --rmi local --volumes --remove-orphans
	@echo "✅ ${NAME} has been deep cleaned.";

.PHONY: all up down clean fclean
