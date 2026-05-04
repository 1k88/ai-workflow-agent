AI Workflow Agent

项目简介
一个基于多 Agent 协作的自动化任务执行系统，能够对用户输入任务进行解析、拆解、执行与评估，形成完整闭环。

核心功能
任务自动拆解（Planner Agent）
多步骤执行（Executor Agent）
结果质量评估（Evaluator Agent）
简单记忆模块（Memory）

工作流程
用户输入任务 → Agent解析 → 自动拆解 → 执行 → 评估 → 输出结果

使用方法
pip install -r requirements.txt python main.py
示例
输入：
帮我写一个AI项目申请方案
输出：
系统自动完成任务拆解 → 执行 → 评估

项目亮点
多 Agent 协作架构
自动化工作流闭环
显著提升任务执行效率
