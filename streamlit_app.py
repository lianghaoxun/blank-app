import streamlit as st
from pages.login_config import login_right, meau

st.set_page_config(
    page_title="org", # 页面标题
    page_icon="📊",
    layout="wide", #
    initial_sidebar_state="expanded"
)
if login_right():
    pass
else:
    st.warning("请先登录")
    st.stop()

try:
    user_name = meau()
except:
    # 使用CSS隐藏原生侧边栏导航标题（但保留侧边栏）
    hide_nav_title = """
    <style>
        /* 隐藏侧边栏中的页面路径标题 */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* 隐藏页面路径，但保留侧边栏容器 */
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:first-child {
            display: none;
        }
    </style>
    """
    st.markdown(hide_nav_title, unsafe_allow_html=True)
    st.stop()

from datetime import datetime
pages = [
    ("管理员", '聊天群组', st.Page("pages/main.py", title="💬 聊天页面", icon=":material/chat:")),
]
# 管理员用户
manage_user = ["chen","luo","hx"]
# 测试用户
test_user = ["cy_test02"]
# 财务用户
finance_user = ["cy_test03"]

create_page = {"聊天群组":[]}
for user_pa, user_how,usr_st in pages:
    if user_pa not in ["隐藏"]:
        if  user_name in manage_user:
            create_page[user_how].append(usr_st)
        else:
            if user_name in test_user:
                if user_pa in ["用户"]:
                    create_page[user_how].append(usr_st)
            elif user_name in finance_user:
                if user_pa in ["财务"]:
                    create_page[user_how].append(usr_st)


print("当前用户:", user_name, "身份", "管理员" if user_name in manage_user else "用户" if user_name in test_user else "财务", "当前时间:", datetime.now())
st.session_state["create_page"] = create_page
base_bir =  {
    "🏠 首页": [st.Page("pages/main_home.py", title=f"{user_name}", icon=":material/home:")],
    }
for i,v in create_page.items():
    base_bir[i] = v

pg = st.navigation(
        base_bir
)

pg.run()
