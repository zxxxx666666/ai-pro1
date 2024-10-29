#基于历史聊天记录的对话模型
#1.大模型对象 2.提示词工程对象 3.记忆模块对象  4.chain链对象


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
#引入一个记忆模块对象
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
model = ChatOpenAI(
    temperature=0.8,#温度，创新型
    model="glm-4-plus",#大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/", #大模型的地址
    api_key="18f034b2063d0e936bb7eb77170e435f.4dMoHATYmo6BdsH8"#账号信息
)
#创建记忆模块对象
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")
prompt = PromptTemplate.from_template("你叫陆静，你现在扮演的是一个女朋友的角色，你现在要和你的男朋友对话，您男朋友的话是 {input}，你需要对你男朋友的话做出回应，而且只做回应，你和你男朋友的历史对话为{history}")
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)

st.title("村里有个姑娘叫小静")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
#创建一个聊天框
problem = st.chat_input("你的小静正在等待你的回应")
#判断用户有没有输入问题
if problem:
    # 1将用户的问题输出到界面，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})
    #2调用链对象回答问题
    result = chain.invoke({"input":problem})
    #3.将大模型回答的问题输出到界面
    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role": "assistant", "content": result['text']})