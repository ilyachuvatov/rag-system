from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


class ConversationalRAGChain:
    @staticmethod
    def get_conversational_rag_chain(retriever_chain):
        llm = ChatOpenAI()
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "Give a short answer based on the context:\n\n{context}"),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
            ]
        )
        stuff_documents_chain = create_stuff_documents_chain(llm, prompt)
        return create_retrieval_chain(retriever_chain, stuff_documents_chain)
