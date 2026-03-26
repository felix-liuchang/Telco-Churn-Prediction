# 📞 Telco Customer Churn Prediction & MLOps Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![uv](https://img.shields.io/badge/Package_Manager-uv-purple)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-success)

## 📖 项目简介 (Project Overview)
本项目旨在解决电信行业的经典商业痛点：**客户流失预警**。
通过构建端到端的机器学习工程流水线（MLOps），实现从原始数据清洗、特征工程、模型自动调参，到前端 Web 应用交互与 CI/CD 自动化测试的全栈落地。

## 🚀 核心技术与工程亮点 (Engineering Highlights)
1. **彻底杜绝数据泄露**：严格使用 `Scikit-Learn Pipeline` 封装 `SimpleImputer` 和 `OneHotEncoder`，隔离训练集与测试集的信息交叉。
2. **解决样本不平衡**：通过 `RandomizedSearchCV` 引入 `class_weight='balanced'`，配合 AUC 指标评估，显著提升了少数类（流失客户）的 Recall（召回率）。
3. **现代化依赖管理**：摒弃传统的 pip 体系，全面引入基于 Rust 的极速包管理器 **`uv`**，利用 `pyproject.toml` 和 `uv.lock` 实现毫秒级构建与跨平台环境 100% 复现。
4. **CI/CD 自动化**：集成 `GitHub Actions`，实现代码 Push 自动触发环境同步 (`uv sync`) 与模型拓扑结构健康度校验。

## 📊 核心商业洞察 (Business Insights)
基于逻辑回归模型提取的权重（Weights），定位出导致客户流失的三大核心诱因：
1. **光纤网络 (Fiber Optic)**：办理光纤的客户流失概率急剧增加，建议技术侧立刻排查网络稳定性。
2. **按月付费 (Month-to-month)**：缺乏长期绑定，建议运营侧加大“包年立减”活动的营销力度。
3. **入网时长 (Tenure)**：新客户极易流失，老客户极度忠诚。建议加强前 3 个月的新手期关怀。

## 💻 极速运行指南 (Quick Start)

本项目采用 `uv` 进行现代化管理，无需繁琐的虚拟环境配置。

**1. 克隆仓库**
```bash
git clone https://github.com/你的用户名/Telco-Churn-Prediction.git
cd Telco-Churn-Prediction
```
**2. 一键同步环境**
```bash
uv sync
```
**3. 启动交互式 Web 预警系统**
bash
uv run streamlit run app.py

# 📂 项目结构 (Repository Structure)
.
├── .github/workflows/ci.yml  # GitHub Actions 自动化测试脚本
├── app.py                    # Streamlit 前端交互代码
├── train_model.ipynb         # 核心算法研发、数据清洗与调参 Notebook
├── telco_churn_pipeline.pkl  # 序列化后的工业级 Pipeline 模型
├── pyproject.toml            # 现代化 Python 项目配置
├── uv.lock                   # 依赖绝对锁定文件 (保证复现)
└── README.md