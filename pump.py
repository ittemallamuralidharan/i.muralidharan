import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Pump Performance Calculator",
    page_icon="⚙️",
    layout="centered"
)

# Constants
g = 9.81        # gravitational acceleration (m/s^2)
rho = 1000      # density of water (kg/m^3)

# App Title & Description
st.title("⚙️ Pump Performance Calculator")
st.markdown("Calculate hydraulic power, shaft power, pump efficiency, developed head, and discharge using standard turbomachinery formulas.")

# Sidebar Navigation for Calculation Mode
st.sidebar.header("Calculation Mode")
mode = st.sidebar.selectbox(
    "Select Parameter to Compute:",
    (
        "1. Hydraulic Power",
        "2. Shaft Power",
        "3. Pump Efficiency",
        "4. Head Developed by Pump",
        "5. Discharge"
    )
)

st.divider()

# --- Mode 1: Hydraulic Power ---
if mode == "1. Hydraulic Power":
    st.subheader("💧 Hydraulic Power Calculation")
    st.markdown("Formula: $Ph = \\rho \\cdot g \\cdot Q \\cdot H$")
    
    col1, col2 = st.columns(2)
    with col1:
        Q = st.number_input("Discharge $Q$ (m³/s)", min_value=0.0, value=0.05, step=0.01, format="%.4f")
    with col2:
        H = st.number_input("Head $H$ (m)", min_value=0.0, value=20.0, step=1.0, format="%.2f")
    
    if st.button("Calculate Hydraulic Power", type="primary"):
        Ph = rho * g * Q * H
        st.success(f"**Hydraulic Power:** `{Ph:.2f} W` / `{Ph / 1000:.3f} kW`")

# --- Mode 2: Shaft Power ---
elif mode == "2. Shaft Power":
    st.subheader("⚡ Shaft Power Calculation")
    st.markdown("Formula: $Ps = \\frac{\\rho \\cdot g \\cdot Q \\cdot H}{\\eta}$")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Q = st.number_input("Discharge $Q$ (m³/s)", min_value=0.0, value=0.05, step=0.01, format="%.4f")
    with col2:
        H = st.number_input("Head $H$ (m)", min_value=0.0, value=20.0, step=1.0, format="%.2f")
    with col3:
        eta = st.number_input("Pump Efficiency $\\eta$ (%)", min_value=0.1, max_value=100.0, value=75.0, step=1.0)
    
    if st.button("Calculate Shaft Power", type="primary"):
        eta_dec = eta / 100.0
        Ps = (rho * g * Q * H) / eta_dec
        st.success(f"**Shaft Power:** `{Ps:.2f} W` / `{Ps / 1000:.3f} kW`")

# --- Mode 3: Pump Efficiency ---
elif mode == "3. Pump Efficiency":
    st.subheader("📈 Pump Efficiency Calculation")
    st.markdown("Formula: $\\eta = \\frac{\\rho \\cdot g \\cdot Q \\cdot H}{Ps} \\times 100$")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Q = st.number_input("Discharge $Q$ (m³/s)", min_value=0.0, value=0.05, step=0.01, format="%.4f")
    with col2:
        H = st.number_input("Head $H$ (m)", min_value=0.0, value=20.0, step=1.0, format="%.2f")
    with col3:
        Ps = st.number_input("Shaft Power $Ps$ (W)", min_value=0.1, value=15000.0, step=100.0, format="%.2f")
    
    if st.button("Calculate Efficiency", type="primary"):
        if Ps > 0:
            eta = (rho * g * Q * H) / Ps
            st.success(f"**Pump Efficiency:** `{eta * 100:.2f}%`")
        else:
            st.error("Shaft power must be greater than zero.")

# --- Mode 4: Head Developed ---
elif mode == "4. Head Developed by Pump":
    st.subheader("⛰️ Head Developed Calculation")
    st.markdown("Formula: $H = \\frac{\\eta \\cdot Ps}{\\rho \\cdot g \\cdot Q}$")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Q = st.number_input("Discharge $Q$ (m³/s)", min_value=0.0001, value=0.05, step=0.01, format="%.4f")
    with col2:
        Ps = st.number_input("Shaft Power $Ps$ (W)", min_value=0.1, value=15000.0, step=100.0, format="%.2f")
    with col3:
        eta = st.number_input("Pump Efficiency $\\eta$ (%)", min_value=0.1, max_value=100.0, value=75.0, step=1.0)
    
    if st.button("Calculate Head", type="primary"):
        eta_dec = eta / 100.0
        if Q > 0:
            H = (eta_dec * Ps) / (rho * g * Q)
            st.success(f"**Head Developed:** `{H:.2f} m`")
        else:
            st.error("Discharge must be greater than zero.")

# --- Mode 5: Discharge ---
elif mode == "5. Discharge":
    st.subheader("🌊 Discharge Calculation")
    st.markdown("Formula: $Q = \\frac{\\eta \\cdot Ps}{\\rho \\cdot g \\cdot H}$")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        H = st.number_input("Head $H$ (m)", min_value=0.0001, value=20.0, step=1.0, format="%.2f")
    with col2:
        Ps = st.number_input("Shaft Power $Ps$ (W)", min_value=0.1, value=15000.0, step=100.0, format="%.2f")
    with col3:
        eta = st.number_input("Pump Efficiency $\\eta$ (%)", min_value=0.1, max_value=100.0, value=75.0, step=1.0)
    
    if st.button("Calculate Discharge", type="primary"):
        eta_dec = eta / 100.0
        if H > 0:
            Q = (eta_dec * Ps) / (rho * g * H)
            st.success(f"**Discharge:** `{Q:.4f} m³/s` (`{Q * 1000:.2f} L/s`)")
        else:
            st.error("Head must be greater than zero.")
