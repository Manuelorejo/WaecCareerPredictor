import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Career Recommendation System",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS inspired by the Tech Career Advisor design but with modifications
st.markdown("""
<style>
    .main {
        padding: 20px;
    }
    .title {
        color: #20c997;
        text-align: center;
        font-size: calc(1.8rem + 1vw) !important;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #495057;
        text-align: center;
        font-size: calc(1.2rem + 0.5vw) !important;
        margin-bottom: 30px;
    }
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    .cta-button {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        color: #6c757d;
        padding-top: 50px;
    }
    .intro-text {
        text-align: center; 
        max-width: 800px; 
        margin: 0 auto; 
        padding: 20px;
    }
    .intro-text p {
        font-size: 18px;
    }
    .process-step {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .step-number {
        background-color: #20c997;
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        margin-right: 20px;
        flex-shrink: 0;
    }
    .step-content {
        flex-grow: 1;
    }
    .step-title {
        font-weight: bold;
        color: #20c997;
        font-size: 18px;
        margin-bottom: 5px;
    }
    .career-category {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .career-category-title {
        color: #20c997;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 15px;
        border-bottom: 2px solid #e9ecef;
        padding-bottom: 10px;
    }
    .career-item {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .career-icon {
        width: 30px;
        text-align: center;
        margin-right: 15px;
        font-size: 20px;
    }
    .career-path-section {
        margin-top: 40px;
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("<h1 class='title'>🎓 Career Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Find Your Ideal Career Path Based on Elementary School Performance</h2>", unsafe_allow_html=True)

# Main image - updated to a different image
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("https://img.freepik.com/free-vector/choosing-best-career-way-flat-vector-illustration_82574-3471.jpg", use_container_width=True)

# Introduction
st.markdown("""
<div class='intro-text'>
    <p>
        Our data-driven Career Recommendation System analyzes elementary student performance 
        to identify natural aptitudes and potential career paths. Get personalized guidance 
        early in your educational journey to make informed decisions about your future.
    </p>
</div>
""", unsafe_allow_html=True)

# Redesigned "How It Works" section with a timeline/process flow approach
st.markdown("<h2 style='text-align: center; margin-top: 30px; margin-bottom: 30px;'>How It Works</h2>", unsafe_allow_html=True)

# Process step 1
st.markdown("""
<div class="process-step">
    <div class="step-number">1</div>
    <div class="step-content">
        <div class="step-title">Enter Your Academic Information</div>
        <p>Provide your scores in core elementary subjects like Mathematics, Science, and Language Arts. 
        Tell us about your learning style preferences to enhance the accuracy of our recommendations.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Process step 2
st.markdown("""
<div class="process-step">
    <div class="step-number">2</div>
    <div class="step-content">
        <div class="step-title">Machine Learning Analysis</div>
        <p>Our advanced algorithm processes your academic data, identifying patterns in your performance 
        that correlate with success in various career fields. We analyze strengths across different 
        subject areas to find your natural aptitudes.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Process step 3
st.markdown("""
<div class="process-step">
    <div class="step-number">3</div>
    <div class="step-content">
        <div class="step-title">Review Your Personalized Results</div>
        <p>Receive a detailed analysis of your top career matches, complete with confidence scores 
        and descriptions of each path. Understand why these careers align with your academic 
        strengths and how you can further develop relevant skills.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to action
st.markdown("""
<div class='cta-button'>
    <a href='/Recommendation' target='_self'>
        <button style='
            background-color: #20c997;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
        '>
            Get My Career Recommendations
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# Completely redesigned Career Paths section
st.markdown("<div class='career-path-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Explore Career Domains</h2>", unsafe_allow_html=True)

# Create two columns for the career categories
col1, col2 = st.columns(2)

with col1:
    # STEM Careers
    st.markdown("""
    <div class="career-category">
        <div class="career-category-title">STEM Careers</div>
        <div class="career-item">
            <div class="career-icon">💻</div>
            <div>Computer Science & Information Technology</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🔧</div>
            <div>Engineering & Architecture</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🔬</div>
            <div>Natural Sciences & Research</div>
        </div>
        <div class="career-item">
            <div class="career-icon">⚕️</div>
            <div>Medicine & Healthcare</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🧮</div>
            <div>Mathematics & Statistics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Business & Commerce
    st.markdown("""
    <div class="career-category">
        <div class="career-category-title">Business & Commerce</div>
        <div class="career-item">
            <div class="career-icon">📊</div>
            <div>Finance & Accounting</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🏢</div>
            <div>Management & Administration</div>
        </div>
        <div class="career-item">
            <div class="career-icon">📣</div>
            <div>Marketing & Sales</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🌐</div>
            <div>International Business & Economics</div>
        </div>
        <div class="career-item">
            <div class="career-icon">📈</div>
            <div>Entrepreneurship & Innovation</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Humanities & Creative Arts
    st.markdown("""
    <div class="career-category">
        <div class="career-category-title">Humanities & Creative Arts</div>
        <div class="career-item">
            <div class="career-icon">🎨</div>
            <div>Visual & Performing Arts</div>
        </div>
        <div class="career-item">
            <div class="career-icon">✏️</div>
            <div>Writing & Literature</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🎭</div>
            <div>Media & Communication</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🏛️</div>
            <div>History & Cultural Studies</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🌎</div>
            <div>Languages & Linguistics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Service & Social Impact
    st.markdown("""
    <div class="career-category">
        <div class="career-category-title">Service & Social Impact</div>
        <div class="career-item">
            <div class="career-icon">⚖️</div>
            <div>Law & Legal Services</div>
        </div>
        <div class="career-item">
            <div class="career-icon">📚</div>
            <div>Education & Teaching</div>
        </div>
        <div class="career-item">
            <div class="career-icon">👥</div>
            <div>Social Sciences & Psychology</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🤝</div>
            <div>Social Work & Community Service</div>
        </div>
        <div class="career-item">
            <div class="career-icon">🌱</div>
            <div>Environmental Management & Conservation</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Additional information about the system
st.markdown("""
<div style="background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-top: 30px; text-align: center;">
    <h3 style="color: #495057;">Early Guidance for Future Success</h3>
    <p>
        Our system provides guidance, not limitations. We believe that identifying strengths early helps 
        students explore and develop their talents, while still maintaining the freedom to explore diverse interests.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <p>© 2025 Career Recommendation System | Based on Elementary Subject Performance</p>
</div>
""", unsafe_allow_html=True)