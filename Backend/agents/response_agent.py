
class ResponseAgent:
    def __init__(self, llm):
        self.llm = llm

    def generate_response(self, query: str):
        """
        Generate AI response for the user's query.
        """

        response = self.llm.invoke(query)

        return {
            "query": query,
            "response": response
        }