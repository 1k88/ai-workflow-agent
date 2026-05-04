from agents.base_agent import BaseAgent
from tools.llm import call_llm

class PlannerAgent(BaseAgent):
    def run(self, task):
        prompt = f"""
你是一个任务拆解专家。
请把以下任务拆解为清晰的步骤（列表形式）：

任务：
{task}
"""
        return call_llm(prompt)
