import streamlit as st

st.set_page_config(page_title="About", layout="wide")

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
    
    .header-gradient {
        background: linear-gradient(135deg, #0f1b3c 0%, #1a2f5a 100%);
        padding: 3rem 2rem;
        border-radius: 0 0 20px 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(15, 27, 60, 0.15);
    }
    
    .header-gradient h1 {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .header-gradient p {
        font-size: 1rem;
        margin: 0.8rem 0 0 0;
        opacity: 0.9;
        font-weight: 300;
    }
    
    .content-card {
        background: white;
        border-radius: 16px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #2563eb;
    }
    
    .content-card h2 {
        color: #0f1b3c;
        font-size: 1.8rem;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }
    
    .content-card p, .content-card li {
        color: #334155;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%);
        padding: 2rem;
        border-radius: 12px;
        border-left: 4px solid #10b981;
    }
    
    .feature-card h3 {
        color: #0f1b3c;
        margin-top: 0;
        font-weight: 700;
    }
    
    .feature-card p {
        color: #475569;
        margin-bottom: 0;
    }
    
    .tech-badge {
        display: inline-block;
        background: linear-gradient(135deg, #2563eb 0%, #0f1b3c 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        margin: 0.5rem 0.5rem 0.5rem 0;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .highlight {
        color: #10b981;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-gradient">
        <h1>📚 About Cell Classifier</h1>
        <p>Understanding advanced cervical cell detection technology</p>
    </div>
    """, unsafe_allow_html=True)

# About section
st.markdown("""
    <div class="content-card">
        <h2>🎯 Project Overview</h2>
        <p>
            Cell Classifier is an advanced artificial intelligence system designed to automatically detect and classify 
            cervical cell types from microscopic images. Using state-of-the-art deep learning technology, our system can 
            accurately identify five distinct cell classifications with high precision.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Classification types
st.markdown("""
    <div class="content-card">
        <h2>🔬 Classification Types</h2>
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

# Features
st.markdown("""
    <div class="content-card">
        <h2>✨ Key Features</h2>
        <ul>
            <li><span class="highlight">Rapid Analysis:</span> Get instant results in seconds using advanced GPU acceleration</li>
            <li><span class="highlight">High Accuracy:</span> ResNet50 architecture trained on extensive cervical cell datasets</li>
            <li><span class="highlight">Confidence Scoring:</span> Transparent confidence metrics for each prediction</li>
            <li><span class="highlight">Probability Distribution:</span> View detailed breakdown of all classification probabilities</li>
            <li><span class="highlight">User-Friendly Interface:</span> Intuitive design optimized for medical professionals</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Technology
st.markdown("""
    <div class="content-card">
        <h2>🛠️ Technology Stack</h2>
        <p>Built with cutting-edge technologies for optimal performance and reliability:</p>
        <div style="padding: 1rem; background: #f8fafc; border-radius: 8px; margin: 1rem 0;">
        """, unsafe_allow_html=True)

tech_stack = ["PyTorch", "ResNet50", "Streamlit", "CUDA", "Python 3.x", "TorchVision"]
for tech in tech_stack:
    st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# How it works
st.markdown("""
    <div class="content-card">
        <h2>⚙️ How It Works</h2>
        <ol>
            <li><strong>Image Upload:</strong> Upload a high-quality cervical cell microscopy image</li>
            <li><strong>Preprocessing:</strong> Image is automatically normalized and resized to optimal dimensions</li>
            <li><strong>Deep Learning Analysis:</strong> ResNet50 model analyzes the cellular features</li>
            <li><strong>Classification:</strong> Assigns the cell to one of five classification categories</li>
            <li><strong>Results:</strong> Displays prediction with confidence score and probability distribution</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 2rem 0;">
        <p>🔐 Developed with precision and care for medical excellence</p>
        <p style="font-size: 0.9rem;">© 2026 Cell Classifier | Advanced Medical AI Technology</p>
    </div>
    """, unsafe_allow_html=True)
