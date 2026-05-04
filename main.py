from workflows.workflow_engine import WorkflowEngine

def main():
    engine = WorkflowEngine()

    while True:
        task = input("\n请输入任务（输入 exit 退出）：")
        if task.lower() == "exit":
            break

        engine.run(task)

if __name__ == "__main__":
    main()
