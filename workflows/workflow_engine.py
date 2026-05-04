from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.evaluator_agent import EvaluatorAgent
from tools.memory import save_memory

class WorkflowEngine:
    def __init__(self):
        self.planner = PlannerAgent("Planner")
        self.executor = ExecutorAgent("Executor")
        self.evaluator = EvaluatorAgent("Evaluator")

    def run(self, task):
        print("\n[1] 任务拆解中...")
        plan = self.planner.run(task)
        print(plan)

        print("\n[2] 执行任务中...")
        result = self.executor.run(plan)
        print(result)

        print("\n[3] 评估结果...")
        evaluation = self.evaluator.run(result)
        print(evaluation)

        save_memory(task, result)

        return result, evaluation
