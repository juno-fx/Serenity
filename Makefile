BROWSER := xdg-open

ifeq ($(OS),Windows_NT)
    BROWSER := start
endif

.PHONY: docs

# local devel workflow
setup:
	python -m pip install --upgrade pip
	pip3 install -r requirements/dev.txt
	pre-commit install

build:
	@docker-compose build

dev: build
	docker-compose up

run:
	python -m serenity

test:
	python -m unittest

lint:
	pylint ./serenity

clean-coverage:
	rm -rf htmlcov
	rm -rf .coverage

coverage: clean-coverage
	coverage run -m unittest
	coverage html
	$(BROWSER) "$(CURDIR)/htmlcov/index.html"

clean-docs:
	rm -rf docs/_build

docs: clean-docs
	sphinx-build -b html docs docs/_build
	$(BROWSER) "$(CURDIR)/docs/_build/index.html"

clean: clean-coverage clean-docs
	rm -rf src/*.egg-info


# deployment workflow
ops:
	minikube start --driver=docker
	#rm -rf .ops
	#mkdir -p .ops
	#git clone https://gitlab.hatfieldfx.com:9443/infra/hfx-kube-charts.git ./.ops/

infinity:
	@helm delete infinity || echo "Already clean"
	helm install infinity ./.ops/charts/infinity/$(VERSION)/ --wait
	#kubectl --namespace=default port-forward services/infinity 5432:5432
	#python db_setup.py

openfaas:
	@kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
	@helm repo add openfaas https://openfaas.github.io/faas-netes
	@helm repo update
	@helm upgrade openfaas --install openfaas/openfaas --namespace openfaas --set functionNamespace=openfaas-fn --set generateBasicAuth=true --wait
	@printf "\n\nUsername:\nadmin\nPassword:\n"
	@kubectl -n openfaas get secret basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode
	@printf "\n\nStarting port forward...\n\nOpen http://localhost:8080 to access the OpenFaaS gateway"
	@kubectl -n openfaas port-forward service/gateway 8080:8080

openfaas-creds:
	@printf "\n\nUsername:\nadmin\nPassword:\n"
	@kubectl -n openfaas get secret basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode

serenity: build
	@helm delete serenity || echo "Already clean"
	helm install --set "version=dev" serenity ./.ops/charts/serenity/$(VERSION)/ --wait
	kubectl port-forward service/serenity 3030:3030

logs:
	@kubectl logs deployments/serenity
