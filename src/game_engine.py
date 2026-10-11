from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def run_maze_simulation(use_superposition=True, inject_noise=True, use_quantum_shield=False):
    """
    Simulates quantum maze routing with superposition, 
    environmental noise, and error shielding.
    """
    qc = QuantumCircuit(1, 1)
    
    # 1. Superposition: Split path across top/bottom route
    if use_superposition:
        qc.h(0)
        
    # 2. Quantum Shield / Error Correction: Apply Phase protection
    if use_quantum_shield:
        qc.s(0)  # S-gate (Phase gate) to stabilize phase noise
        
    # 3. Channel Noise Hazard (Bit flip / Decoherence)
    if inject_noise:
        qc.x(0)
        
    # 4. Receiver Measurement (Collapse wave function)
    qc.measure(0, 0)
    
    # Execute simulation
    simulator = AerSimulator()
    job = simulator.run(qc, shots=100)
    counts = job.result().get_counts()
    
    return counts
