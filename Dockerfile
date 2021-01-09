FROM python:3.7-alpine

ENV PYTHONPATH /app/
WORKDIR /app

# Get our main application
COPY ./serenity ./serenity
COPY requirements/deploy.txt ./requirements.txt

# Get all libraries and packages required for later compiling
RUN apk update && \
    apk add --virtual build-deps curl openssl bash gcc python3-dev musl-dev && \
    apk add postgresql-dev

# Get the latest stable versions of kubectl and help
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl \
    && curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
    && chmod +x get_helm.sh && ./get_helm.sh

# Python packages
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

# Clean up intermediate dependencies
RUN apk del build-deps

# Lets do this
CMD ["python3", "-u", "-m", "serenity"]
