from conversational_rag_chain import ConversationalRAGChain
from retriever_chain import RetrieverChain


class ChatBot:
    @staticmethod
    def get_response(user_input, vector_store, chat_history):
        retriever_chain = RetrieverChain.get_context_retriever_chain(vector_store)
        conversation_rag_chain = ConversationalRAGChain.get_conversational_rag_chain(
            retriever_chain
        )
        response = conversation_rag_chain.invoke(
            {"chat_history": chat_history, "input": user_input}
        )
        return response["answer"]
