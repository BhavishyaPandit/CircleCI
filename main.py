knowledge_base = {
    "langchain": "LangChain simplifies LLM application development.",
    "rag": "RAG improves LLM accuracy by grounding them in external data.",
    "faiss": "FAISS is an efficient library for similarity search.",
    "openai": "OpenAI provides powerful language models."
}

def retrieve_facts(keywords):
    """
    Retrieves facts from the knowledge base based on keywords.

    Args:
        keywords: A list of keywords (strings).

    Returns:
        A list of relevant facts (strings). Returns an empty list if no facts are found.
    """

    retrieved_facts = []
    for keyword in keywords:
        fact = knowledge_base.get(keyword.lower()) # Case-insensitive matching
        if fact:
            retrieved_facts.append(fact)
    return retrieved_facts