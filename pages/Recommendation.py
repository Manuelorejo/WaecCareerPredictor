import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
import os

# Set page configuration
st.set_page_config(
    page_title="Career Recommendation System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS matching the homepage colors with centered button
def local_css():
    st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    /* Remove the gradient background and match the homepage */
    .stApp {
        background-color: #f8f9fa;
    }
    h1 {
        color: #20c997;
        font-weight: bold;
        padding-bottom: 20px;
        margin-bottom: 30px;
        text-align: center;
    }
    h2, h3 {
        color: #495057;
        margin-top: 30px;
    }
    .subject-input {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .recommendation-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 10px;
        border-left: 5px solid #6c757d;
    }
    .top-recommendation {
        border-left: 5px solid #20c997;
    }
    .stButton>button {
        background-color: #20c997;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.75rem 1.5rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-size: 18px;
        cursor: pointer;
    }
    .stButton>button:hover {
        opacity: 0.9;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
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
    .stRadio > div {
        padding: 10px;
        background-color: white;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    /* Form field styling to match homepage */
    .stNumberInput > div > div > input {
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    .stSelectbox > div > div {
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    /* Footer styling */
    .footer {
        text-align: center;
        color: #6c757d;
        padding-top: 50px;
        font-size: 0.8em;
    }
    /* Center the button */
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('waec_subjects_career_dataset.csv')
    
    # Drop specified columns
    columns_to_drop = [
        'Study_Habits', 'Analytical_Thinking', 'Creative_Thinking', 
        'Communication_Skills', 'Practical_Skills', 'Science_Club', 
        'Debate_Club'
    ]
    
    for col in columns_to_drop:
        if col in data.columns:
            data = data.drop(col, axis=1)
            
    return data

# Train model
@st.cache_resource
def train_model(data):
    # Prepare features and target
    X = data.drop(['StudentID', 'Career_Path'], axis=1)
    y = data['Career_Path']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Define categorical and numerical columns
    categorical_cols = ['Learning_Style', 'Gender']
    numerical_cols = [col for col in X.columns if col not in categorical_cols]
    
    # Create preprocessing pipelines
    numerical_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
    
    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])
    
    # Create the modeling pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=150, random_state=42))
    ])
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, 'career_recommendation_model.pkl')
    
    return model

# Load or train model
def get_model(data):
    model_path = 'career_recommendation_model.pkl'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        return train_model(data)

# Predict careers
def predict_careers(student_data, model, top_n=3):
    student_df = pd.DataFrame([student_data])
    probas = model.predict_proba(student_df)
    classes = model.classes_
    career_probs = [(classes[i], probas[0][i]) for i in range(len(classes))]
    career_probs.sort(key=lambda x: x[1], reverse=True)
    return career_probs[:top_n]

# Map learning style from user-friendly to technical terms
def map_learning_style(user_choice):
    mapping = {
        "I learn best with numbers and logical problems": "Logical-Mathematical",
        "I learn best with pictures, diagrams and visualizations": "Visual-Spatial",
        "I learn best through hands-on activities and movement": "Bodily-Kinesthetic",
        "I learn best when working with others and discussing": "Interpersonal",
        "I learn best through reading and writing": "Verbal-Linguistic",
        "I learn best through self-reflection and independent study": "Intrapersonal",
        "I learn best by studying nature, plants and animals": "Naturalistic"
    }
    return mapping[user_choice]

# Career emoji mapping
def get_career_emoji(career):
    emoji_map = {
        'Computer_Science': '💻',
        'Engineering': '🔧',
        'Medicine': '⚕️',
        'Business': '📊',
        'Arts_Humanities': '🎨',
        'Social_Sciences': '🌍',
        'Education': '📚',
        'Law': '⚖️',
        'Natural_Sciences': '🔬',
        'Technical_Vocational': '🛠️'
    }
    return emoji_map.get(career, '📝')

# Main app
def main():
    # Apply custom CSS
    local_css()
    
    # App header with logo and title using the homepage styling
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://img.icons8.com/ios-filled/100/20c997/graduation-cap.png", width=80)
    with col2:
        st.markdown("<h1 class='title'>Career Path Recommendation System</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='subtitle'>Find your ideal career based on WAEC examination results</h2>", unsafe_allow_html=True)
    
    # Load data
    data = load_data()
    
    # Automatically train/load model in the background
    model = get_model(data)
    
    # Get subject names
    subject_cols = [col for col in data.columns if col not in ['StudentID', 'Career_Path', 'Gender', 'Learning_Style']]
    
    # Create a card-like container for the form
    st.markdown('<div class="subject-input">', unsafe_allow_html=True)
    
    # Create a form for input
    with st.form("student_form"):
        st.markdown("#### Enter your WAEC examination scores")
        st.write("Enter scores for each subject (0-100)")
        
        student_data = {}
        
        # Create three columns for better layout
        cols = st.columns(3)
        
        # Split subjects among columns
        subjects_per_col = len(subject_cols) // 3 + 1
        
        for i, subject in enumerate(subject_cols):
            col_idx = i // subjects_per_col
            with cols[col_idx]:
                student_data[subject] = st.number_input(
                    f"{subject}", 
                    min_value=0, 
                    max_value=100, 
                    value=70, 
                    step=1,
                    key=f"input_{subject}"
                )
        
        st.markdown("#### Learning Preferences")
        
        # Learning style with simplified options and nice formatting
        learning_style_options = [
            "I learn best with numbers and logical problems",
            "I learn best with pictures, diagrams and visualizations",
            "I learn best through hands-on activities and movement",
            "I learn best when working with others and discussing",
            "I learn best through reading and writing",
            "I learn best through self-reflection and independent study",
            "I learn best by studying nature, plants and animals"
        ]
        
        learning_choice = st.radio("How do you prefer to learn?", learning_style_options)
        student_data['Learning_Style'] = map_learning_style(learning_choice)
        
        # Gender with a more compact layout
        student_data['Gender'] = st.selectbox("Gender", ["Male", "Female"])
        
        # Submit button with proper centering using a custom container
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        submitted = st.form_submit_button("Get My Career Recommendations")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted:
        # Predict careers
        recommendations = predict_careers(student_data, model)
        
        # Display recommendations with nice formatting
        st.markdown("<h3 style='text-align: center; color: #495057;'>Your Recommended Career Paths</h3>", unsafe_allow_html=True)
        st.write("Based on your academic performance, here are your top career matches:")
        
        # Display each recommendation as a card
        for i, (career, prob) in enumerate(recommendations):
            emoji = get_career_emoji(career)
            card_class = "recommendation-card top-recommendation" if i == 0 else "recommendation-card"
            
            st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
            
            if i == 0:
                st.markdown(f"#### {i+1}. {emoji} {career.replace('_', ' ')} - Top Match!")
            else:
                st.markdown(f"#### {i+1}. {emoji} {career.replace('_', ' ')}")
            
            # Confidence bar
            st.progress(float(prob))
            st.write(f"Confidence: {prob:.1%}")
            
            # Optional: Add career descriptions here
            if career == 'Computer_Science':
                st.write("A career in Computer Science involves software development, system analysis, and solving complex problems with technology.")
            elif career == 'Engineering':
                st.write("Engineers design, build and maintain structures, machines, systems, and processes using scientific principles.")
            elif career == 'Medicine':
                st.write("Medical professionals diagnose, treat, and prevent illness, disease, and injury in patients.")
            elif career == 'Business':
                st.write("Business careers involve managing organizations, marketing products, analyzing finances, and developing strategies.")
            elif career == 'Arts_Humanities':
                st.write("Careers in arts and humanities focus on creative expression, cultural understanding, and communication.")
            elif career == 'Social_Sciences':
                st.write("Social scientists study human behavior, relationships, societies, and cultures to understand social patterns.")
            elif career == 'Education':
                st.write("Educators teach, mentor, and develop learning programs to help students acquire knowledge and skills.")
            elif career == 'Law':
                st.write("Legal professionals interpret laws, analyze cases, represent clients, and ensure justice is properly served.")
            elif career == 'Natural_Sciences':
                st.write("Natural scientists study the physical world through observation, experimentation, and theoretical analysis.")
            elif career == 'Technical_Vocational':
                st.write("Technical careers involve specialized skills in areas like construction, manufacturing, and technical services.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.write("")  # Add some space
            
    # Footer matching the homepage style
    st.markdown("---")
    st.markdown("""
    <div class="footer">
    © 2025 Career Path Recommendation System | Based on Elementary Subject Performance
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()