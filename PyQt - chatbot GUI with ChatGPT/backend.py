from openai import OpenAI

client = OpenAI(api_key="sk-None-13N7OzHP3u8vNC9TPRdZT3BlbkFJo27Nivzzr4YFV27OP4m5")


class Chatbot:
    def __init__(self, api_key):
        client.api_key = api_key
    def get_response(self, user_input):
        response = client.completions.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot(client.api_key)


