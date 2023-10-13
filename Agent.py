import openai
from time import sleep
from Ipynb import Ipynb

class Agent:
    def __init__(self, api_key, model='gpt-3.5-turbo', max_tokens=150):
        openai.api_key = api_key
        self.model = model
        self.messages = []
        self.max_tokens = max_tokens
    
    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content,
        })
    
    def ask(self, question):
        self.add_message("user", question)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            max_tokens=self.max_tokens,
        )
        response_msg = response.choices[0].message.content.strip()
        self.add_message("system", response_msg)
        return response_msg

    def tell(self, information, role="system"):
        self.add_message(role, information)
    
    def dump(self):
        output = ""
        for message in self.messages:
            output += message["role"] + ": " + message["content"] + "\n"
        return output

    def clear(self):
        self.messages = []

    def __str__(self):
        return str(self.model) + "@" + str(self.max_tokens)
    
class Conversation:
    def __init__(self, api_key, role1_desc, role2_desc, model='gpt-3.5-turbo', max_tokens=150, sleep_duration=0.5, notebook='examples.ipynb'):
        self.agent1 = Agent(api_key, model=model, max_tokens=max_tokens)
        self.agent2 = Agent(api_key, model=model, max_tokens=max_tokens)
        self.agent1.tell(role1_desc)
        self.agent2.tell(role2_desc)
        self.sleep_duration = sleep_duration
        self.notebook = Ipynb(notebook)
    
    def pose_question(self, question, n=2):
        response = self.agent2.ask(question)
        print(response, type(response))
        for _ in range(n):
            response = self.agent1.ask(response)
            print('Agent1:', response)
            response = self.agent2.ask(response)
            print('Agent2:', response)
            sleep(self.sleep_duration)

    def code(self):
        code_cell = {'cell_type': 'code',
                    'execution_count': 7,
                    'metadata': {},
                    'outputs': [],
                    'source': ['load_dotenv()\n',
                    'key = os.getenv("OPENAI_API_KEY")\n',
                    '\n',
                    '# Usage example:\n',
                    '\n',
                    'conv = Conversation(key, "Be a student working on computer-assisted math homework", "Be a tutor helping with computer-assisted math homework")\n',
                    '\n',
                    '# conv.pose_question("What is the Pythagorean theorem?", n=1)']
                }
        self.notebook.add_cell(code_cell)

    def md(self):
        md_cell = {'cell_type': 'markdown', 'metadata': {}, 'source': [self.agent1.dump()]}
        self.notebook.add_cell(md_cell)
    
    def __str__(self):
        return str(self.agent1) + " conversing with " + str(self.agent2)