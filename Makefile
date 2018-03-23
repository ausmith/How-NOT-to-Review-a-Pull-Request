SHELL ?= /bin/bash

build:
	@docker build -f Dockerfile -t local/hntrapr:latest .

run:
	@docker run --name hntrapr -it local/hntrapr:latest

cleanup:
	@docker stop hntrapr
	@docker rm hntrapr
