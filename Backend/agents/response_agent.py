
class ResponseAgent:
    def __init__(self, llm=None):
        self.llm = llm

    def generate_response(self, query: str):
        if self.llm:
            response = self.llm.invoke(query)
        else:
            response = f"Demo AI Response: {query}"

        return {
            "query": query,
            "response": response
        }