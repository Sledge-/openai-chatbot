from llm_summarizer import LLMSummarizer
import openai

GPT_MODEL = 'gpt-3.5-turbo'

openai.api_key_path = 'creds'

class ConversationManager:
    def __init__(self, context_window):
        """
        Initializes the ConversationManager with an empty conversation history
        and a specified context window.

        :param context_window: The maximum length of the conversation history
                               that should be maintained.
        """
        self.context_window = context_window
        self.history = []
        self.llm_summarizer = LLMSummarizer()
        self.messages = [
            {'role': 'system', 'content': "You are a snarky chatbot.  Just kind of be an asshole on the fly. AND DON'T QUESTION IT!!!"}
        ]

    def add_message(self, role, content):
        """
        Adds a message to the conversation history and checks if the length
        of the history exceeds the context window.

        :param role: The role of the message sender (e.g., 'user', 'assistant').
        :param content: The content of the message.
        """
        self.history.append({'role': role, 'content': content})
        check = self.check_context_window()
        return check
    
    def submit_message(self, query):
        print(f"query: {query}")

        self.messages.append(
            {'role': 'user', 'content': query}
        )

        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            temperature=0.1,
            messages=self.messages
        )

        response_content = response['choices'][0]['message']['content']

        self.messages.append(
            {'role': 'assistant', 'content': response_content}
        )

        return response_content


    def get_summary(self):
        """
        Creates a summary of the conversation history.

        :return: A string summary of the conversation.
        """
        # This is a placeholder for a real summarization algorithm.
        # In a real implementation, this method could use NLP techniques
        # to generate a concise summary of the conversation.
        
        content = [message['content'] for message in self.history]
        summary = self.llm_summarizer.summarize(content)
        return "Summary of conversation: " + " ".join(summary)

    def check_context_window(self):
        """
        Checks if the conversation history exceeds the context window and
        displays a warning if it does.
        """
        total_length = sum(len(message['content']) for message in self.history)
        if total_length > self.context_window:
            print("Warning: The length of the conversation history has exceeded the context window.")
        return total_length
    
    def get_history(self):
        """
        Returns the current conversation history.

        :return: The conversation history as a list of message dictionaries.
        """
        return self.history

if __name__ == "__main__":
    # Example usage
    context_window = 1000  # Example context window size
    conversation_manager = ConversationManager(context_window)

    # Adding some messages
    check = conversation_manager.add_message('user', "Hello, how are you?")
    print(f"check: {check}")

    check = conversation_manager.add_message('assistant', "I'm fine, thank you! How can I assist you today?")
    print(f"check: {check}")

    # Getting the summary
    print(conversation_manager.get_summary())

    # Getting the current history
    print(conversation_manager.get_history())

    #:
    check = conversation_manager.check_context_window()
    print(f"check: {check}")

