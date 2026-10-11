import streamlit as st
from game_engine import run_maze_simulation

st.set_page_config(page_title="Quantum Maze Escape", layout="centered")

st.title("🧩 Quantum Maze Escape")
st.subheader("A Quantum State & Noise Adventure")

st.markdown("""
**Welcome, Player!** Guide your quantum data packet through the communication maze. 
Use **Superposition** to explore two paths simultaneously, and deploy a **Quantum Shield** to block noise traps!
""")

# Sidebar Controls
st.sidebar.header("🕹️ Game Controls")
use_h = st.sidebar.checkbox("🚀 Enable Superposition (Hadamard Gate)", value=True)
use_shield = st.sidebar.checkbox("🛡️ Deploy Quantum Shield (Phase Gate)", value=False)
inject_noise = st.sidebar.checkbox("⚠️ Active Environmental Noise Hazard", value=True)

# Visualizing the Maze Status
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🗺️ Maze Routes")
    st.markdown("""
    * **Path A (Top Route):** Standard Waveguide
    * **Path B (Bottom Route):** Quantum Tunneling Lane
    """)
    if use_h:
        st.info("⚡ Status: Character split into Superposition (Exploring Path A & B simultaneously).")
    else:
        st.warning("🔒 Status: Classical single-path mode. Vulnerable to obstacles.")

with col2:
    st.markdown("### 📊 Metrics")
    st.metric(label="Channel Interference", value="High" if inject_noise else "Low")
    st.metric(label="Error Mitigation", value="Active" if use_shield else "Inactive")

# Run Game Button
if st.button("🚀 Launch Through Maze"):
    counts = run_maze_simulation(use_superposition=use_h, inject_noise=inject_noise, use_quantum_shield=use_shield)
    
    st.subheader("🎯 Transmission Result (100 Shots)")
    st.bar_chart(counts)
    
    # Game outcome logic
    if '0' in counts and '1' in counts and not inject_noise:
        st.success("🎉 **VICTORY!** Your quantum signal successfully navigated both paths and reached the receiver intact!")
    elif use_shield and '0' in counts:
        st.success("🛡️ **SHIELD ENGAGED!** The quantum phase filter successfully blocked the noise trap and secured delivery!")
    elif inject_noise and not use_shield:
        st.error("💥 **SIGNAL DEGRADED!** Unmitigated channel noise caused decoherence. The data packet hit a noise wall!")
    else:
        st.info("🔍 **WAVEFUNCTION COLLAPSED:** Measurement completed successfully across the network grid.")
