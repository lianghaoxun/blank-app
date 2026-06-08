from pages.login_config import login_right, meau
import streamlit as st
# 1️⃣ 页面基础配置

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
def app_main():
    # 2️⃣ 侧边栏导航（保持不变）
    meau()
    # 3️⃣ Hero 横幅（CSS 背景渐变）
    st.markdown(
        """
        <style>
        .hero {
            padding: 100px 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 40px;
        }
        .hero h1 {
            font-size: 3rem;
            margin: 0;
        }
        .hero p {
            font-size: 1.2rem;
            margin-top: 8px;
        }
        </style>
        <div class="hero">
          <h1>欢迎登录！ 私人综合处理</h1>
          <p>一键洞察数据 · 让决策更简单</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 4️⃣ 三列卡片布局
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style="
                background:#f4f6f8;
                padding:24px;
                border-radius:12px;
                height:220px;
            ">
            <h3 style="color:#000;" >🚀 快速开始</h3>
            <ul style="color:#000;">
              <li><a href="/#">工作处理</a> </li>
              <li><a href="/#">报表统计</a></li>
              <li><a href="/#">周报管理</a>点击「运行」</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="
                background:#f4f6f8;
                padding:24px;
                border-radius:12px;
                height:220px;
            ">
            <h3 style="color:#000;">📖 使用指引</h3>
            <p style="color:#000;">
            1. 没什么好指引的<br/>
            2. 玩去吧<br/>
               3. 所有图表支持交互</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style="
                background:#f4f6f8;
                padding:24px;
                border-radius:12px;
                height:220px;
            ">
            <h3 style="color:#000;" >💬 联系我们</h3>
            <p style="color:#000;">如遇问题，别找我<br/>
               <a href="mailto:help@company.com">这不是我的邮箱@buswo.com</a><br/>
               或企业微信反馈(没有)。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # 5️⃣ 可选：底部 Footer
    st.markdown(
        """
        <hr style="margin-top:60px">
        <div style="text-align:center;color:#888;font-size:0.9rem;">
          © 2026 hx 的私人综合处理. 保留所有权利.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("内网 IP：", st.context.ip_address)
    st.write("")
    
app_main()

