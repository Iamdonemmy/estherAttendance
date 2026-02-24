# # home.py
# import streamlit as st
# from utils.auth import init_session_state
#
# # Initialize session state and check auth
# init_session_state()
# if not st.session_state.get('authenticated', False):
#     st.warning("Please login to access the system")
#     st.stop()  # Stop execution if not authenticated
#
# # Page configuration
# st.set_page_config(page_title='Attendance System', layout='wide')
#
#
# def main():
#     # Center the logo
#     col1, col2, col3 = st.columns(3)
#     with col2:
#         st.image('logo.jpg')
#
#     st.title("☁️ **Cloud-based Facial Recognition Attendance System** 🚀")
#     st.markdown("---")
#     st.subheader(f"👤 Author: Akinjisola Esther Omobolanle")
#     st.subheader(f"🆔 Matric No: CSC/2022/033")
#
#     # Logout button in sidebar
#     st.sidebar.markdown(f"**Logged in as:** admin")
#     if st.sidebar.button("Logout"):
#         st.session_state.authenticated = False
#         st.rerun()
#
#     # Face recognition module
#     with st.spinner("Loading Face Recognition"):
#         import face_record
#         st.success("Data successfully loaded from Redis")
#
#
# if __name__ == '__main__':
#     main()


import streamlit as st
# from utils.auth import init_session_state
import time
import face_record  # Import moved to top level
from datetime import datetime, timedelta

# Initialize session state and check auth
# init_session_state()
# if not st.session_state.get('authenticated', False):
#     st.warning("Please login to access the system")
#     st.stop()

# Page configuration
st.set_page_config(
    page_title='Attendance System',
    layout='wide',
    page_icon="👨‍🎓"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.header {
    background: linear-gradient(135deg, #6e8efb, #a777e3);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

.feature-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
    border-left: 4px solid #6e8efb;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}

.sidebar-user {
    text-align: center;
    padding: 1rem;
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    border-radius: 10px;
    margin-bottom: 1.5rem;
}

.logo-container {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)


def main():
    # Sidebar User Info
    # Update the Quick Stats section in your home.py (inside the sidebar)
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-user">
            <h3>👨‍💼 Admin Dashboard</h3>
            <p>Welcome back, <strong>admin</strong></p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.experimental_rerun()

        st.markdown("---")
        st.markdown("### 📊 Quick Stats")

        try:
            # Get dynamic data
            redis_face_db = face_record.retrieve_data()
            logs_list = face_record.r.lrange('emma:logs', 0, -1)

            # Calculate stats
            total_students = len(redis_face_db[redis_face_db['Role'] == 'Student'])
            total_teachers = len(redis_face_db[redis_face_db['Role'] == 'Teacher'])

            # Today's attendance calculation
            today = datetime.now().date()
            today_attendance = 0
            unique_attendees_today = set()

            for log in logs_list:
                try:
                    log_data = log.decode().split('@')
                    if len(log_data) >= 4:  # Ensure log has all required parts
                        log_time = datetime.strptime(log_data[3], '%Y-%m-%d %H:%M:%S.%f').date()
                        if log_time == today:
                            unique_attendees_today.add(log_data[0])  # Add name to set
                except Exception as e:
                    print(f"Skipping malformed log entry: {log}")

            attendance_percentage = 0
            if total_students > 0:
                attendance_percentage = round((len(unique_attendees_today) / total_students * 100))

                # New registrations (simplified version)
                new_registrations = "N/A"  # Default if we can't track

                col1, col2 = st.columns(2)
                col1.metric("Total Students", total_students)
                col2.metric("Today's Attendance", f"{attendance_percentage}%",
                            f"{len(unique_attendees_today)} present")

                # Additional metrics
                st.metric("Total Teachers", total_teachers)

        except Exception as e:
            st.error(f"Error loading stats: {str(e)}")
            col1, col2 = st.columns(2)
            col1.metric("Total Students", "N/A")
            col2.metric("Today's Attendance", "N/A")

        with st.expander("ℹ️ System Info"):
            st.write("**Version:** 2.1.0")
            st.write("**Last Updated:** Today")
            st.write("**Database:** Redis Cloud")

    # Main Content
    with st.container():
        st.markdown("""
        <div class="header">
            <h1 style="margin:0;">☁️ Cloud-based Facial Recognition Attendance System</h1>
            <p style="margin:0; opacity:0.8;">Modern solution for automated attendance tracking</p>
        </div>
        """, unsafe_allow_html=True)

        # Logo with animation - Replace 'logo.jpg' with your actual logo file
        import base64
        import os

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(BASE_DIR, "logo.jpg")

        # Convert image to base64
        with open(logo_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()

        st.markdown(f"""
        <div class="logo-container">
            <img src="data:image/jpg;base64,{encoded}" width="200"
                 style="border-radius: 10px;">
        </div>
        """, unsafe_allow_html=True)


        # Author Info with columns
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.markdown("""
                <div class="feature-card">
                    <h3>👤 Author</h3>
                    <p>Abiodun Emmanuel Seun</p>
                    <p style="color: #666;">FTP/CSC/25/0114410</p>
                </div>
                """, unsafe_allow_html=True)

        with col2:
            with st.container():
                st.markdown("""
                <div class="feature-card">
                    <h3>🏫 Institution</h3>
                    <p>Federal University Oye-Ekiti</p>
                    <p style="color: #666;">Computer Science Department</p>
                </div>
                """, unsafe_allow_html=True)
        # Features Section
        st.markdown("## ✨ Key Features")

        features = [
            {"icon": "👨‍🎓", "title": "Real-time Face Recognition", "desc": "Instant identification with 98% accuracy",
             "bg": "#f0f4ff"},
            {"icon": "📊", "title": "Automated Reports", "desc": "Generate attendance reports with one click",
             "bg": "#f5fff4"},
            {"icon": "☁️", "title": "Cloud Storage", "desc": "Secure Redis data storage", "bg": "#fff4f9"},
            {"icon": "🔒", "title": "Admin Dashboard", "desc": "Full control and monitoring capabilities",
             "bg": "#fff9f0"}
        ]

        cols = st.columns(2)

        for i, feature in enumerate(features):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="feature-card" 
                     style="background: {feature['bg']};">
                    <h2>{feature['icon']} {feature['title']}</h2>
                    <p>{feature['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

        # System Status with Face Recognition Integration
        with st.expander("🖥️ System Status", expanded=True):
            progress_bar = st.progress(0)
            status_text = st.empty()

            for i in range(101):
                progress_bar.progress(i)
                status_text.text(f"System Initializing... {i}%")
                time.sleep(0.01)

            # Face recognition module integration from original version
            with st.spinner("Loading Face Recognition Model..."):
                try:
                    # This will automatically use the existing face_record import
                    redis_face_db = face_record.retrieve_data()
                    status_text.success("✅ System Ready - All components operational")

                    st.markdown(f"""
                    <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px;">
                        <h4>📶 Connection Status</h4>
                        <p>Redis Database: <span style="color: green;">Connected ({len(redis_face_db)} records loaded)</span></p>
                        <p>Face Recognition Model: <span style="color: green;">Loaded</span></p>
                        <p>Cloud Storage: <span style="color: green;">Active</span></p>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    status_text.error(f"❌ System Error: {str(e)}")
                    st.error("Failed to load face recognition data from Redis")


if __name__ == '__main__':
    main()