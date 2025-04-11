import streamlit as st
from datetime import datetime

# --- APP 設定 ---
st.set_page_config(
    page_title="Pi股宇宙",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 標題區 ---
st.markdown("# 🌟 Pi股宇宙")
st.markdown("讓 AI 幫你讀懂股市宇宙 🚀")

# --- 偵測使用時間 ---
now = datetime.now()
st.markdown(f"🕒 現在時間：{now.strftime('%Y-%m-%d %H:%M:%S')}")

# --- 股票代碼輸入 ---
stock = st.text_input("請輸入你想追蹤的股票代碼（如 AAPL、2330）", "")
if stock:
    st.success(f"你輸入的股票是：`{stock}`")

# --- 主題切換 ---
theme = st.radio("🎨 選擇主題模式", ["日間模式", "夜間模式"], index=0, horizontal=True)
if theme == "日間模式":
    st.markdown("☀️ 目前為【日間模式】，使用莓紅 + 淺粉色系。")
else:
    st.markdown("🌙 目前為【夜間模式】，使用科技藍 + 星塵暗色系。")

# --- 預留策略模組區塊 ---
st.markdown("---")
st.subheader("🧠 策略模組將在完整版中啟用")
st.markdown("請期待 RSI 金叉、MA20 策略模擬與 Telegram 通知推播功能。")

# --- Footer ---
st.markdown("---")
st.caption("版本：Pi股宇宙 · 測試版｜由 pipiverse AI 金融設計")