FROM python:3.7-alpine

ENV PYTHONPATH /app/

WORKDIR /app

# Get and install our main application
COPY ./dist/serenity-0.0.0-py3-none-any.whl ./serenity-0.0.0-py3-none-any.whl

RUN python3 -m pip install --upgrade pip
RUN pip3 install python-dotenv
RUN pip3 install serenity-0.0.0-py3-none-any.whl && rm -rf ./serenity-0.0.0-py3-none-any.whl

# Lets do this
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3030"]
