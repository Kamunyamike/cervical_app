import streamlit as st

st.set_page_config(page_title="Research Publication", layout="wide")

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
    
    .paper-header {
        background: white;
        border-radius: 16px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #2563eb;
    }
    
    .paper-title {
        color: #0f1b3c;
        font-size: 2rem;
        font-weight: 800;
        margin: 0 0 1rem 0;
    }
    
    .author-info {
        color: #475569;
        font-size: 1.05rem;
        margin: 0.5rem 0;
    }
    
    .affiliation {
        color: #64748b;
        font-style: italic;
        font-size: 0.95rem;
        margin: 0.3rem 0;
    }
    
    .section-card {
        background: white;
        border-radius: 16px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-top: 5px solid #2563eb;
    }
    
    .section-title {
        color: #0f1b3c;
        font-size: 1.6rem;
        font-weight: 700;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }
    
    .section-content {
        color: #475569;
        font-size: 1.05rem;
        line-height: 1.8;
    }
    
    .result-item {
        background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%);
        padding: 2rem;
        border-radius: 12px;
        border-left: 4px solid #10b981;
        text-align: center;
    }
    
    .result-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #10b981;
        margin: 0.5rem 0;
    }
    
    .result-label {
        font-size: 0.95rem;
        color: #475569;
        font-weight: 600;
        margin: 0;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fee2e2 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
    }
    
    .highlight-box strong {
        color: #92400e;
    }
    
    .highlight-box p {
        color: #b45309;
        margin: 0;
    }
    
    .methodology-step {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #2563eb;
    }
    
    .methodology-step strong {
        color: #0f1b3c;
        font-size: 1.1rem;
    }
    
    .methodology-step p {
        color: #475569;
        margin: 0.5rem 0 0 0;
    }
    
    .keyword-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin: 1.5rem 0;
    }
    
    .keyword-tag {
        background: linear-gradient(135deg, #2563eb 0%, #0f1b3c 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-gradient">
        <h1>📄 Research Publication</h1>
        <p>Peer-reviewed research on automated cervical cancer detection via deep learning</p>
    </div>
    """, unsafe_allow_html=True)

# Paper Header
st.markdown("""
    <div class="paper-header">
        <h2 class="paper-title">Automated Cervical Cancer Detection via Deep Learning</h2>
        <p class="author-info"><strong>Authors:</strong></p>
        <p class="author-info">Mikenickson Wanjohi — African Centre for Data Science and Analytics — <a href="mailto:kamunyawanjohi@gmail.com">kamunyawanjohi@gmail.com</a></p>
        <p class="author-info">John Ng'ang'a — The Cooperative University of Kenya</a></p>
        <p class="author-info">Florence Kinyua — School of Health Sciences, University of Nairobi</a></p>
        <p class="affiliation"><strong>Primary Subject Area:</strong> Reimagining Public Health &amp; Health Systems</p>
        <div class="keyword-tags">
            <span class="keyword-tag">Deep Learning</span>
            <span class="keyword-tag">Cervical Cancer</span>
            <span class="keyword-tag">CNN</span>
            <span class="keyword-tag">Medical Imaging</span>
            <span class="keyword-tag">Diagnostic AI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Introduction
st.markdown("""
    <div class="section-card">
        <h3 class="section-title">📋 Introduction</h3>
        <div class="section-content">
            <p>
                Cervical cancer remains a major global health challenge, particularly in regions with limited 
                access to advanced diagnostic infrastructure. Manual Pap smear examination is subjective, labor-intensive, 
                and time-consuming, requiring highly skilled cytologists.
            </p>
            <p>
                This dependency often leads to diagnostic inconsistencies and delays in treatment, contributing to adverse health outcomes. 
                We aimed at developing an automated, scalable, and highly accurate diagnostic system utilizing deep learning to address 
                these limitations.
            </p>
            <div class="highlight-box">
                <strong>🎯 Research Objective:</strong>
                <p>
                    Produce a model capable of rapid and reliable classification of cervical cell images into clinically 
                    relevant categories, supporting early detection and intervention.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Methodology
st.markdown("""
    <div class="section-card">
        <h3 class="section-title">🔬 Methodology</h3>
        <div class="section-content">
            <p><strong>Dataset:</strong> SIPaKMeD (publicly available Pap smear cell images)</p>
            <p><strong>Cell Classifications:</strong> Five clinically relevant categories</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Cell categories
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
        <div class="result-item">
            <div style="font-size: 1.8rem;">🔵</div>
            <strong>Superficial & Intermediate Squamous</strong>
            <p style="color: #64748b; font-size: 0.9rem;">Normal mature cells</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="result-item">
            <div style="font-size: 1.8rem;">🟢</div>
            <strong>Parabasal</strong>
            <p style="color: #64748b; font-size: 0.9rem;">Normal intermediate cells</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="result-item">
            <div style="font-size: 1.8rem;">🟠</div>
            <strong>Metaplastic</strong>
            <p style="color: #64748b; font-size: 0.9rem;">Abnormal changes in epithelial cells</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="result-item">
            <div style="font-size: 1.8rem;">🟡</div>
            <strong>Koilocytotic (HPV)</strong>
            <p style="color: #64748b; font-size: 0.9rem;">HPV-infected cells</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="result-item">
            <div style="font-size: 1.8rem;">🔴</div>
            <strong>Dyskeratotic</strong>
            <p style="color: #64748b; font-size: 0.9rem;">Precancerous cells</p>
        </div>
        """, unsafe_allow_html=True)

# Data Processing
st.markdown("""
    <div class="section-card">
        <h3 class="section-title">⚙️ Data Processing Pipeline</h3>
        <div class="methodology-step">
            <strong>🖼️ Preprocessing</strong>
            <p>Resizing, normalization, and quality enhancement of cell images</p>
        </div>
        <div class="methodology-step">
            <strong>🔄 Data Augmentation</strong>
            <p>Random flips, rotations, zoom, and brightness adjustments to expand dataset diversity and improve generalization</p>
        </div>
        <div class="methodology-step">
            <strong>🧠 CNN Architecture</strong>
            <p>Custom Convolutional Neural Network with multiple convolutional layers, max pooling, dropout regularization, and softmax classification layer</p>
        </div>
        <div class="methodology-step">
            <strong>🎓 Training Strategy</strong>
            <p>Adam optimizer, categorical crossentropy loss, early stopping, and learning rate reduction callbacks with continuous validation monitoring</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Results
st.markdown("""
    <div class="section-card">
        <h3 class="section-title">📊 Results & Performance</h3>
        <p class="section-content">The trained CNN achieved strong performance metrics across all classification tasks:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
        <div class="result-item">
            <div class="result-value">94%</div>
            <div class="result-label">Validation Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="result-item">
            <div class="result-value">91.3%</div>
            <div class="result-label">Test Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="result-item">
            <div class="result-value">0.2145</div>
            <div class="result-label">Test Loss</div>
        </div>
        """, unsafe_allow_html=True)

# Discussion
st.markdown("""
    <div class="section-card">
        <h3 class="section-title">💡 Discussion & Findings</h3>
        <div class="section-content">
            <p>
                <strong>Clinical Significance:</strong> The model demonstrated reliable classification across all five categories. 
                Dyskeratotic and koilocytotic cells, which are clinically significant for HPV infection and precancerous changes, 
                were consistently and accurately identified.
            </p>
            <p>
                <strong>Viability Confirmation:</strong> The high accuracy metrics confirm the viability of this deep learning approach 
                for automated cervical cancer detection and early intervention.
            </p>
            <p>
                <strong>Future Improvements:</strong> Our roadmap includes:
            </p>
            <ul>
                <li>Enhancing interpretability through Grad-CAM visualizations</li>
                <li>Expanding to full-slide image analysis</li>
                <li>Validating predictions with clinical experts</li>
                <li>Fine-tuning hyperparameters for improved performance</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Conclusion
st.markdown("""
    <div class="section-card">
        <h3 class="section-title">✅ Conclusion</h3>
        <div class="section-content">
            <p>
                These findings confirm that the developed deep learning architecture is well-suited for cervical cancer detection 
                using Pap smear imagery. The system offers a practical solution for improving diagnostic speed and accuracy in 
                underserved settings.
            </p>
            <div class="highlight-box">
                <strong>🚀 Next Steps:</strong>
                <p>
                    Fine-tuning hyperparameters, scaling deployment to mobile and edge devices, and integrating the model into 
                    a user-friendly web application for real-world clinical use.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 2rem 0;">
        <p><strong>Publication Details</strong></p>
        <p style="font-size: 0.95rem;">Presented at: The Kash Conference @ KEMRI</p>
        <p style="font-size: 0.9rem;">© 2026 Automated Cervical Cancer Detection Research | African Centre for Data Science and Analytics</p>
    </div>
    """, unsafe_allow_html=True)
