import streamlit as st
from rag import streaming_question_answering_code

# Set page config
st.set_page_config(
    page_title="Code Review Assistant",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .suggestion {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 5px solid #3b82f6;
    }
    .suggestion h4 {
        color: #1e3a8a;
        margin-top: 0;
    }
    .suggestion pre {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 8px;
        white-space: pre-wrap;
    }
    .severity-high {
        color: #dc2626;
        font-weight: bold;
    }
    .severity-medium {
        color: #d97706;
        font-weight: bold;
    }
    .severity-low {
        color: #059669;
    }
</style>
""", unsafe_allow_html=True)

# Template for code review
CODE_REVIEW_TEMPLATE = """
As an experienced software engineer, analyze the following code snippet and provide a detailed code review.

Code to Review:
```
{code}
```

For the code review, please provide:
1. Potential bugs or errors
2. Code smells and anti-patterns
3. Security vulnerabilities
4. Performance issues
5. Code style and best practices
6. Suggested improvements

For each issue found, please include:
- A brief description
- Severity level (High/Medium/Low)
- The problematic code snippet
- Suggested fix or improvement

Format your response in clear, structured markdown with appropriate headings and code blocks.
"""

def review_code(code):
    """Generate code review using the RAG system."""
    try:
        # Get the streaming response
        response_stream = streaming_question_answering_code(
            code=code,
            template=CODE_REVIEW_TEMPLATE
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
        st.error(f"Error generating code review: {str(e)}")
        return None

st.title("🤖 AI Code Review Assistant")
st.markdown("Get instant code reviews with AI-powered analysis of your code.")

# Code input
code = st.text_area(
    "Paste your code here:",
    height=300,
    placeholder="def example():\n    x = 5\n    y = 0\n    return x/y"
)

# Language selection
language = st.selectbox(
    "Select programming language:",
    ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Ruby", "TypeScript", "Other"]
)

# Review button
if st.button("Review Code"):
    if not code.strip():
        st.warning("Please enter some code to review.")
    else:
        with st.spinner("Analyzing code..."):
            review_code(code)

# Example section
with st.expander("Example Code Snippets"):
    st.markdown("""
    **Example 1: Python - Division by Zero**
    ```python
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)
    
    # Potential issue: Will raise ZeroDivisionError if numbers is empty
    ```
    
    **Example 2: JavaScript - Undefined Check**
    ```javascript
    function processUser(user) {
        return user.name.first + " " + user.name.last;
    }
    // Potential issue: No null/undefined check for user or user.name
    ```
    
    **Example 3: Python - Inefficient String Concatenation**
    ```python
    def build_string(items):
        result = ""
        for item in items:
            result += str(item)
        return result
    # Issue: String concatenation in a loop is inefficient
    ```
    """)
