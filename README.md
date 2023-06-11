# OpenAI API Examples

## IDE Preparations

This repository is built for usage with VS Code and devcontainers.

The devcontainer setup takes care of the necessary installations to work with Python, the OpenAI library and other necessary components.

## API Usage Preparations

* You need to be signed up on [OpenAI](https://platform.openai.com/).
* In your account settings you need to provide your payment method (eg. credit card details)
* In your account settings you need to create an API KEY (and store that key in a save place)

## "Hello World"

The goal of this section is to verify that your end-to-end setup is working properly.

The content is inspired by [OpenAI's question answering tutorial](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb).

The "Hello World" task is to answer questions about an article provided to the program.
As a default a [Wikipedia article](https://en.wikipedia.org/wiki/Curling_at_the_2022_Winter_Olympics) about curling in the 2022 Olympics is used.

Run the program as shown below

```bash
python hello_world.py
```

Example questions:

* Which athletes won the gold medal in curling at the 2022 Winter Olympics?
* List the countries that participated in the 2022 curling winter olypmic games
* List the team members of all teams winning gold in the 2022 curling olympics
