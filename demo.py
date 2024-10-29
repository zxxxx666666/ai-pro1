#制作一个聊天界面
#解决聊天界面不能渲染以往旧对话信息
import streamlit as st
#langchain 调用大模型，导入langchain的代码
from langchain_openai import ChatOpenAI

#构建一个大模型 --智谱公司提供的大模型
model = ChatOpenAI(
    temperature=0.8,#温度，创新型
    model="glm-4-plus",#大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/", #大模型的地址
    api_key="18f034b2063d0e936bb7eb77170e435f.4dMoHATYmo6BdsH8"#账号信息
)
st.title("AI demo小程序👏👏👏👏👏")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])



#创建一个聊天框
problem = st.chat_input("请输入你的问题")
#判断用户有没有输入问题
if problem:
    # 1将用户的问题输出到界面，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})

    #2调用大模型回答问题
    result = model.invoke(problem)
    #3.将大模型回答的问题输出到界面
    with st.chat_message("assistant"):
        st.write(result.content)
    st.session_state.cache.append({"role": "assistant", "content": result.content})