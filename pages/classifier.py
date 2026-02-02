import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import StandardResNet50

st.set_page_config(page_title="Cell Classifier", layout="wide")

# Custom CSS for multi-page aesthetics
st.markdown("""
    <style>
    :root {
        --navy: #0f1b3c;
        --light-navy: #1a2f5a;
        --bright-navy: #2563eb;
        --accent: #10b981;
        --white: #ffffff;
        --light-gray: #f8fafc;
        --border: #e2e8f0;
    }
    
    * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }
    
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
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .header-gradient p {
        font-size: 1.1rem;
        margin: 0.8rem 0 0 0;
        opacity: 0.9;
        font-weight: 300;
    }
    
    .upload-section {
        background: white;
        border: 2px dashed #2563eb;
        border-radius: 16px;
        padding: 2.5rem;
        text-align: center;
        margin: 2rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.1);
    }
    
    .upload-section:hover {
        border-color: #10b981;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.15);
        transform: translateY(-2px);
    }
    
    .result-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #10b981;
    }
    
    .prediction-badge {
        background: linear-gradient(135deg, #2563eb 0%, #0f1b3c 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
    }
    
    .prediction-label {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.9;
        font-weight: 600;
    }
    
    .prediction-value {
        font-size: 2.2rem;
        font-weight: 800;
        margin-top: 0.5rem;
    }
    
    .confidence-section {
        background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 4px solid #2563eb;
    }
    
    .confidence-label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #0f1b3c;
        margin-bottom: 0.8rem;
    }
    
    .confidence-percent {
        font-size: 1.8rem;
        font-weight: 700;
        color: #10b981;
    }
    
    .chart-container {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    .chart-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0f1b3c;
        margin-bottom: 1.5rem;
    }
    
    .class-list {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
    }
    
    .class-item {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        border-left: 3px solid #2563eb;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .class-name {
        font-weight: 600;
        color: #0f1b3c;
    }
    
    .class-prob {
        font-weight: 700;
        color: #10b981;
        font-size: 1rem;
    }
    
    .loading-spinner {
        color: #2563eb;
        text-align: center;
        padding: 2rem;
    }
    
    .error-box {
        background: #fee2e2;
        border: 1px solid #fecaca;
        border-radius: 12px;
        padding: 1.5rem;
        color: #991b1b;
        margin: 1rem 0;
    }
    
    .success-box {
        background: #dcfce7;
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 1.5rem;
        color: #166534;
        margin: 1rem 0;
    }
    
    .disclaimer-box {
        background: #fee2e2;
        border: 2px solid #fecaca;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .disclaimer-box p {
        margin: 0;
        color: #991b1b;
    }
    
    .disclaimer-title {
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .disclaimer-text {
        font-size: 0.95rem;
        margin-top: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        if not os.path.exists("resnet50_cervical.pth"):
            return None, device, "Model file not found"
        
        model = StandardResNet50(num_classes=5).to(device)
        model.load_state_dict(torch.load("resnet50_cervical.pth", map_location=device))
        model.eval()
        return model, device, "success"
    except Exception as e:
        return None, None, str(e)

model, device, model_status = load_model()

# Define Transform
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

transform = transforms.Compose([
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD)
])

class_names = ['Dyskeratotic', 'Koilocytotic', 'Metaplastic', 'Parabasal', 'Superficial-Intermediate']

# Header
st.markdown("""
    <div class="header-gradient">
        <h1>🔬 Cell Classification AI</h1>
        <p>Advanced ResNet50-powered cervical cell type detection</p>
    </div>
    """, unsafe_allow_html=True)

# Check model status
if model_status != "success":
    st.markdown(f'<div class="error-box">❌ Model Loading Error: {model_status}</div>', unsafe_allow_html=True)
    st.stop()

# Main content
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown("### 📤 Upload Cell Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, use_column_width=True, caption="Uploaded Image")

with col2:
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file).convert("RGB")
            input_tensor = transform(image).unsqueeze(0).to(device)
            
            with st.spinner("🔄 Analyzing cell..."):
                with torch.no_grad():
                    outputs = model(input_tensor)
                    probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]
                    _, predicted = torch.max(outputs, 1)
                    label = class_names[predicted.item()]
                    confidence = probabilities[predicted.item()].item()
            
            # Display prediction
            st.markdown("""
                <div class="prediction-badge">
                    <div class="prediction-label">Predicted Classification</div>
                    <div class="prediction-value">""" + label + """</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Display confidence
            st.markdown(f"""
                <div class="confidence-section">
                    <div class="confidence-label">Confidence Score</div>
                    <div class="confidence-percent">{confidence:.1%}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.progress(confidence)
            
        except Exception as e:
            st.markdown(f'<div class="error-box">❌ Error: {str(e)}</div>', unsafe_allow_html=True)

# Probability distribution
if uploaded_file is not None:
    st.markdown("---")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("### 📊 Probability Distribution")
    
    image = Image.open(uploaded_file).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]
    
    prob_dict = {class_names[i]: probabilities[i].item() for i in range(len(class_names))}
    prob_dict = dict(sorted(prob_dict.items(), key=lambda x: x[1], reverse=True))
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.bar_chart(prob_dict)
    
    with col2:
        st.markdown("**Class Probabilities:**")
        for cls, prob in prob_dict.items():
            st.markdown(f"<div class='class-item'><span class='class-name'>{cls}</span><span class='class-prob'>{prob:.1%}</span></div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 2rem 0;">
        <div style="background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%); border-left: 4px solid #2563eb; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <p style="color: #0f1b3c; margin: 0; font-weight: 600; font-size: 0.95rem;">ℹ️ Notice</p>
            <p style="color: #475569; margin: 0.8rem 0 0 0; font-size: 0.9rem;">
                This tool is purely for academic purposes and is currently under review for clinical use. It may therefore not be advisable to use without the guidance of a medical professional.
            </p>
        </div>
        <p style="font-size: 0.9rem;">© 2026 Cell Classifier | Advanced Deep Learning Technology</p>
    </div>
    """, unsafe_allow_html=True)
