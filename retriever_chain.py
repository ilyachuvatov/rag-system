from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import create_history_aware_retriever


class RetrieverChain:
    @staticmethod
    def get_context_retriever_chain(vector_store):
        llm = ChatOpenAI()
        retriever = vector_store.as_retriever()
        prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
                (
                    "user",
                    "Generate a search query to look up information relevant to the conversation",
                ),
            ]
        )
        return create_history_aware_retriever(llm, retriever, prompt)
