import time
import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 获取用户输入
from pages.login_config import meau,user_icon_mapping
try:
    user_name = meau()
except:
    st.stop()


st.set_page_config(
    page_title="综合处理",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

csv_file = f"need_delete/chat_history.csv"
# 获取用户输入
prompt = st.chat_input("Say something")

if st.button("加载历史消息",use_container_width=True):
    st.session_state.loaded_rows += 1
index_1 = st.container()
index_2 = st.container()

@st.fragment(run_every="2s")
def release_the_balloons():
    # 初始化加载的行数
    if 'loaded_rows' not in st.session_state:
        st.session_state.loaded_rows = 5
    # st.balloons()
    # 检查文件是否存在
    if os.path.exists(csv_file):
        # 显示当前用户的聊天历史
        df = pd.read_csv(csv_file)
        last_rows = df.tail(st.session_state.loaded_rows)
        # placeholder = st.empty()  # 指定区域更新(区域也会随着从头到尾刷新...)
        # with placeholder.container(): # 指定区域更新(区域也会随着从头到尾刷新...)
        container = st.container()  # 指定区域更新(会增加)
        with container: # 指定区域更新(会增加)
            for time, user, role, message in last_rows[["时间", "用户", "角色", "消息"]].values.tolist():
                user_msg = user_icon_mapping.get(user, {"col":"green-badge"})
                user_icon = user_msg["col"]
                with st.chat_message(user_msg["ro"]):
                    # st.badge(user)
                    st.markdown(
                        f":{user_icon}[:material/star: {user}] :orange-badge[{time}]"
                    )
                    st.write(message)
with index_2:
    co1,co2 = st.columns([1,1])
    with co1:
        refresh_button = st.button("刷新加载信息", use_container_width=True,key="refresh_button", help="自动刷新页面")
    with co2:
        if st.button("清理界面",use_container_width=True):
            del st.session_state.loaded_rows



# 如果用户输入了内容
if prompt:
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 获取用户名称
    user_name = meau()
    # 将新的聊天记录追加到 CSV 文件中
    user_msg = user_icon_mapping.get(user_name, {"col": "green-badge"})

    new_record = pd.DataFrame([(current_time, user_name, user_msg["ro"], prompt)], columns=["时间", "用户", "角色", "消息"])

    # 检查文件是否存在
    if os.path.exists(csv_file):
        # 如果文件存在，直接追加新记录
        new_record.to_csv(csv_file, mode='a', header=False, index=False, encoding="utf-8")
        st.session_state.loaded_rows += 1
        # release_the_balloons()
    else:
        # 如果文件不存在，创建新文件并写入新记录
        new_record.to_csv(csv_file, mode='w', header=True, index=False, encoding="utf-8")
        st.session_state.loaded_rows += 1
        # release_the_balloons()

# 如果按钮被点击，重新运行脚本
if refresh_button:
    with index_1:
        release_the_balloons()
else:
    with index_1:
        release_the_balloons()

