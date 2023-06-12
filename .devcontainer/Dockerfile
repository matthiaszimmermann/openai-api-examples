# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.11-bullseye
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

USER vscode

# upgrade pip
RUN python -m pip install --upgrade pip

# install python libraries
RUN python -m pip install python-dotenv
RUN python -m pip install openai
RUN python -m pip install pandas
RUN python -m pip install tiktoken
RUN python -m pip install scipy

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

WORKDIR /workspace
