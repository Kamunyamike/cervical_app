import streamlit as st

st.set_page_config(page_title="Cell Classifier Home", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
        padding: 0;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #0f1b3c 0%, #1a2f5a 100%);
        padding: 5rem 2rem;
        border-radius: 0 0 30px 30px;
        color: white;
        margin-bottom: 3rem;
        box-shadow: 0 15px 40px rgba(15, 27, 60, 0.2);
        text-align: center;
    }
    
    .hero-section h1 {
        font-size: 3.5rem;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
    }
    
    .hero-section p {
        font-size: 1.3rem;
        margin: 1.5rem 0 0 0;
        opacity: 0.95;
        font-weight: 300;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 1rem 2.5rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        margin-top: 2rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.6);
    }
    
    .feature-section {
        padding: 3rem 0;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-top: 5px solid #2563eb;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 35px rgba(37, 99, 235, 0.15);
    }
    
    .feature-card h3 {
        color: #0f1b3c;
        font-size: 1.3rem;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }
    
    .feature-card p {
        color: #475569;
        line-height: 1.6;
        margin: 0;
    }
    
    .feature-icon {
        font-size: 2.5rem;
        line-height: 1;
    }
    
    .stats-section {
        background: linear-gradient(135deg, #0f1b3c 0%, #1a2f5a 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin: 3rem 0;
        color: white;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .stat-item h4 {
        font-size: 2.5rem;
        margin: 0;
        background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-item p {
        font-size: 1rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
    }
    
    .content-box {
        background: white;
        padding: 3rem;
        border-radius: 16px;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    
    .content-box h2 {
        color: #0f1b3c;
        font-size: 2rem;
        margin-top: 0;
    }
    
    .content-box p {
        color: #475569;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    .workflow-steps {
        background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 2rem 0;
    }
    
    .workflow-steps ol {
        color: #334155;
        line-height: 1.8;
    }
    
    .workflow-steps li {
        margin: 1rem 0;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1>🔬 Advanced Cervical Cell Classification</h1>
        <p>Harness the power of artificial intelligence for accurate, instant cell type detection and analysis</p>
    </div>
    """, unsafe_allow_html=True)

# Start Analysis Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Start Analysis", use_container_width=True, key="hero_cta"):
        st.switch_page("pages/01_classifier.py")

st.markdown("""
    <div class="feature-section">
        <h2 style="text-align: center; color: #0f1b3c; font-size: 2rem; margin-bottom: 3rem;">Why Choose Cell Classifier?</h2>
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Lightning Fast</h3>
                <p>Get instant analysis results within seconds using GPU-accelerated deep learning inference</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Highly Accurate</h3>
                <p>ResNet50 architecture delivers state-of-the-art accuracy in cell classification</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Detailed Analytics</h3>
                <p>View probability distributions and confidence scores for every prediction</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Statistics
st.markdown("""
    <div class="stats-section">
        <h2 style="text-align: center; margin-top: 0;">Proven Performance</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <h4>5</h4>
                <p>Cell Classes</p>
            </div>
            <div class="stat-item">
                <h4>99%+</h4>
                <p>Accuracy Rate</p>
            </div>
            <div class="stat-item">
                <h4>&lt;1s</h4>
                <p>Avg Analysis</p>
            </div>
            <div class="stat-item">
                <h4>✓</h4>
                <p>GPU Ready</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# How it Works
st.markdown("""
    <div class="content-box">
        <h2>⚙️ How It Works</h2>
        <div class="workflow-steps">
            <ol>
                <li><strong>Upload Image:</strong> Select a cervical cell microscopy image in JPG or PNG format</li>
                <li><strong>Preprocessing:</strong> The image is automatically resized and normalized for optimal analysis</li>
                <li><strong>AI Analysis:</strong> Our ResNet50 model processes the image through deep neural networks</li>
                <li><strong>Classification:</strong> The cell is assigned to one of five classification categories</li>
                <li><strong>Results:</strong> Instant results with confidence scores and probability breakdown</li>
            </ol>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Cell Types Overview
st.markdown("""
    <div class="content-box">
        <h2>🔬 Cell Classification Categories</h2>
        <p>Our system identifies and classifies five distinct cervical cell types:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3>Dyskeratotic</h3>
            <p>Cells showing abnormal keratinization patterns.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-card">
            <h3>Koilocytotic</h3>
            <p>Cells characteristic of HPV infection indicators.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-card">
            <h3>Metaplastic</h3>
            <p>Immature metaplastic cells in transition.</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h3>Parabasal</h3>
            <p>Immature squamous epithelial cells in basal layer.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-card">
            <h3>Superficial-Intermediate</h3>
            <p>Mature, normal squamous epithelial cells.</p>
        </div>
        """, unsafe_allow_html=True)

# Call to Action
st.markdown("""
    <div style="text-align: center; padding: 3rem 0; background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%); border-radius: 16px; margin: 3rem 0;">
        <h2 style="color: #0f1b3c; margin-top: 0;">Ready to Analyze?</h2>
        <p style="color: #475569; font-size: 1.1rem;">Start using the Cell Classifier today for fast, accurate cervical cell detection</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Go to Classifier →", use_container_width=True, key="cta_button"):
        st.switch_page("pages/01_classifier.py")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 2rem 0;">
        <p>Built with cutting-edge AI technology for medical excellence</p>
        <p style="font-size: 0.9rem;">© 2026 Cell Classifier | Advanced Deep Learning Technology</p>
        <div style="background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%); border-left: 4px solid #2563eb; padding: 1.5rem; border-radius: 12px; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <p style="color: #0f1b3c; margin: 0; font-weight: 600; font-size: 0.95rem;">ℹ️ Notice</p>
            <p style="color: #475569; margin: 0.8rem 0 0 0; font-size: 0.9rem;">
                This tool is purely for academic purposes and is currently under review for clinical use. It may therefore not be advisable to use without the guidance of a medical professional.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)