import unittest
from main import retrieve_facts

class TestRagUtils(unittest.TestCase):

    def test_retrieve_existing_facts(self):
        keywords = ["langchain", "rag"]
        expected_facts = [
            "LangChain simplifies LLM application development.",
            "RAG improves LLM accuracy by grounding them in external data."
        ]
        self.assertEqual(retrieve_facts(keywords), expected_facts)

    def test_retrieve_nonexistent_facts(self):
        keywords = ["nonexistent_keyword"]
        self.assertEqual(retrieve_facts(keywords), [])

    def test_retrieve_mixed_facts(self):
        keywords = ["langchain", "nonexistent_keyword", "faiss"]
        expected_facts = [
            "LangChain simplifies LLM application development.",
            "FAISS is an efficient library for similarity search."
        ]
        self.assertEqual(retrieve_facts(keywords), expected_facts)

    def test_retrieve_empty_keywords(self):
        keywords = []
        self.assertEqual(retrieve_facts(keywords), [])

    def test_retrieve_case_insensitive(self):
        keywords = ["LangChain", "RAG"]  # Capitalized keywords
        expected_facts = [
            "LangChain simplifies LLM application development.",
            "RAG improves LLM accuracy by grounding them in external data."
        ]
        self.assertEqual(retrieve_facts(keywords), expected_facts)

if __name__ == '__main__':
    unittest.main()