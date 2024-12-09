import duckdb
import streamlit as st

# タイトルを出力
st.title("DuckDB test")

# バージョンを出力
st.write(f"DuckDB version: {duckdb.__version__}")

# Vectorを含むテーブルを作成
duckdb.query("CREATE OR REPLACE TABLE my_vector_table (i INTEGER, v FLOAT[3])")

# Vectorデータを挿入する
idx = 0
for x in range(11):
    for y in range(11):
        for z in range(11):
            duckdb.query(f"INSERT INTO my_vector_table VALUES ({idx}, [{x}, {y}, {z}])")
            idx += 1

# Vectorデータを取得する
result = duckdb.sql("SELECT * FROM my_vector_table").df()
st.dataframe(result)

# 類似度検索
x = st.slider("x", 0.0, 10.0, 5.0, step=0.1)
y = st.slider("y", 0.0, 10.0, 5.0, step=0.1)
z = st.slider("z", 0.0, 10.0, 5.0, step=0.1)
result = duckdb.sql(f"SELECT *, array_distance(v, [{x}, {y}, {z}]::FLOAT[3]) as d FROM my_vector_table ORDER BY d LIMIT 30").df()
st.dataframe(result)
