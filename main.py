
import streamlit as st
from datetime import datetime

# --- APP 設定 ---
st.set_page_config(
    page_title="Pi股宇宙",
    page_icon="🌌",
    layout="wide"
)

# --- Logo 選擇區塊 ---
st.sidebar.title("LOGO 模式選擇")
logo_mode = st.sidebar.radio("請選擇顯示 LOGO", ["🌌 靜態 LOGO", "✨ 動態 LOGO"])

if logo_mode == "🌌 靜態 LOGO":
    st.image("assets/logo_stardust.png", width=300)
else:
    st.image("assets/logo_stardust_slow.gif", width=300)

# --- 標題區 ---
st.title("🌟 Pi股宇宙")
st.markdown("讓 AI 幫你讀懂股市宇宙 🚀")

# --- 偵測使用時間 ---
now = datetime.now()
st.markdown(f"🕒 現在時間：{now.strftime('%Y-%m-%d %H:%M:%S')}")

# --- 股票代碼輸入 ---
stock = st.text_input("請輸入你想追蹤的股票代碼（如 AAPL、2330）", "")
if stock:
    st.success(f"你輸入的股票是：`{stock}`")

# --- 主題模式切換 ---
theme = st.radio("🎨 主題模式", ["日間模式", "夜間模式"], horizontal=True)
if theme == "日間模式":
    st.markdown("☀️ 使用莓紅＋粉色系")
else:
    st.markdown("🌙 使用科技藍＋暗星色系")

# --- 策略模擬 ---
st.header("🧠 策略模擬")
st.markdown("- RSI 金叉策略")
st.markdown("- MA20 趨勢策略")
st.markdown("- 策略觸發提示卡")

# --- 金句展示 ---
st.header("💬 今日金句")
st.info("“In investing, what is comfortable is rarely profitable.” — Robert Arnott (1951–)")

# --- 儲存說明 ---
st.markdown("📂 每週股市週報將儲存在 `/records/` 資料夾")
