import streamlit as st
import base64

def set_page_config():
    st.set_page_config(
        page_title="TestCaseGen AI",
        page_icon="🧪",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .title-text {
            font-size: 2.8rem;
            font-weight: 700;
            color: #1e3a8a;
            margin-bottom: 0.5rem;
        }
        .subtitle-text {
            font-size: 1.2rem;
            color: #4b5563;
            margin-bottom: 2rem;
        }
        .card {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            margin-bottom: 2rem;
        }
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #3b82f6;
        }
        .get-started-btn {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            margin-top: 1rem;
        }
        .get-started-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

def display_hero():
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown('<div class="title-text">AI-Powered Test Case Generation</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle-text">Transform your software requirements into comprehensive test cases with the power of AI</div>', unsafe_allow_html=True)
        
        st.markdown('''
        <div style="margin-bottom: 2rem;">
            <p style="font-size: 1.1rem; color: #4b5563; margin-bottom: 1.5rem;">
                Simply describe your software requirements in natural language, and our advanced AI will generate 
                detailed test cases including test steps, expected results, and edge cases.
            </p>
        </div>
        ''', unsafe_allow_html=True)
        

    
    with col2:
        # Software testing illustration
        st.image(
            "https://cdn.prod.website-files.com/619e15d781b21202de206fb5/62f62b00791f0a712a693a46_Core-Benefits-of-Automated-Testing-in-App-Development.webp",
            use_container_width=True,
            caption="Comprehensive Software Testing Process"
        )

def display_features():
    st.markdown("## ✨ Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="feature-icon">🚀</div>', unsafe_allow_html=True)
            st.markdown("### Rapid Test Creation")
            st.markdown("Generate test cases in seconds instead of hours. Focus on building great software while we handle the testing.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="feature-icon">🤖</div>', unsafe_allow_html=True)
            st.markdown("### AI-Powered")
            st.markdown("Leverage the power of advanced LLMs to create comprehensive and accurate test cases that cover all scenarios.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="feature-icon">📊</div>', unsafe_allow_html=True)
            st.markdown("### Detailed Reports")
            st.markdown("Get clear, structured test cases with step-by-step instructions and expected results for each scenario.")
            st.markdown('</div>', unsafe_allow_html=True)

set_page_config()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Display the homepage content
display_hero()
st.markdown("<br><br>", unsafe_allow_html=True)
display_features()


