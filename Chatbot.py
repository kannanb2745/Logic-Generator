from ai21 import AI21Client

from config import config

client = AI21Client(api_key=config["ApiKey"])


class Chatbot:
    "Chatbot Operations"

    def __init__(self, prompt):
        self.prompt = prompt
        Procedure_list_prompt = f"""
                    tell me the topic which i am trying to say like conditional \
                    what are method to slove are there  not to reply this\
                    its for refrence return me as signle list contain the necessary steps involved\
                    for the prompt of i am trying to implement an function for 
                    {self.prompt} 
                    which can be used in these case just give me in single list types
                    return in list in python not any additional words
        """
        Procedure_list = self.response_from_ai(Procedure_list_prompt)
        print(Procedure_list)

    def response_from_ai(self, prompt):
        "Genrate the response from the ai by the prompt"
        response = client.completion.create(
            model="j2-ultra",
            prompt=prompt,
            num_results=1,
            max_tokens=200,
            temperature=0.1,
        )
        return response.completions[0].data.text


user = Chatbot("logic for flames calculator")
