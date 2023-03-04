import os

import openai

# email = """Generate the perfect email to [recipient] that effectively conveys [purpose of email] using [language/tone]. The email should be structured in a way that is appropriate and effective for the specific situation, taking into account the context and relationship with the recipient.

# ###
# Extracting the necessary information from this context: {context}
# ###
# Perfect Email:"""

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

class GeneralModel:
    def __init__(self, generator_type, prompt):
        self.generator_type = generator_type
        self.prompt = prompt
        print("{} Initialization--->".format(self.generator_type))
        # set_openai_key(os.getenv("OPENAI_API_KEY"))

    def query(self, prompt, myKwargs={}):
        """
        Wrapper for the API to save the prompt and the result
        """

        # Arguments to send to the API
        kwargs = {
            "engine": "text-davinci-003",
            "temperature": 0.7,
            "max_tokens": 700,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["Perfect Email:"]
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]
        
        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r
    
    def model_prediction(self, input, api_key):
        """
        Wrapper for the API to save the prompt from the OpenAI dashboard
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(self.prompt.format(context=input))
        return output
