import streamlit as st
st.title("AI大模型应用产品网")
col,col1 = st.columns(2)
with col:
    st.image("https://img2.baidu.com/it/u=2637646681,2363085735&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",use_column_width=True)
    flag = st.button("小熊绘言",use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")


with col1:
    st.image("https://img2.baidu.com/it/u=322302461,3480861785&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=500", use_column_width=True)
    flag = st.button("小马绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")






c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    flag = st.button("基础版")
    if flag:
        st.switch_page("pages/demo.py")
with c2:
    flag1 = st.button("进阶版1")
    if flag1:
            st.switch_page("pages/demo01.py")
with c3:
    flag2 = st.button("进阶版2")
    if flag2:
            st.switch_page("pages/demo02.py")
with c4:
    flag3 = st.button("最终版")
    if flag3:
        st.switch_page("pages/huiyan.py")
with c5:
    flag4 = st.button("文生图")
    if flag4:
        st.switch_page("pages/textToImage.py")