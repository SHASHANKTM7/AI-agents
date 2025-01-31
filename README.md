# Phi Data Agents
- Phi data is framework used for building AI agents. It will provide access to essential and fascinating tools and models to interact with.
-AI Agents are independent programs used to perform specific tasks.

## How Agents Work
- we can think of AI agents which has virtual arms and legs .here we can consider them as environment (databases or tools) and LLM as the brain.
- when AI Agents recieve input query it interacts with tools to get information with the help of model to produce response

## Agents Created And Worked On
1. **[Financial_Agent](https://github.com/SHASHANKTM7/AI-agents/blob/main/financial_agent_1.py)** an agent was created which is specialized in finance domain as it was having access to tools like yfinance and duckduckgo. it was a multi modal agent where i was interacting with 2 independent agents.
2. **[Python_Agent](https://github.com/SHASHANKTM7/AI-agents/blob/main/python_agent.py)**  an agent was created  which is used to provide python code along with steps when a query or problem is given.
3. **[Sports_Agent](https://github.com/SHASHANKTM7/AI-agents/blob/main/table_of_responses.py)** here also a multimodal agent was created which is used to generate a table of responses where each response where produced by independent agents.
esults of

## Results of Responses 
![Alt text]("https://github.com/SHASHANKTM7/AI-agents/blob/main/NVDA%20stock.png")

## Storage
- **Agent storage** :- will be able to store sessions and is better than built in memory as built in memory has some limitations (it needs the sessionID to be active to persist storage)
- **Agent memory** :- is used to classify and store user preferences . this will give better reponses to the user.

## Limitations
- **Multi-agent-dependencies** :- multi-agents sharing the same foundatinal model will share the same pitfalls. to work under normal conditions it is better to use different model for each agent.
- reasoning is good but there may be cases encountered where the agent is not able to do deal with the steps due to which the tools are called again and again and this might lead to loop which causes time consumption.
- building AI agents from scratch can be expensive , require more resources and leads to more time consumption.

## Overcoming Limitations 
- Developers can give access to users for **log of actions** . where each intermidiate step of what is being happpened is being controlled by user and describes about the error encounterd.
- to avoid  infinite loop we can go for **interuptability** where each sub task or action can be controlled and the looping caused by tools can be overcomed.
- it is better to go for human feedback to improve responses compared to agent feedback.

## Benifits
- Complex tasks are solved autonomusly
- multi modal agents work better because more plans of action is available and more learning and relflection occours.
- Agent provide responses that are more accurate and personalised responses.

## References and Documentation
- **[Phi Data Documentation]( https://docs.phidata.com/introduction)** 
- **[IBM Documentation](https://www.ibm.com/think/topics/ai-agents)** 
- **[AWS Documentation](https://aws.amazon.com/what-is/ai-agents/)**
 




 


