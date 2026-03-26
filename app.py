import streamlit as st
import pandas as pd
import joblib

# 页面配置
st.set_page_config(page_title="电信流失预警系统", page_icon="📞")

@st.cache_resource
def load_model():
    return joblib.load("telco_churn_pipeline.pkl")

model = load_model()

st.title("📞 电信客户流失预警系统")
st.markdown("通过输入客户特征，基于机器学习 Pipeline 实时预测下个月的流失概率。")

# 侧边栏输入
st.sidebar.header("输入客户特征")
tenure = st.sidebar.slider("入网时长 (月)", 0, 72, 12)
contract = st.sidebar.selectbox("合同类型", ["Month-to-month", "One year", "Two year"])
internet = st.sidebar.selectbox("网络服务", ["DSL", "Fiber optic", "No"])
monthly_charges = st.sidebar.number_input("月租费 ($)", 10.0, 150.0, 50.0)
total_charges = tenure * monthly_charges

if st.sidebar.button("🔮 开始预测"):
    # 组装数据 (Pipeline会自动处理缺失的其他特征的填充)
    input_data = pd.DataFrame({
        'tenure': [tenure], 'Contract': [contract],
        'InternetService': [internet], 'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        # 补齐必填兜底数据
        'gender': ['Male'], 'SeniorCitizen': [0], 'Partner': ['No'], 'Dependents': ['No'],
        'PhoneService': ['Yes'], 'MultipleLines': ['No'], 'OnlineSecurity': ['No'],
        'OnlineBackup': ['No'], 'DeviceProtection': ['No'], 'TechSupport': ['No'],
        'StreamingTV': ['No'], 'StreamingMovies': ['No'], 'PaperlessBilling': ['Yes'],
        'PaymentMethod': ['Electronic check']
    })
    
    prob = model.predict_proba(input_data)[0][1]
    
    st.subheader("预测结果")
    if prob > 0.5:
        st.error(f"⚠️ 高风险客户！流失概率达 **{prob:.1%}**。建议立刻发放优惠券挽留。")
    else:
        st.success(f"✅ 安全客户。流失概率仅为 **{prob:.1%}**。")