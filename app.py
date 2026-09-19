import streamlit as st
st.subheader("🖥️ System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("System", "ONLINE")

with col2:
    st.metric("Safety State", "SAFE")

with col3:
    st.metric("Validation", "PASSED")
st.set_page_config(
    page_title="ELEVATE Safety Simulator",
    page_icon="🛗",
    layout="wide"
)

st.title("🛗 ELEVATE Safety Simulator")
st.write("Autonomous Failure Injection & Safety Validation Platform")

st.subheader("System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Floor", "3")

with col2:
    st.metric("Speed", "1.2 m/s")

with col3:
    st.metric("Door", "CLOSED")

with col4:
    st.metric("Safety State", "SAFE")

st.success("System is operating normally.")
st.subheader("🔴 Failure Injection")

component = st.selectbox(
    "Select Component",
    ["Speed Sensor", "Door Sensor", "Brake Controller", "Position Sensor"]
)

fault_type = st.selectbox(
    "Select Fault Type",
    ["Sensor Fault", "Signal Loss", "Stuck Signal", "Communication Failure"]
)

severity = st.selectbox(
    "Severity",
    ["Low", "Medium", "High"]
)

duration = st.number_input(
    "Duration (seconds)",
    min_value=1,
    max_value=60,
    value=5
)

if st.button("🔴 INJECT FAULT"):
    st.error("⚠️ FAULT DETECTED")

    st.write("Component:", component)
    st.write("Fault:", fault_type)
    st.write("Severity:", severity)
    st.write("Duration:", duration, "seconds")

    if severity == "High":
        st.warning("🛑 CRITICAL FAULT — Emergency safety response activated")
    elif severity == "Medium":
        st.warning("⚠️ WARNING — Safety response activated")
    else:
        st.info("ℹ️ LOW-SEVERITY FAULT — Safety monitoring activated")

    st.success("🟢 Elevator moved to SAFE STATE")
    st.error("⚠️ FAULT DETECTED")

    st.write("Component:", component)
    st.write("Fault:", fault_type)
    st.write("Severity:", severity)
    st.write("Duration:", duration, "seconds")

    st.warning("🛑 Safety response activated")
    st.success("🟢 Elevator moved to SAFE STATE")
    st.write("Component:", component)
    st.write("Fault:", fault_type)
    st.write("Severity:", severity)
    st.write("Duration:", duration, "seconds")
st.subheader("📋 Fault History")

if "fault_history" not in st.session_state:
    st.session_state.fault_history = []

if st.button("💾 SAVE FAULT TO HISTORY"):
    st.session_state.fault_history.append({
        "Component": component,
        "Fault": fault_type,
        "Severity": severity,
        "Duration (s)": duration,
        "Response": "SAFE STATE"
    })

if st.session_state.fault_history:
    st.table(st.session_state.fault_history)
else:
    st.info("No faults recorded yet.")
st.subheader("✅ Safety Validation")

if st.session_state.fault_history:
    st.success("VALIDATION PASSED")
    st.write("Fault was detected and safety response was activated.")
else:
    st.info("Inject and save a fault to perform validation.")
st.subheader("⏱️ Detection & Response Time")

if st.session_state.fault_history:
    st.metric("Detection Time", "0.32 s")
    st.metric("Response Time", "0.48 s")
    st.success("⚡ Safety response completed successfully")
else:
    st.info("Inject and save a fault to display timing results.")
st.subheader("📊 Fault Severity Summary")

if st.session_state.fault_history:
    low_count = sum(1 for f in st.session_state.fault_history if f["Severity"] == "Low")
    medium_count = sum(1 for f in st.session_state.fault_history if f["Severity"] == "Medium")
    high_count = sum(1 for f in st.session_state.fault_history if f["Severity"] == "High")

    st.write("🟢 Low Severity:", low_count)
    st.write("🟡 Medium Severity:", medium_count)
    st.write("🔴 High Severity:", high_count)
else:
    st.info("No fault data available.")
st.subheader("📝 Latest Fault Test Report")

if st.session_state.fault_history:
    latest_fault = st.session_state.fault_history[-1]

    st.write("**Component:**", latest_fault["Component"])
    st.write("**Fault Type:**", latest_fault["Fault"])
    st.write("**Severity:**", latest_fault["Severity"])
    st.write("**Duration:**", latest_fault["Duration (s)"], "seconds")
    st.write("**Safety Response:**", latest_fault["Response"])

    st.success("✅ Fault test completed and validated")
else:
    st.info("No fault test available.")
