import streamlit as st
import face_record

# Page configuration
st.set_page_config(page_title='Attendance System', layout='wide')

# Center the logo
col1, col2, col3 = st.columns(3)
with col2:
    st.image('logo.jpg')

def main():
    st.title("☁️ **Cloud-based Facial Recognition Attendance System** 🚀")
    st.markdown("---")  # Adds a horizontal separator
    st.subheader(f"👤 Author: Akinjisola Esther Omobolanle")
    st.subheader(f"🆔 Matric No: CSC/2022/033")
    display_libraries()

    # Face recognition module
    with st.spinner("Loading Face Recognition"):
        import face_record
        st.success("Data successfully loaded from Redis")


def display_libraries():
    st.markdown("### 📚 Libraries & Technologies Used")

    libraries = [
        {
            "name": "Streamlit",
            "description": "Python library for creating web applications",
            "link": "https://streamlit.io/",
            "color": "#FF4B4B"  # Streamlit's signature red
        },
        {
            "name": "NumPy",
            "description": "Fundamental package for scientific computing in Python",
            "link": "https://numpy.org/",
            "color": "#013243"  # Deep blue
        },
        {
            "name": "Redis",
            "description": "In-memory data structure store, used as a database",
            "link": "https://redis.io/",
            "color": "#D82C20"  # Redis red
        },
        {
            "name": "AWS (Amazon Web Services)",
            "description": "Cloud computing platform",
            "link": "https://aws.amazon.com/",
            "color": "#FF9900"  # AWS orange
        },
        {
            "name": "Pandas",
            "description": "Data manipulation and analysis library",
            "link": "https://pandas.pydata.org/",
            "color": "#150458"  # Deep purple
        },
        {
            "name": "OpenCV",
            "description": "Open-source computer vision and machine learning software library",
            "link": "https://opencv.org/",
            "color": "#5C3EE8"  # Deep violet
        },
        {
            "name": "InsightFace",
            "description": "Deep learning face recognition library",
            "link": "https://github.com/deepinsight/insightface",
            "color": "#0366D6"  # GitHub blue
        },
        {
            "name": "Scikit-learn",
            "description": "Machine learning library for Python",
            "link": "https://scikit-learn.org/",
            "color": "#F89939"  # Scikit-learn orange
        },
        {
            "name": "Streamlit WebRTC",
            "description": "Streamlit component for WebRTC functionality",
            "link": "https://github.com/whitphx/streamlit-webrtc",
            "color": "#61DAFB"  # Bright blue
        }
    ]

    # Custom CSS for colored library cards
    st.markdown("""
        <style>
        .library-card {
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .library-card:hover {
            transform: scale(1.05);
        }
        </style>
        """, unsafe_allow_html=True)

    # Create columns for better layout
    cols = st.columns(3)

    # Display libraries in a grid
    for i, lib in enumerate(libraries):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="library-card" style="background-color: {lib['color']}; color: white;">
                    <h3 style="color: white;">{lib['name']}</h3>
                    <p>{lib['description']}</p>
                    <a href="{lib['link']}" style="color: white; text-decoration: underline;">🌐 Website</a>
                </div>
                """, unsafe_allow_html=True)

    # Optional: Add a note about technologies
    st.markdown("---")



if __name__ == '__main__':
    main()
