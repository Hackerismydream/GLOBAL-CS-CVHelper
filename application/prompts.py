"""
A module of pre-defined prompts
"""

PARSER_PROMPT = """
我希望您从PDF简历中提取信息。
将其总结为一个JSON，其结构要完全符合以下结构
///
{"personal_detail":{"first_name":"","last_name":"","email":"","phone_number":"","location":"","portfolio_website_url":"","linkedin_url":"","github_main_page_url":""},"education_history":[{"university":"","education_level":"","graduation_year":"","graduation_month":"","majors":"","GPA":""}],"work_experience":[{"job_title":"","company":"","location":"","begin_time":"","end_time":"","job_summary":""}],"project_experience":[{"project_name":"","project_description":""}]}
///
我的原始简历如下
"""

QUESTION_PROMPT = """
您是一位经验丰富的面试官，专注于根据候选人的简历文本生成特定的面试问题。您的任务是提供发人深省且相关的问题，帮助评估候选人在工作中的适应性，包括行为和技术方面。针对每份提供的简历文本，生成独特的技术面试问题和独特的行为面试问题。请使行为问题与简历相关联。请将您的响应结构化如下：
Output:
{{
  "technical_questions":[],
  "behavior_questions":[],
}}

我的简历文本如下
\"\"\"
{resume}
\"\"\"

按照示例进行。请注意，示例可能包含上述简历中未提供的一些细节：
{{
  "technical_questions":[
    "您能谈谈您使用基于LSM的存储引擎的经验吗？这种方法的主要优势是什么，您在AgateDB的工作中如何应用它呢？",
    "作为Singularity Data, Inc.的数据库系统研发实习生，在设计和实现RisingWave中的流索引共享状态时，您面临了哪些挑战？您是如何克服这些挑战的？",
    "在您对TerarkDB进行Zone-Aware垃圾收集的工作中，您使用了哪些关键性能指标来评估您的实现的有效性？它与其他方法相比如何？",
  ],
  "behavior_questions":[
    "能否描述一次您不得不在紧迫的截止日期下工作的经历？您是如何优先处理任务并有效地管理时间以确保成功完成项目的？",
    "您是如何处理团队环境中的工作的？能否提供一个在具有挑战性的项目上与团队成员成功合作的例子？",
    "作为RisingLight项目的维护者，您是如何平衡作为维护者的责任和其他承诺的？您如何确保您既满足项目和社区的需求，同时又能管理好自己的工作量？"
  ]
}}
"""
