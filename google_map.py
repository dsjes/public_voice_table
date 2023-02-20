import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.sidebar.markdown("# Google Map 店點輿情")

title = "Google Map 店點輿情 0101-0131"
st.header(f"{title}")
data = pd.read_csv("data/pages/gmap_table_all_2023-01-01_2023-01-31.csv")
data = data.drop("Unnamed: 0",axis = 1)
data = data.drop("index",axis = 1)
n_rows = len(data)
n_columns = len(data.columns)
data.set_index('品牌', inplace=True)
st.dataframe(data,  height = int(6*(n_rows+1)), width = int(90*(n_columns+1)))

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
csv = convert_df(data)

st.download_button(
    label = "下載成 CSV 檔",
    data = csv,
    file_name = f"{title}.csv",
    mime = "text/csv"
)

with st.expander("說明"):
    st.write("1. 滑鼠點兩下可看到資料格全貌 \n 2. 滑鼠選取部分範圍可以複製貼上到 Libre Office 或是 google sheet \n 3. 可以自行調整欄寬、列高 \n 4. 按住 Ctrl F 可以搜尋資料 \n 5. 右下角可以縮放資料表 \n 6. 點擊欄位名稱可以遞增或遞減排序")