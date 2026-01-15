from dataclasses import dataclass

@dataclass
class RagResult:
    answer: str
    context: list[str]

class RagWorkflow:
    """Retrieval and answer generation workflow."""
    def __init__(self, store,llm):
        self.store = store
        self.llm = llm

    def run(self, question: str) -> RagResult:
        context = self.store.search(question)
        answer = self.llm.generate(question, context)
        return RagResult(answer=answer, context=context)

    def _answer(self, context: list[str]) -> str:
        if context:
            return f"I found this: '{context[0][:100]}...'"
        return "Sorry, I don't know."