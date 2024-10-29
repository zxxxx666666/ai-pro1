#文生图大模型应用
import streamlit as st
from zhipuai import ZhipuAI
model = ZhipuAI(api_key='18f034b2063d0e936bb7eb77170e435f.4dMoHATYmo6BdsH8')
st.title("设计大王")

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role'] == 'user':
            with st.chat_message(message['role']):
                st.write(message["content"])
        else:
            with st.chat_message(message['role']):
                st.image(message["content"],width=300)


#创建输入框
desc = st.chat_input("请输入图片的描述")
if desc:
    #将用户输入的内容以用户角色输出到界面上
    with st.chat_message("user"):
        st.write(desc)
    st.session_state.cache.append({"role":"user","content":desc})
    #调用智谱ai的文生图大模型生成图片
    response = model.images.generations(
        model="cogview-3-plus",  # 填写需要调用的模型编码
        prompt=desc,
    )
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=100)
    st.session_state.cache.append({"role": "assistant", "content": response.data[0].url})
