from agents.base_agent import BaseAgent
from tools.llm import call_llm

class ExecutorAgent(BaseAgent):
    def run(self, plan):
        prompt = f"""
根据以下任务步骤，执行任务并给出完整结果：

步骤：
{plan}
"""
        return call_llm(prompt)
