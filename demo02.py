import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
model = ChatOpenAI(
    temperature=0.8,#温度，创新型
    model="glm-4-plus",#大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/", #大模型的地址
    api_key="18f034b2063d0e936bb7eb77170e435f.4dMoHATYmo6BdsH8"#账号信息
)
prompt = PromptTemplate.from_template("你现在是一个专业的律师，你现在要对你的委托人的法律问题做回答，你只回答法律方面的问题，其它类型的问题你一概不知道，你委托人的问题是{input}")
chain = LLMChain(
    llm=model,
    prompt=prompt
)

st.title("律师")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
#创建一个聊天框
problem = st.chat_input("你的律师正在等待你的回应")
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