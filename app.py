import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import random
import time
import os

# ========== PAGE CONFIGURATION ==========
st.set_page_config(
    page_title="Smart Lab Automation System", 
    layout="wide",
    page_icon="🔬",
    initial_sidebar_state="expanded"
)

# ========== DATA DIRECTORY ==========
DATA_DIR = "lab_data"
os.makedirs(DATA_DIR, exist_ok=True)

# ========== PROFESSIONAL CUSTOM CSS ==========
st.markdown("""
<style>
    /* Main Background - Light Gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
    }
    
    /* Sidebar - Professional Dark Blue Gradient */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f2b3d 0%, #1a3a4f 100%) !important;
        box-shadow: 2px 0 10px rgba(0,0,0,0.1);
    }
    
    /* Sidebar Text - Clean White with Opacity */
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Sidebar Title Styling */
    section[data-testid="stSidebar"] h1 {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        border-bottom: 2px solid #00b4d8 !important;
        display: inline-block !important;
        padding-bottom: 8px !important;
    }
    
    /* Sidebar Radio Buttons - Professional Look */
    section[data-testid="stSidebar"] .stRadio label {
        color: #e0e0e0 !important;
        font-weight: 500 !important;
        padding: 8px 12px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }
    
    section[data-testid="stSidebar"] .stRadio label:hover {
        background-color: rgba(0, 180, 216, 0.2) !important;
        color: #00b4d8 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:checked + label {
        background-color: #00b4d8 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }
    
    /* Sidebar Selectbox */
    section[data-testid="stSidebar"] .stSelectbox label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox div {
        background-color: rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }
    
    /* Buttons - Professional Gradient */
    .stButton > button {
        background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(0,180,216,0.4) !important;
        background: linear-gradient(135deg, #00c8e8 0%, #0088c8 100%) !important;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #0f2b3d !important;
        font-weight: 600 !important;
    }
    
    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #0077b6 !important;
    }
    
    div[data-testid="stMetricLabel"] {
        font-weight: 600 !important;
        color: #0f2b3d !important;
    }
    
    /* Workstation Cards - Modern Design */
    .workstation-available {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%) !important;
        padding: 12px !important;
        border-radius: 12px !important;
        text-align: center !important;
        margin: 5px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        transition: transform 0.2s ease !important;
        border-left: 4px solid #28a745 !important;
    }
    
    .workstation-inuse {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%) !important;
        padding: 12px !important;
        border-radius: 12px !important;
        text-align: center !important;
        margin: 5px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        transition: transform 0.2s ease !important;
        border-left: 4px solid #ffc107 !important;
    }
    
    .workstation-maintenance {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%) !important;
        padding: 12px !important;
        border-radius: 12px !important;
        text-align: center !important;
        margin: 5px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        transition: transform 0.2s ease !important;
        border-left: 4px solid #dc3545 !important;
    }
    
    .workstation-offline {
        background: linear-gradient(135deg, #e2e3e5 0%, #d6d8db 100%) !important;
        padding: 12px !important;
        border-radius: 12px !important;
        text-align: center !important;
        margin: 5px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        transition: transform 0.2s ease !important;
        border-left: 4px solid #6c757d !important;
    }
    
    .workstation-available:hover, .workstation-inuse:hover,
    .workstation-maintenance:hover, .workstation-offline:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background-color: #f8f9fa !important;
        border-radius: 10px !important;
        border-left: 4px solid #00b4d8 !important;
    }
    
    /* Info Boxes */
    .stAlert {
        border-radius: 10px !important;
        border-left: 4px solid #00b4d8 !important;
    }
    
    /* Dataframe Styling */
    .dataframe {
        border-radius: 10px !important;
        overflow: hidden !important;
    }
    
    /* Card-like containers */
    .css-1r6slb0 {
        background-color: rgba(255,255,255,0.7) !important;
        border-radius: 15px !important;
        padding: 5px !important;
    }
    
    /* Mobile Responsive Adjustments */
    @media (max-width: 768px) {
        .workstation-available, .workstation-inuse,
        .workstation-maintenance, .workstation-offline {
            padding: 6px !important;
            font-size: 10px !important;
        }
        div[data-testid="stMetricValue"] {
            font-size: 1.2rem !important;
        }
        h1 {
            font-size: 1.5rem !important;
        }
    }
    
    /* Success/Warning/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%) !important;
        border-left: 4px solid #28a745 !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%) !important;
        border-left: 4px solid #ffc107 !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%) !important;
        border-left: 4px solid #dc3545 !important;
    }
    
    /* Info Box */
    .stInfo {
        background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%) !important;
        border-left: 4px solid #17a2b8 !important;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 10px 10px 0 0;
        padding: 8px 20px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%) !important;
        color: white !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #6c757d;
        font-size: 12px;
        border-top: 1px solid #dee2e6;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# ========== INITIALIZE DATA FILES ==========
def init_data_files():
    # Laboratories table
    if not os.path.exists(os.path.join(DATA_DIR, "laboratories.csv")):
        labs = pd.DataFrame([{
            "lab_id": 1, 
            "lab_name": "Computer Lab A", 
            "building": "Science Block", 
            "total_workstations": 20, 
            "is_active": True
        }])
        labs.to_csv(os.path.join(DATA_DIR, "laboratories.csv"), index=False)
    
    # Workstations table
    if not os.path.exists(os.path.join(DATA_DIR, "workstations.csv")):
        workstations = []
        for i in range(1, 21):
            workstations.append({
                "workstation_id": i, 
                "workstation_name": f"PC-{i:03d}", 
                "lab_id": 1, 
                "status": "available", 
                "ip_address": f"192.168.1.{i}"
            })
        pd.DataFrame(workstations).to_csv(os.path.join(DATA_DIR, "workstations.csv"), index=False)
    
    # Issues table
    if not os.path.exists(os.path.join(DATA_DIR, "issues.csv")):
        pd.DataFrame(columns=["issue_id", "workstation_id", "reported_by", "issue_description", "severity", "status", "reported_at"]).to_csv(os.path.join(DATA_DIR, "issues.csv"), index=False)
    
    # Reservations table
    if not os.path.exists(os.path.join(DATA_DIR, "reservations.csv")):
        pd.DataFrame(columns=["reservation_id", "workstation_id", "reserved_by", "start_time", "end_time", "purpose"]).to_csv(os.path.join(DATA_DIR, "reservations.csv"), index=False)

init_data_files()

# ========== HELPER FUNCTIONS ==========
def get_workstation_status():
    """Get current status of all workstations with random simulation"""
    workstations = pd.read_csv(os.path.join(DATA_DIR, "workstations.csv"))
    # Simulate random status changes for demo
    for idx in workstations.index:
        rand = random.random()
        if rand < 0.65:
            workstations.loc[idx, "status"] = "available"
        elif rand < 0.80:
            workstations.loc[idx, "status"] = "in-use"
        elif rand < 0.92:
            workstations.loc[idx, "status"] = "maintenance"
        else:
            workstations.loc[idx, "status"] = "offline"
    workstations.to_csv(os.path.join(DATA_DIR, "workstations.csv"), index=False)
    return workstations

def get_active_issues():
    """Get all unresolved issues"""
    issues = pd.read_csv(os.path.join(DATA_DIR, "issues.csv"))
    if not issues.empty:
        active = issues[issues["status"] != "resolved"]
        return active
    return pd.DataFrame()

def report_issue(workstation_id, reported_by, description, severity):
    """Create a new issue report"""
    issues = pd.read_csv(os.path.join(DATA_DIR, "issues.csv"))
    new_id = issues["issue_id"].max() + 1 if not issues.empty else 1
    new_issue = pd.DataFrame([{
        "issue_id": new_id,
        "workstation_id": workstation_id,
        "reported_by": reported_by,
        "issue_description": description,
        "severity": severity,
        "status": "open",
        "reported_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    issues = pd.concat([issues, new_issue], ignore_index=True)
    issues.to_csv(os.path.join(DATA_DIR, "issues.csv"), index=False)
    return new_id

def resolve_issue(issue_id):
    """Mark an issue as resolved"""
    issues = pd.read_csv(os.path.join(DATA_DIR, "issues.csv"))
    issues.loc[issues["issue_id"] == issue_id, "status"] = "resolved"
    issues.to_csv(os.path.join(DATA_DIR, "issues.csv"), index=False)

def generate_usage_report():
    """Generate simulated usage statistics"""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    usage = np.random.randint(40, 95, 5)
    return pd.DataFrame({"Day": days, "Usage Percentage": usage})

# ========== SESSION STATE ==========
if "user_role" not in st.session_state:
    st.session_state.user_role = "Technician"

# ========== SIDEBAR NAVIGATION ==========
with st.sidebar:
    st.markdown("### 🔬 Lab Automation")
    st.markdown("### System")
    st.markdown("---")
    
    menu = st.radio("📋 NAVIGATION", [
        "🏠 Dashboard",
        "🖥️ Workstation Status",
        "📝 Report Issue",
        "📋 Issue Tracking",
        "📅 Reservations",
        "📊 Reports",
        "ℹ️ About"
    ])
    
    st.markdown("---")
    st.markdown("### 👤 User")
    user_role = st.selectbox("Select Role", ["Student", "Faculty", "Technician", "Administrator"])
    
    st.markdown("---")
    st.markdown("### 📊 System Info")
    st.markdown("🟢 **Active:** Online")
    st.markdown(f"📅 **Date:** {datetime.now().strftime('%Y-%m-%d')}")
    st.markdown(f"⏰ **Time:** {datetime.now().strftime('%H:%M')}")

# Clean menu names for comparison
menu_clean = menu.replace("🏠 ", "").replace("🖥️ ", "").replace("📝 ", "").replace("📋 ", "").replace("📅 ", "").replace("📊 ", "").replace("ℹ️ ", "")

# ========== MAIN CONTENT ==========

# PAGE 1: DASHBOARD
if menu_clean == "Dashboard":
    st.markdown("# 🏫 Laboratory Monitoring Dashboard")
    st.markdown("---")
    
    workstations = get_workstation_status()
    active_issues = get_active_issues()
    
    # Metrics Row - Professional Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💻 Total Workstations", len(workstations), delta=None)
    with col2:
        available = len(workstations[workstations["status"] == "available"])
        st.metric("🟢 Available", available, delta=f"{int(available/len(workstations)*100)}%")
    with col3:
        in_use = len(workstations[workstations["status"] == "in-use"])
        st.metric("🟡 In Use", in_use)
    with col4:
        issues = len(workstations[workstations["status"] == "maintenance"]) + len(workstations[workstations["status"] == "offline"])
        st.metric("🔴 Needs Attention", issues, delta="Urgent" if issues > 0 else None)
    
    st.markdown("---")
    st.markdown("## 🗺️ Laboratory Map")
    st.caption("Real-time workstation status - Updated automatically")
    
    # Workstation Grid Display - Responsive
    cols = st.columns(5)
    for idx, (_, ws) in enumerate(workstations.iterrows()):
        col = cols[idx % 5]
        with col:
            if ws["status"] == "available":
                st.markdown(f'<div class="workstation-available">🟢<br><b>{ws["workstation_name"]}</b><br>Available</div>', unsafe_allow_html=True)
            elif ws["status"] == "in-use":
                st.markdown(f'<div class="workstation-inuse">🟡<br><b>{ws["workstation_name"]}</b><br>In Use</div>', unsafe_allow_html=True)
            elif ws["status"] == "maintenance":
                st.markdown(f'<div class="workstation-maintenance">🔴<br><b>{ws["workstation_name"]}</b><br>Maintenance</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="workstation-offline">⚫<br><b>{ws["workstation_name"]}</b><br>Offline</div>', unsafe_allow_html=True)
    
    # Active Alerts Section
    if not active_issues.empty:
        st.markdown("---")
        st.markdown("## ⚠️ Active Issues")
        for _, issue in active_issues.iterrows():
            st.warning(f"**PC-{issue['workstation_id']:03d}** - {issue['issue_description']}  \n📅 Reported: {issue['reported_at']}")

# PAGE 2: WORKSTATION STATUS
elif menu_clean == "Workstation Status":
    st.markdown("# 🖥️ Workstation Status Details")
    st.markdown("---")
    
    workstations = get_workstation_status()
    
    status_filter = st.selectbox("🔍 Filter by Status", ["All", "Available", "In Use", "Maintenance", "Offline"])
    
    if status_filter != "All":
        filtered = workstations[workstations["status"] == status_filter.lower()]
    else:
        filtered = workstations
    
    st.dataframe(filtered[["workstation_name", "status", "ip_address"]], use_container_width=True)
    
    # Status Pie Chart
    st.markdown("---")
    st.markdown("### 📊 Status Distribution")
    status_counts = workstations["status"].value_counts()
    fig = px.pie(values=status_counts.values, names=status_counts.index, title="Workstation Status Distribution", color_discrete_sequence=['#28a745', '#ffc107', '#dc3545', '#6c757d'])
    st.plotly_chart(fig, use_container_width=True)

# PAGE 3: REPORT ISSUE
elif menu_clean == "Report Issue":
    st.markdown("# 📝 Report Equipment Issue")
    st.markdown("---")
    
    workstations = pd.read_csv(os.path.join(DATA_DIR, "workstations.csv"))
    workstation_options = [f"{w['workstation_name']}" for _, w in workstations.iterrows()]
    selected = st.selectbox("🖥️ Select Workstation", workstation_options)
    workstation_id = int(selected.split("-")[1])
    
    with st.form("issue_form"):
        reporter_name = st.text_input("👤 Your Name / ID")
        issue_desc = st.text_area("📝 Describe the issue in detail", height=100)
        severity = st.selectbox("⚠️ Severity Level", ["Low", "Medium", "High", "Critical"])
        
        submitted = st.form_submit_button("🚀 Submit Report", use_container_width=True)
        
        if submitted:
            if reporter_name and issue_desc:
                issue_id = report_issue(workstation_id, reporter_name, issue_desc, severity)
                st.success(f"✅ Issue #{issue_id} reported successfully! A technician will address it soon.")
                st.balloons()
            else:
                st.error("❌ Please fill all required fields")

# PAGE 4: ISSUE TRACKING
elif menu_clean == "Issue Tracking":
    st.markdown("# 📋 Issue Tracking System")
    st.markdown("---")
    
    issues = pd.read_csv(os.path.join(DATA_DIR, "issues.csv"))
    
    if not issues.empty:
        for _, issue in issues.iterrows():
            with st.expander(f"🔧 Issue #{issue['issue_id']} - PC-{issue['workstation_id']:03d} - {issue['status'].upper()}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**👤 Reported by:** {issue['reported_by']}")
                    st.markdown(f"**⚠️ Severity:** {issue['severity']}")
                with col2:
                    st.markdown(f"**📅 Reported at:** {issue['reported_at']}")
                st.markdown(f"**📝 Description:** {issue['issue_description']}")
                
                if user_role in ["Technician", "Administrator"] and issue['status'] != "resolved":
                    if st.button(f"✅ Mark Resolved", key=f"res_{issue['issue_id']}"):
                        resolve_issue(issue['issue_id'])
                        st.success("Issue marked as resolved!")
                        st.rerun()
    else:
        st.info("✨ No issues reported. All systems are running normally.")

# PAGE 5: RESERVATIONS
elif menu_clean == "Reservations":
    st.markdown("# 📅 Laboratory Reservations")
    st.markdown("---")
    
    if user_role in ["Faculty", "Administrator"]:
        with st.form("reservation_form"):
            purpose = st.text_input("📚 Course Name / Purpose")
            col1, col2 = st.columns(2)
            with col1:
                date = st.date_input("📅 Date")
                start_time = st.time_input("⏰ Start Time")
            with col2:
                end_time = st.time_input("⏰ End Time")
                num_workstations = st.number_input("💻 Number of Workstations", min_value=1, max_value=20, value=10)
            
            submitted = st.form_submit_button("📅 Request Reservation", use_container_width=True)
            
            if submitted:
                if purpose:
                    st.success(f"✅ Reservation submitted for {purpose} on {date} from {start_time} to {end_time}")
                else:
                    st.error("❌ Please enter a purpose for the reservation")
    else:
        st.info("👨‍🏫 **Faculty and Administrators** can make laboratory reservations. Please contact your lab administrator.")
    
    st.markdown("---")
    st.markdown("### 📅 Upcoming Reservations")
    st.info("No upcoming reservations scheduled at this time.")

# PAGE 6: REPORTS
elif menu_clean == "Reports":
    st.markdown("# 📊 Laboratory Reports")
    st.markdown("---")
    
    report_type = st.selectbox("📑 Select Report Type", ["Workstation Usage Summary", "Issue History Report", "Maintenance Log"])
    
    if st.button("📄 Generate Report", use_container_width=True):
        with st.spinner("🔄 Generating report..."):
            time.sleep(1)
            
            if report_type == "Workstation Usage Summary":
                usage_data = generate_usage_report()
                st.markdown("### 📈 Weekly Workstation Usage")
                fig = px.bar(usage_data, x="Day", y="Usage Percentage", title="Average Usage by Day", color="Usage Percentage", color_continuous_scale="Blues")
                st.plotly_chart(fig, use_container_width=True)
                
                csv = usage_data.to_csv(index=False)
                st.download_button("💾 Download Report as CSV", csv, "usage_report.csv", "text/csv")
            
            elif report_type == "Issue History Report":
                issues = pd.read_csv(os.path.join(DATA_DIR, "issues.csv"))
                if not issues.empty:
                    st.dataframe(issues, use_container_width=True)
                    csv = issues.to_csv(index=False)
                    st.download_button("💾 Download Issues Report", csv, "issues_report.csv", "text/csv")
                else:
                    st.info("No issues to report")
            
            else:
                st.info("📝 Maintenance log report generated")

# PAGE 7: ABOUT
else:
    st.markdown("# ℹ️ About Smart Laboratory Automation System")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 🔬 System Overview
        An IoT-based platform for real-time computer laboratory monitoring and management.
        
        ### ✨ Key Features
        - **🏠 Real-time workstation status monitoring** - See which computers are available
        - **📝 Automated issue reporting** - Students can report problems instantly
        - **📅 Reservation system** - Faculty can book laboratory sessions
        - **📊 Usage analytics** - Track laboratory utilization patterns
        - **🔧 Maintenance tracking** - Monitor equipment health
        
        ### ⚙️ How It Works
        1. Workstations send status updates to the central server
        2. Environmental sensors monitor temperature and humidity
        3. The dashboard displays real-time information
        4. Alerts notify staff of issues immediately
        5. Reports help with capacity planning
        
        ### 👥 Target Users
        - Laboratory Technicians
        - IT Administrators  
        - Faculty Members
        - Students
        """)
    
    with col2:
        st.markdown("""
        ### 🛠️ Technologies
        | Technology | Purpose |
        |------------|---------|
        | Streamlit | Frontend UI |
        | Python | Backend Logic |
        | CSV | Data Storage |
        | Plotly | Visualizations |
        
        ### 📊 System Stats
        - **Version:** v1.0.0
        - **Status:** Active
        - **Type:** Laboratory Management
        """)
    
    st.markdown("---")
    st.markdown('<div class="footer">© 2024 Smart Laboratory Automation System | Computer Laboratory Edition</div>', unsafe_allow_html=True)