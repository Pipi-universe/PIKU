import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Pi股宇宙", layout="wide")

st.title("🌟 Pi股宇宙 · 策略 v2.6")
st.caption("讓 AI 幫你讀懂股市宇宙 🚀")
st.write(f"🕒 現在時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

code = st.text_input("輸入股票代碼（如 AAPL、2330）")
if code:
    st.success(f"你輸入的股票是：{code}")

theme = st.radio("🎨 主題模式", ["日間模式", "夜間模式"], horizontal=True)
if theme == "日間模式":
    st.markdown("☀️ 使用莓紅 + 粉色系")
else:
    st.markdown("🌙 使用星塵藍 + 暗色系")

st.subheader("🧠 策略模擬")
st.markdown("""- RSI 金叉策略
- MA20 趨勢策略
- 策略觸發提示卡""")

st.subheader("💬 今日金句")
st.info("“In investing, what is comfortable is rarely profitable.” — Robert Arnott (1951–)")

st.markdown("---")
st.markdown("📤 每週股市週報將儲存在 `/records/` 資料夾")