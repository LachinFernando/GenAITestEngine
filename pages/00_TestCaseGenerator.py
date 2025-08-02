import streamlit as st
from rag import streaming_question_answering
import json

# Set page config
st.set_page_config(
    page_title="Test Case Generator",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .test-case {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 5px solid #3b82f6;
    }
    .test-case h4 {
        color: #1e3a8a;
        margin-top: 0;
    }
    .test-case pre {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 8px;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# Template for test case generation
TEST_CASE_TEMPLATE = """
As a professional QA engineer, generate comprehensive test cases based on the following software requirements.

Requirements:
{requirements}

For each test case, provide:
1. Test Case ID and Title
2. Test Steps (detailed and sequential)
3. Test Data (inputs)
4. Expected Results
5. Actual Results (leave blank for execution)
6. Pass/Fail (leave blank for execution)
7. Any additional notes or preconditions

Format the output in clear, structured markdown with appropriate headings and bullet points.
"""

def generate_test_cases(requirements):
    """Generate test cases using the RAG system."""
    try:
        # Get the streaming response
        response_stream = streaming_question_answering(
            requirements=requirements,
            template=TEST_CASE_TEMPLATE
        )
        
        # Display the streaming response
        message_placeholder = st.empty()
        full_response = ""
        
        for chunk in response_stream:
            if chunk is not None:
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        return full_response
        
    except Exception as e:
        st.error(f"Error generating test cases: {str(e)}")
        return None

st.title("AI-Powered Test Case Generator")
st.markdown("Transform your software requirements into comprehensive test cases with the power of AI.")

# Requirements input
requirements = st.text_area(
    "Enter your software requirements (be as detailed as possible):",
    height=200,
    placeholder="Example: The system should allow users to register with email and password. Password must be at least 8 characters long and contain at least one number and one special character."
)

# Generate button
if st.button("Generate Test Cases"):
    if not requirements.strip():
        st.warning("Please enter some requirements to generate test cases.")
    else:
        with st.spinner("Generating test cases..."):
            generate_test_cases(requirements)

# Example section
with st.expander("Example Requirements"):
    st.markdown("""
    **Example 1: User Authentication**
    ```
    The login page should have email and password fields.
    - Email format should be validated
    - Password should be masked
    - Show 'Forgot Password' link
    - Login button should be disabled until both fields are filled
    ```
    
    **Example 2: Shopping Cart**
    ```
    The shopping cart should allow users to:
    - Add/remove items
    - Update quantities
    - See item subtotals and total
    - Apply discount codes
    - Proceed to checkout
    ```
    """)
