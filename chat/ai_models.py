from groq import Groq


class AIModelManager:
    def __init__(self):
        self.client = Groq()
        self.default_model = "llama3-8b-8192"

    def get_chat_completion(self, messages, stream=True, model=None, preferences=None):
        try:
            # Optionally modify messages based on preferences
            if preferences:
                messages.insert(0, {"role": "system", "content": preferences})
            return self.client.chat.completions.create(
                model=model or self.default_model,
                messages=messages,
                temperature=0.7,
                top_p=1,
                stream=stream,
            )
        except Exception as e:
            raise AIModelException(f"Error getting completion: {str(e)}")


    def generate_title(self, conversation):
        try:
            title_prompt = f"{conversation}\n\nBased on this conversation, generate a very short title (5 words or less)."
            completion = self.get_chat_completion(
                messages=[{"role": "user", "content": title_prompt}],
                stream=False,
                max_tokens=20
            )
            return completion.choices[0].message.content.strip().strip('"')
        except Exception as e:
            raise AIModelException(f"Error generating title: {str(e)}")


class AIModelException(Exception):
    pass
