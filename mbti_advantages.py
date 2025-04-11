import streamlit as st

st.set_page_config(page_title="MBTI 保研优势劣势测评", page_icon="🧠", layout="centered")

# 16种 MBTI 类型及其对应的描述
mbti_profiles = {
    "INTJ": {
        "advantage": "逻辑严密，目标导向，擅长科研规划，适合科研型方向。",
        "disadvantage": "社交略显被动，团队项目中需要主动沟通锻炼。"
    },
    "INTP": {
        "advantage": "分析能力强，思维跳跃，善于提出新观点，适合理论研究。",
        "disadvantage": "执行力稍弱，容易陷入过度分析，影响效率。"
    },
    "ENTJ": {
        "advantage": "领导力强，目标明确，擅长组织协调，是团队骨干力量。",
        "disadvantage": "有时过于强势，需注意团队合作中的共情。"
    },
    "ENTP": {
        "advantage": "思维灵活，创新能力强，适合跨学科项目或表达性方向。",
        "disadvantage": "可能缺乏细节耐心，科研项目中需注意持续性。"
    },
    "INFJ": {
        "advantage": "洞察力强，有理想主义色彩，擅长深度研究与辅导他人。",
        "disadvantage": "内耗较强，需管理情绪压力以提升稳定性。"
    },
    "INFP": {
        "advantage": "理想主义驱动，有同理心，适合教育、心理等研究方向。",
        "disadvantage": "不擅长应试或高压环境，需训练表达与应变能力。"
    },
    "ENFJ": {
        "advantage": "极强的人际沟通力，擅长组织协调，适合公共事务与跨界研究。",
        "disadvantage": "可能过度在意他人看法，影响独立判断。"
    },
    "ENFP": {
        "advantage": "充满热情，表达力强，适合展示型研究与学术报告。",
        "disadvantage": "注意力分散，需提升聚焦与执行力。"
    },
    "ISTJ": {
        "advantage": "务实严谨，执行力强，适合结构化研究和规范流程项目。",
        "disadvantage": "创新性稍弱，需鼓励突破常规。"
    },
    "ISFJ": {
        "advantage": "踏实细腻，责任感强，适合资料整理与协作型科研。",
        "disadvantage": "不善表达观点，需加强展示与主导能力。"
    },
    "ESTJ": {
        "advantage": "组织性强，执行力高，适合带领团队完成复杂任务。",
        "disadvantage": "可能忽视情绪细节，需提升人际敏感度。"
    },
    "ESFJ": {
        "advantage": "乐于助人，沟通力强，擅长协作项目与公共关系方向。",
        "disadvantage": "容易受情绪影响，需加强自我节奏控制。"
    },
    "ISTP": {
        "advantage": "动手能力强，逻辑清晰，适合实验型科研或工程方向。",
        "disadvantage": "不喜规章，需适应学术系统性要求。"
    },
    "ISFP": {
        "advantage": "温和包容，感知力敏锐，适合人文社科领域研究。",
        "disadvantage": "不喜竞争，需提升目标感与自我驱动。"
    },
    "ESTP": {
        "advantage": "反应快，行动力强，适合突发任务或实践性项目。",
        "disadvantage": "学术深度略弱，需加强理论基础。"
    },
    "ESFP": {
        "advantage": "活泼热情，擅长表达与交际，适合面试和展示型项目。",
        "disadvantage": "注意力难集中，需控制干扰与自律。"
    }
}

# 🎨 页面内容
st.title("🧠 MBTI 保研优势劣势测评")
st.markdown("输入你的 MBTI 类型，看看在保研过程中的优势与挑战👇")

# 下拉菜单选择 MBTI
selected_mbti = st.selectbox("选择你的 MBTI 类型", list(mbti_profiles.keys()))

if selected_mbti:
    st.subheader(f"你选择的是：**{selected_mbti}**")
    st.success(f"🌟 优势：{mbti_profiles[selected_mbti]['advantage']}")
    st.error(f"⚠️ 劣势：{mbti_profiles[selected_mbti]['disadvantage']}")

# 👣 底部说明
st.markdown("---")
st.caption("本工具为非正式性格参考，仅供保研自我分析使用 😊")
