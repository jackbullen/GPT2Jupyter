## GPT2Jupyter

Classes to simplify interacting with OpenAI API ChatCompletion endpoint.

1. `Agent(api_key, model, max_tokens)`
   - ask(question)
   - tell(information)
   - dump()

2. `Ipynb(path_to_notebook)`
   - add_cell(cell)
   - save() # called by add_cell

&nbsp;
> Check out examples.ipynb for sample usage
