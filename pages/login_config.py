import time
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit_authenticator as stauth


# 定义用户到图标的映射
user_icon_mapping = {
    "chen": {"col": "green-badge", "ro": "🦖"},
    "luo": {"col": "red-badge", "ro": "🐉"},
    "hx": {"col": "yellow-badge", "ro": "🦄"},    
    "yl": {"col": "yellow-badge", "ro": "🦊"},    

}

# @st.dialog("登录拦截",width="large")
def login_right():
    config = {
        'credentials': {
            'usernames': {
                'chen': { #用户
                    'name': 'chen',
                    'password': stauth.Hasher().hash('123#asdfghjkl')
                },
                'luo': { #用户
                    'name': 'luo',
                    'password': stauth.Hasher().hash('123#asdfghjkl')
                },
                'hx': { #管理员
                    'name': 'hx',
                    'password': stauth.Hasher().hash('123#asdfghjkl')
                },
                'yl': { #用户
                    'name': 'yl',
                    'password': stauth.Hasher().hash('123#asdfghjkl')
                },
            }
        },
        'cookie': {
            'expiry_days': '30',
            'key': 'your_secret_key'
        }
    }

    # 初始化认证器
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    # 1. 调用 login（无返回值）
    try:
        authenticator.login(location='main')
    except Exception as e:
        del st.session_state.authentication_status
    # 2. 通过 st.session_state 判断是否登录
    if st.session_state["authentication_status"]:
        # st.success(f'欢迎回来，{st.session_state["name"]}！')
        authenticator.logout(button_name='退出', location='sidebar')
        return st.session_state["name"]
    elif st.session_state["authentication_status"] is False:
        st.error('用户名或密码错误')
        return False
    elif st.session_state["authentication_status"] is None:
        st.warning('请输入用户名和密码')
        return False
    else:
        st.warning('请输入用户名和密码')
        return st.stop()

def meau():
    # print(st.session_state)
    if 'name' not in st.session_state:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
            st.rerun()
    elif st.session_state["name"] is None:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
            st.rerun()
    try:
        user_name = st.session_state["name"]
    except:
        login_right()
    return user_name

