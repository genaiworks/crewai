brew install pipx
pipx ensurepath
pipx install poetry
poetry --version

Create pyproject.toml
poetry install --no-root
poetry env list

To run into the new poetry env
poetry shell 

poetry add langchain-openai=0.0.5
poetry remove tools
