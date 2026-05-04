from agents.base_agent import BaseAgent
from tools.llm import call_llm

class EvaluatorAgent(BaseAgent):
    def run(self, result):
        prompt = f"""
请评估以下结果质量（0-100分）并给出改进建议：

结果：
{result}
"""
        return call_llm(prompt)
