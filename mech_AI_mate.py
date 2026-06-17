import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import random

# ========== 页面配置 ==========
st.set_page_config(page_title="材料力学交互式学习系统", layout="wide", page_icon="📐")

# ========== 中文支持辅助函数 ==========
def set_chinese_font(fig):
    """为图表设置中文字体"""
    fig.update_layout(
        font=dict(family="SimHei, Microsoft YaHei, Arial Unicode MS, sans-serif")
    )
    return fig

# ========== 侧边栏导航 ==========
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/mechanical-engineering.png", width=80)
    st.title("📚 材料力学")
    st.markdown("**交互式学习系统 v2.0**")
    st.markdown("---")
    
    module = st.radio(
        "选择知识模块",
        ["🏠 课程首页",
         "📖 理论知识体系",
         "📊 应力与应变分析",
         "🔄 基本变形动画",
         "📈 剪力图与弯矩图",
         "🎨 应力云图交互",
         "🧪 虚拟实验",
         "📝 知识测验",
         "🏗️ 综合工程案例"]
    )
    st.markdown("---")
    st.caption("💡 拖动滑块、点击按钮，探索材料力学的奥秘！")

# ============================================================
# 1. 课程首页
# ============================================================
if module == "🏠 课程首页":
    st.title("📐 材料力学")
    st.subheader("交互式智能学习系统 v2.0")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📖 知识模块", "9 大板块", "从理论到实践")
    with col2:
        st.metric("🎨 可视化", "实时交互", "3D 应力云图")
    with col3:
        st.metric("🧪 虚拟实验", "6 项实验", "动手实践")
    with col4:
        st.metric("🏗️ 工程案例", "实战应用", "综合设计")
    
    st.markdown("---")
    st.markdown("""
    ### 🎯 学习路径
    """)
    cols = st.columns(5)
    with cols[0]:
        st.markdown("**1️⃣ 理论**\n\n掌握基本概念")
    with cols[1]:
        st.markdown("**2️⃣ 可视化**\n\n观察应力应变")
    with cols[2]:
        st.markdown("**3️⃣ 动画**\n\n理解变形过程")
    with cols[3]:
        st.markdown("**4️⃣ 实验**\n\n动手操作")
    with cols[4]:
        st.markdown("**5️⃣ 应用**\n\n解决工程问题")
    
    st.markdown("---")
    st.markdown("""
    ### 🚀 快速开始
    左侧菜单选择模块，开始你的学习之旅！
    
    ### 📌 课程简介
    材料力学是研究构件在外力作用下的**变形、应力、应变及破坏规律**的学科，
    是机械、土木、航空等工程专业的重要基础课。
    """)
    
    if st.button("🎬 播放欢迎动画"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
            if i < 30:
                status_text.text("🚀 加载课程资源...")
            elif i < 60:
                status_text.text("📚 准备知识库...")
            elif i < 90:
                status_text.text("🎨 渲染可视化组件...")
            else:
                status_text.text("✅ 准备就绪！")
        status_text.text("✅ 欢迎来到材料力学世界！开始探索吧！")
        st.balloons()

# ============================================================
# 2. 理论知识体系
# ============================================================
elif module == "📖 理论知识体系":
    st.title("📖 材料力学理论知识体系")
    
    st.markdown("### 🧠 知识图谱")
    st.graphviz_chart('''
    digraph {
        "材料力学" -> "基本概念"
        "材料力学" -> "基本变形"
        "材料力学" -> "组合变形"
        "材料力学" -> "压杆稳定"
        "基本概念" -> "应力"
        "基本概念" -> "应变"
        "基本概念" -> "胡克定律"
        "基本变形" -> "轴向拉压"
        "基本变形" -> "扭转"
        "基本变形" -> "弯曲"
        "组合变形" -> "拉弯组合"
        "组合变形" -> "弯扭组合"
        "组合变形" -> "强度理论"
        "压杆稳定" -> "欧拉公式"
        "压杆稳定" -> "长细比"
        "压杆稳定" -> "临界应力"
    }
    ''')
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📌 基本概念", "📐 基本变形", "⚙️ 组合变形", "📏 压杆稳定", "🔗 材料性能"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### 材料力学的研究任务
            研究构件在**外力作用下的变形、应力、应变及破坏规律**，为工程设计提供理论基础。
            
            ### 基本假设
            - **连续性假设**：材料内部连续无空隙
            - **均匀性假设**：材料各处力学性能相同
            - **各向同性假设**：材料在各个方向性能相同
            - **小变形假设**：变形远小于构件尺寸
            - **线弹性假设**：应力与应变呈线性关系
            """)
        with col2:
            st.markdown("""
            ### 核心概念
            | 概念 | 定义 | 公式 |
            |------|------|------|
            | **应力** | 单位面积上的内力 | $\\sigma = \\frac{F}{A}$ |
            | **应变** | 单位长度的变形量 | $\\varepsilon = \\frac{\\Delta L}{L}$ |
            | **弹性模量** | 应力与应变之比 | $E = \\frac{\\sigma}{\\varepsilon}$ |
            | **泊松比** | 横向与纵向应变比 | $\\nu = -\\frac{\\varepsilon_y}{\\varepsilon_x}$ |
            | **切应力** | 单位面积上的切向力 | $\\tau = \\frac{F_s}{A}$ |
            | **切应变** | 角度的改变量 | $\\gamma = \\frac{\\tau}{G}$ |
            """)
        st.latex(r"\text{胡克定律：} \sigma = E\varepsilon, \quad \tau = G\gamma")
    
    with tab2:
        st.markdown("""
        ### 三种基本变形
        
        #### 1. 轴向拉伸/压缩
        - 外力沿杆件轴线方向
        - 变形表现为长度变化
        - 关键公式：$\\Delta L = \\frac{FL}{EA}$
        - 强度条件：$\\sigma = \\frac{F}{A} \\leq [\\sigma]$
        
        #### 2. 扭转
        - 外力偶矩作用于杆件横截面
        - 变形表现为相对扭转角
        - 关键公式：$\\varphi = \\frac{TL}{GJ_p}$
        - 强度条件：$\\tau_{\\max} = \\frac{T}{W_p} \\leq [\\tau]$
        
        #### 3. 弯曲
        - 外力垂直于杆件轴线
        - 变形表现为挠曲线
        - 关键公式：$\\sigma = \\frac{My}{I}, \\quad w_{\\max} = \\frac{PL^3}{3EI}$
        - 强度条件：$\\sigma_{\\max} = \\frac{M_{\\max}}{W_z} \\leq [\\sigma]$
        """)
    
    with tab3:
        st.markdown("""
        ### 组合变形
        
        **组合变形**是指构件同时承受两种或以上基本变形的受力状态。
        
        #### 常见组合变形类型
        - **拉弯组合**（偏心拉伸/压缩）
        - **压弯组合**
        - **弯扭组合**
        
        #### 分析方法：**叠加原理**
        将组合变形分解为各基本变形，分别计算应力，然后叠加。
        
        #### 四大强度理论
        | 强度理论 | 适用条件 | 等效应力公式 |
        |----------|----------|--------------|
        | 第一（最大拉应力） | 脆性材料 | $\\sigma_{r1} = \\sigma_1$ |
        | 第二（最大拉应变） | 脆性材料 | $\\sigma_{r2} = \\sigma_1 - \\nu\\sigma_2$ |
        | 第三（最大切应力） | 塑性材料 | $\\sigma_{r3} = \\sigma_1 - \\sigma_3$ |
        | 第四（畸变能） | 塑性材料 | $\\sigma_{r4} = \\sqrt{\\frac{(\\sigma_1-\\sigma_2)^2+(\\sigma_2-\\sigma_3)^2+(\\sigma_3-\\sigma_1)^2}{2}}$ |
        """)
    
    with tab4:
        st.markdown("""
        ### 压杆稳定
        
        **压杆稳定**问题：细长杆在压力作用下可能突然弯曲失稳。
        
        #### 欧拉临界力公式
        $$P_{cr} = \\frac{\\pi^2 EI}{(\\mu L)^2}$$
        
        #### 长度系数 $\\mu$
        | 约束条件 | $\\mu$ | 临界力 |
        |----------|-------|--------|
        | 两端铰支 | 1.0 | $P_{cr} = \\pi^2 EI/L^2$ |
        | 一端固定一端自由 | 2.0 | $P_{cr} = \\pi^2 EI/(4L^2)$ |
        | 两端固定 | 0.5 | $P_{cr} = 4\\pi^2 EI/L^2$ |
        | 一端固定一端铰支 | 0.7 | $P_{cr} = 2.05\\pi^2 EI/L^2$ |
        
        #### 长细比 $\\lambda = \\frac{\\mu L}{i}$，$i = \\sqrt{\\frac{I}{A}}$
        - **大柔度杆**：$\\lambda \\geq \\lambda_p$，欧拉公式适用
        - **中柔度杆**：$\\lambda_s < \\lambda < \\lambda_p$，经验公式
        - **小柔度杆**：$\\lambda \\leq \\lambda_s$，强度问题
        """)
    
    with tab5:
        st.markdown("""
        ### 常用工程材料力学性能
        
        | 材料 | 弹性模量 E (GPa) | 屈服强度 σ_s (MPa) | 抗拉强度 σ_b (MPa) | 泊松比 ν |
        |------|------------------|--------------------|--------------------|----------|
        | Q235钢 | 200-210 | 235 | 375-500 | 0.25-0.30 |
        | 45钢 | 210 | 355 | 600 | 0.28 |
        | 铸铁 | 100-150 | - | 200-400 | 0.25 |
        | 铝合金 | 70 | 280 | 310 | 0.33 |
        | 铜 | 110 | 70 | 220 | 0.34 |
        | 钛合金 | 110 | 830 | 900 | 0.34 |
        """)

# ============================================================
# 3. 应力与应变分析
# ============================================================
elif module == "📊 应力与应变分析":
    st.title("📊 应力与应变分析")
    
    tab1, tab2 = st.tabs(["📉 莫尔圆", "📊 应力分量"])
    
    with tab1:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### 参数控制")
            sigma_x = st.slider("σ_x (MPa)", -150, 250, 100, 5, key="mx")
            sigma_y = st.slider("σ_y (MPa)", -100, 200, 50, 5, key="my")
            tau_xy = st.slider("τ_xy (MPa)", -80, 80, 30, 5, key="txy")
            
            avg = (sigma_x + sigma_y) / 2
            R = np.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
            sigma1 = avg + R
            sigma2 = avg - R
            tau_max = R
            
            st.markdown("---")
            st.markdown("### 📌 计算结果")
            c1, c2 = st.columns(2)
            with c1:
                st.metric("σ₁", f"{sigma1:.1f} MPa")
                st.metric("σ₂", f"{sigma2:.1f} MPa")
            with c2:
                st.metric("τ_max", f"{tau_max:.1f} MPa")
                st.metric("平均应力", f"{avg:.1f} MPa")
        
        with col2:
            theta = np.linspace(0, 2*np.pi, 200)
            circle_x = avg + R * np.cos(theta)
            circle_y = R * np.sin(theta)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=circle_x, y=circle_y, mode='lines', 
                                     name='莫尔圆', line=dict(color='blue', width=3)))
            fig.add_trace(go.Scatter(x=[sigma_x, sigma_y], y=[tau_xy, -tau_xy], 
                                     mode='markers', marker=dict(color='red', size=12),
                                     name='应力点'))
            fig.add_trace(go.Scatter(x=[sigma1, sigma2], y=[0, 0], mode='markers',
                                     marker=dict(color='green', size=16, symbol='star'),
                                     name='主应力'))
            fig.add_hline(y=0, line_dash="dash", line_color="gray")
            fig.add_vline(x=0, line_dash="dash", line_color="gray")
            fig.update_layout(
                title="莫尔圆 - 应力状态可视化",
                xaxis_title="正应力 σ (MPa)",
                yaxis_title="切应力 τ (MPa)",
                height=550,
                showlegend=True
            )
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### 空间应力状态")
        st.latex(r"\boldsymbol{\sigma} = \begin{bmatrix} \sigma_x & \tau_{xy} & \tau_{xz} \\ \tau_{yx} & \sigma_y & \tau_{yz} \\ \tau_{zx} & \tau_{zy} & \sigma_z \end{bmatrix}")
        
        stress_tensor = np.array([
            [100, 30, 10],
            [30, 50, 20],
            [10, 20, 70]
        ])
        fig = go.Figure(data=go.Heatmap(
            z=stress_tensor,
            x=["σx", "τxy", "τxz"],
            y=["σx", "τyx", "τzx"],
            text=[[f"{v:.0f}" for v in row] for row in stress_tensor],
            texttemplate="%{text}",
            textfont={"size": 16},
            colorscale='Viridis'
        ))
        fig.update_layout(title="应力张量分量", height=400)
        fig = set_chinese_font(fig)
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 4. 基本变形动画
# ============================================================
elif module == "🔄 基本变形动画":
    st.title("🔄 基本变形交互动画")
    
    deformation_type = st.selectbox("选择变形类型", ["轴向拉伸", "扭转", "弯曲"])
    
    if deformation_type == "轴向拉伸":
        st.markdown("### 🔩 轴向拉伸变形")
        col1, col2 = st.columns([1, 2])
        with col1:
            F = st.slider("拉力 F (N)", 0, 50000, 20000, 1000)
            A = st.slider("截面积 A (mm²)", 100, 1000, 314, 10)
            E = st.slider("弹性模量 E (GPa)", 50, 250, 210, 10)
            sigma = F / (A * 1e-6)
            eps = sigma / (E * 1e9)
            delta = eps * 100
            st.metric("正应力 σ", f"{sigma/1e6:.2f} MPa")
            st.metric("应变 ε", f"{eps:.6f}")
        
        with col2:
            L0 = 100
            x = np.array([0, L0])
            x_def = np.array([0, L0 + delta])
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=[0,0], mode='lines+markers', 
                                     name='原始', line=dict(color='blue', dash='dot', width=4)))
            fig.add_trace(go.Scatter(x=x_def, y=[0,0], mode='lines+markers',
                                     name='变形', line=dict(color='red', width=6)))
            fig.update_layout(title="轴向拉伸变形动画", xaxis_title="长度", yaxis_title="",
                              height=400, showlegend=True)
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)
    
    elif deformation_type == "扭转":
        st.markdown("### 🔧 扭转变形")
        col1, col2 = st.columns([1, 2])
        with col1:
            T = st.slider("扭矩 T (N·m)", 0, 5000, 2000, 100)
            d = st.slider("直径 d (mm)", 20, 100, 50, 5)
            tau_max = 16*T/(np.pi*(d/1000)**3)/1e6
            st.metric("最大切应力", f"{tau_max:.2f} MPa")
        
        with col2:
            r = np.linspace(0, d/2, 50)
            tau = tau_max * (r / (d/2))
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=r, y=tau, mode='lines', name='切应力分布',
                                     fill='tozeroy', line=dict(color='orange', width=4)))
            fig.update_layout(title="扭转切应力沿半径分布", 
                              xaxis_title="半径 r (mm)", yaxis_title="切应力 τ (MPa)",
                              height=400)
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)
    
    else:  # 弯曲
        st.markdown("### 📐 弯曲变形")
        col1, col2 = st.columns([1, 2])
        with col1:
            L = st.slider("梁长 L (m)", 0.5, 4.0, 2.0, 0.1)
            P = st.slider("集中力 P (N)", 0, 1000, 500, 10)
            b = st.slider("截面宽 b (mm)", 20, 100, 50, 5)
            h = st.slider("截面高 h (mm)", 20, 200, 100, 5)
            I = b * h**3 / 12
            E = 210e9
            w_max = P * L**3 / (3 * E * I * 1e-12)
            st.metric("最大挠度", f"{w_max:.2f} mm")
        
        with col2:
            x = np.linspace(0, L, 100)
            w = (P * x**2) / (6 * E * I * 1e-12) * (3*L - x) * 1000
            scale = 50 / max(w) if max(w) > 0 else 1
            w_vis = w * scale
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=np.zeros_like(x), mode='lines',
                                     name='原始', line=dict(color='blue', dash='dot', width=3)))
            fig.add_trace(go.Scatter(x=x, y=w_vis, mode='lines',
                                     name='挠曲线（放大）', line=dict(color='red', width=5)))
            fig.update_layout(title="悬臂梁挠曲线", xaxis_title="梁长 x (m)", 
                              yaxis_title="挠度 (放大)", height=400, showlegend=True)
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 5. 剪力图与弯矩图
# ============================================================
elif module == "📈 剪力图与弯矩图":
    st.title("📈 剪力图与弯矩图")
    
    load_type = st.selectbox("载荷类型", ["集中力", "均布载荷"])
    
    col1, col2 = st.columns([1, 2])
    with col1:
        L = st.slider("梁长 L (m)", 1.0, 6.0, 4.0, 0.5)
        if load_type == "集中力":
            P = st.slider("集中力 P (kN)", 1, 50, 20, 1)
            a = st.slider("力作用位置 a (m)", 0.5, L-0.5, 2.0, 0.5)
            R_A = P * (L - a) / L
            R_B = P * a / L
            x = np.linspace(0, L, 1000)
            Fs = np.zeros_like(x)
            M = np.zeros_like(x)
            for i, xi in enumerate(x):
                if xi < a:
                    Fs[i] = R_A
                    M[i] = R_A * xi
                else:
                    Fs[i] = -R_B
                    M[i] = R_B * (L - xi)
        else:
            q = st.slider("均布载荷 q (kN/m)", 1, 20, 10, 1)
            R_A = q * L / 2
            R_B = q * L / 2
            x = np.linspace(0, L, 1000)
            Fs = R_A - q * x
            M = R_A * x - q * x**2 / 2
        
        st.markdown("---")
        st.metric("支座反力 R_A", f"{R_A:.2f} kN")
        st.metric("支座反力 R_B", f"{R_B:.2f} kN")
    
    with col2:
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                            subplot_titles=("剪力图", "弯矩图"),
                            vertical_spacing=0.15)
        fig.add_trace(go.Scatter(x=x, y=Fs, mode='lines', name='剪力 V',
                                 line=dict(color='blue', width=3)), row=1, col=1)
        fig.add_hline(y=0, line_dash="dash", line_color="gray", row=1, col=1)
        fig.add_trace(go.Scatter(x=x, y=M, mode='lines', name='弯矩 M',
                                 line=dict(color='red', width=3)), row=2, col=1)
        fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)
        fig.update_xaxes(title_text="梁长 x (m)", row=2, col=1)
        fig.update_yaxes(title_text="剪力 (kN)", row=1, col=1)
        fig.update_yaxes(title_text="弯矩 (kN·m)", row=2, col=1)
        fig.update_layout(height=500, showlegend=True)
        fig = set_chinese_font(fig)
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 6. 应力云图交互
# ============================================================
elif module == "🎨 应力云图交互":
    st.title("🎨 交互式应力云图")
    
    section_type = st.selectbox("截面形状", ["矩形", "圆形"])
    
    col1, col2 = st.columns([1, 2])
    with col1:
        M = st.slider("弯矩 M (kN·m)", 0, 200, 80, 1)
        if section_type == "矩形":
            b = st.slider("截面宽 b (mm)", 20, 200, 80, 5)
            h = st.slider("截面高 h (mm)", 20, 300, 120, 5)
            I = b * h**3 / 12
            W = I / (h/2)
        else:
            d = st.slider("直径 d (mm)", 20, 200, 80, 5)
            I = np.pi * d**4 / 64
            W = np.pi * d**3 / 32
            b = d
            h = d
        sigma_max = M * 1000 / (W * 1e-9) / 1e6
        st.metric("最大正应力", f"{sigma_max:.2f} MPa")
    
    with col2:
        y = np.linspace(-h/2, h/2, 50)
        z = np.linspace(-b/2, b/2, 50)
        Y, Z = np.meshgrid(y, z)
        sigma = sigma_max * (Y / (h/2))
        
        fig = go.Figure(data=go.Heatmap(
            z=sigma, x=z, y=y,
            colorscale='RdYlBu_r', zmid=0,
            colorbar=dict(title="应力 (MPa)")
        ))
        fig.update_layout(title=f"{section_type}截面弯曲正应力云图",
                          xaxis_title="宽度方向 (mm)",
                          yaxis_title="高度方向 (mm)",
                          height=400)
        fig = set_chinese_font(fig)
        st.plotly_chart(fig, use_container_width=True)
        
        fig3d = go.Figure(data=go.Surface(
            z=sigma, x=z, y=y, colorscale='RdYlBu_r'
        ))
        fig3d.update_layout(title="3D 应力分布曲面",
                            scene=dict(xaxis_title="z (mm)", yaxis_title="y (mm)", zaxis_title="σ (MPa)"),
                            height=400)
        fig3d = set_chinese_font(fig3d)
        st.plotly_chart(fig3d, use_container_width=True)

# ============================================================
# 7. 虚拟实验
# ============================================================
elif module == "🧪 虚拟实验":
    st.title("🧪 虚拟实验")
    
    experiment = st.selectbox("选择实验", ["拉伸实验", "扭转实验", "弯曲实验"])
    
    if experiment == "拉伸实验":
        st.markdown("### 🔩 拉伸实验模拟")
        col1, col2 = st.columns([1, 2])
        with col1:
            material = st.selectbox("材料", ["低碳钢", "铸铁"])
            if material == "低碳钢":
                E = 210
                sigma_s = 235
                sigma_b = 400
                strain_max = 0.25
            else:
                E = 150
                sigma_s = None
                sigma_b = 250
                strain_max = 0.002
            strain_step = st.slider("应变加载", 0.0, strain_max, 0.0, 0.001)
            if sigma_s and strain_step <= sigma_s / E:
                sigma = E * strain_step * 1000
                stage = "弹性阶段"
            elif sigma_s:
                sigma = sigma_s * 1000
                stage = "屈服阶段"
            else:
                sigma = E * strain_step * 1000
                stage = "弹性阶段"
            st.metric("应力", f"{sigma/1000:.0f} MPa")
            st.metric("阶段", stage)
        
        with col2:
            eps_range = np.linspace(0, strain_max, 100)
            sigma_range = np.zeros_like(eps_range)
            for i, eps in enumerate(eps_range):
                if sigma_s and eps <= sigma_s / E:
                    sigma_range[i] = E * eps * 1000
                elif sigma_s:
                    sigma_range[i] = sigma_s * 1000 * (1 - (eps - sigma_s/E) / strain_max * 0.1)
                else:
                    sigma_range[i] = E * eps * 1000
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=eps_range*100, y=sigma_range/1000, mode='lines',
                                     name='应力-应变曲线', line=dict(color='blue', width=3)))
            fig.add_trace(go.Scatter(x=[strain_step*100], y=[sigma/1000], mode='markers',
                                     marker=dict(color='red', size=16), name='当前状态'))
            fig.update_layout(title="应力-应变曲线", xaxis_title="应变 ε (%)", 
                              yaxis_title="应力 σ (MPa)", height=400)
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)
    
    elif experiment == "扭转实验":
        st.markdown("### 🔧 扭转实验模拟")
        col1, col2 = st.columns([1, 2])
        with col1:
            d = st.slider("直径 d (mm)", 10, 50, 20, 5)
            T = st.slider("扭矩 T (N·m)", 0, 500, 100, 10)
            tau_max = 16*T/(np.pi*(d/1000)**3)/1e6
            st.metric("最大切应力", f"{tau_max:.2f} MPa")
        
        with col2:
            r = np.linspace(0, d/2, 50)
            tau = tau_max * (r / (d/2))
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=r, y=tau, mode='lines', name='切应力分布',
                                     fill='tozeroy', line=dict(color='orange', width=3)))
            fig.update_layout(title="切应力分布", xaxis_title="半径 (mm)", 
                              yaxis_title="切应力 (MPa)", height=400)
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)
    
    else:  # 弯曲实验
        st.markdown("### 📐 弯曲实验模拟")
        col1, col2 = st.columns([1, 2])
        with col1:
            L = st.slider("梁长 L (mm)", 100, 1000, 500, 50)
            b = st.slider("截面宽 b (mm)", 10, 50, 20, 5)
            h = st.slider("截面高 h (mm)", 10, 50, 30, 5)
            P = st.slider("集中力 P (N)", 0, 500, 100, 10)
            I = b * h**3 / 12
            sigma_max = P * L * (h/2) / I / 1e6
            w_max = P * L**3 / (3 * 210e3 * I) * 1000
            st.metric("最大正应力", f"{sigma_max:.2f} MPa")
            st.metric("最大挠度", f"{w_max:.2f} mm")
        
        with col2:
            x = np.linspace(0, L, 100)
            w = (P * x**2) / (6 * 210e3 * I) * (3*L - x) * 1000
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=w, mode='lines', name='挠曲线',
                                     line=dict(color='red', width=3), fill='tozeroy'))
            fig.update_layout(title="挠曲线", xaxis_title="梁长 (mm)", 
                              yaxis_title="挠度 (mm)", height=400)
            fig = set_chinese_font(fig)
            st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 8. 知识测验
# ============================================================
elif module == "📝 知识测验":
    st.title("📝 知识测验")
    
    questions = [
        {"question": "材料力学中，应力σ的定义是什么？", 
         "options": ["单位面积上的内力", "单位长度上的变形", "外力与内力的比值"], "answer": 0},
        {"question": "胡克定律 σ = Eε 适用于什么范围？",
         "options": ["弹性范围内", "塑性范围内", "全部变形范围"], "answer": 0},
        {"question": "悬臂梁自由端受集中力P时，最大挠度出现在哪里？",
         "options": ["自由端", "固定端", "梁中点"], "answer": 0},
        {"question": "圆轴扭转时，最大切应力出现在什么位置？",
         "options": ["轴表面", "轴心", "半径中点"], "answer": 0}
    ]
    
    if st.button("🔄 开始测验"):
        st.session_state['score'] = 0
        st.session_state['answered'] = 0
        st.session_state['current_q'] = random.randint(0, len(questions)-1)
        st.session_state['quiz_started'] = True
    
    if 'quiz_started' not in st.session_state:
        st.session_state['quiz_started'] = False
        st.session_state['score'] = 0
        st.session_state['answered'] = 0
        st.session_state['current_q'] = 0
    
    if st.session_state['quiz_started']:
        idx = st.session_state['current_q']
        q = questions[idx]
        st.markdown(f"### 第 {st.session_state['answered']+1} 题")
        st.markdown(f"**{q['question']}**")
        user_answer = st.radio("选择答案", q['options'], key=f"q_{idx}")
        if st.button("提交答案"):
            if q['options'].index(user_answer) == q['answer']:
                st.success("✅ 正确！")
                st.session_state['score'] += 1
            else:
                st.error(f"❌ 错误，正确答案是：{q['options'][q['answer']]}")
            st.session_state['answered'] += 1
            if st.session_state['answered'] < 4:
                st.session_state['current_q'] = random.randint(0, len(questions)-1)
            else:
                st.balloons()
                st.success(f"🎉 完成！答对 {st.session_state['score']} / {st.session_state['answered']} 题！")
                st.session_state['quiz_started'] = False
        if st.session_state['answered'] > 0 and st.session_state['answered'] < 4:
            st.progress(st.session_state['answered'] / 4)

# ============================================================
# 9. 综合工程案例
# ============================================================
elif module == "🏗️ 综合工程案例":
    st.title("🏗️ 综合工程案例：起重机吊臂设计")
    
    st.markdown("""
    ### 📌 设计任务
    - 最大起重量 **F = 50 kN**
    - 吊臂长度 **L = 5 m**
    - 材料：**Q235钢**（σ_s = 235 MPa, E = 210 GPa）
    - 安全系数 **n = 2**
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        L = st.slider("吊臂长度 L (m)", 2.0, 8.0, 5.0, 0.5, key="case_L")
        F = st.slider("最大起重量 F (kN)", 10, 100, 50, 5, key="case_F")
        b = st.slider("截面宽 b (mm)", 50, 400, 200, 10)
        h = st.slider("截面高 h (mm)", 50, 500, 300, 10)
    
    with col2:
        n = st.slider("安全系数 n", 1.5, 4.0, 2.0, 0.5)
        sigma_s = st.number_input("屈服强度 σ_s (MPa)", value=235, step=5)
        E = st.number_input("弹性模量 E (GPa)", value=210, step=10)
    
    # 计算
    A = b * h
    I = b * h**3 / 12
    W = I / (h/2)
    sigma_allow = sigma_s / n
    M_max = F * 1000 * L
    sigma_max = M_max / (W * 1e-9) / 1e6
    E_actual = E * 1e9
    w_max = F * 1000 * L**3 / (3 * E_actual * I * 1e-12) * 1000
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("最大弯矩", f"{M_max/1000:.1f} kN·m")
        st.metric("最大正应力", f"{sigma_max:.2f} MPa")
    with c2:
        st.metric("许用应力", f"{sigma_allow:.2f} MPa")
        st.metric("最大挠度", f"{w_max:.2f} mm")
    with c3:
        strength_ok = sigma_max <= sigma_allow
        stiffness_ok = w_max <= L*1000/500
        st.metric("强度校核", "✅ 通过" if strength_ok else "❌ 不通过")
        st.metric("刚度校核", "✅ 通过" if stiffness_ok else "❌ 不通过")
    
    if all([strength_ok, stiffness_ok]):
        st.balloons()
        st.success("🎉 设计满足所有要求！")
    else:
        st.error("⚠️ 设计不满足要求，请调整参数")
    
    # 应力云图
    y_plot = np.linspace(-h/2, h/2, 50)
    z_plot = np.linspace(-b/2, b/2, 50)
    Y, Z = np.meshgrid(y_plot, z_plot)
    sigma_plot = sigma_max * (Y / (h/2))
    
    fig = go.Figure(data=go.Heatmap(
        z=sigma_plot, x=z_plot, y=y_plot,
        colorscale='RdYlBu_r', zmid=0,
        colorbar=dict(title="应力 (MPa)")
    ))
    fig.update_layout(title="吊臂危险截面应力云图", height=350)
    fig = set_chinese_font(fig)
    st.plotly_chart(fig, use_container_width=True)

# ========== 底部 ==========
st.markdown("---")
st.caption("📐 材料力学交互式智能学习系统 v2.0 | 共9大模块 | 拖动滑块、点击按钮，探索力学的奥秘！")