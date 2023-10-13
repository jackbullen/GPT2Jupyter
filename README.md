## GPT2Jupyter

Classes to simplify interacting with OpenAI API ChatCompletion endpoint.

1. `Conversation(api_key, role1_desc, role2_desc, model, max_tokens, notebook)`
   - pose_question(question, n) # n determines number of times agents interact
   - code() # generate code cell with codes from the messages
   - md() # generate markdown cell with all messages

2. `Ipynb(path_to_notebook)`
   - add_cell(cell)
   - save() # called by add_cell

3. `Agent(api_key, model, max_tokens)`
   - ask(question) # makes the call to ChatCompletion() and adds to messages
   - tell(information) # adds to messages without making api call
   - dump() # dump messages


&nbsp;
> Check out examples.ipynb for sample usage
