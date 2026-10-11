# Quantum Maze Escape 🧩

An interactive web application built with Python, Qiskit, and Streamlit that simulates a quantum data packet navigating through noisy communication channels. 

The goal of this project was to take abstract quantum computing mechanics—like superposition, wave function collapse, and noise mitigation—and turn them into a fun, hands-on visual experience.

## 🚀 What It Does

In **Quantum Maze Escape**, you guide a data packet through a communication grid. Because the channel is vulnerable to environmental noise, you can leverage quantum principles to successfully route and protect your signal:

* **Superposition Routing:** Uses Hadamard gates (H gate) to explore multiple paths at once, splitting your signal to bypass obstacles.
* **Quantum Shielding:** Applies Phase gates (S gate) as an error-mitigation defense against atmospheric noise and decoherence.
* **Live Probability Simulation:** Powered by the Qiskit Aer backend to simulate real-time measurement outcomes and render distribution charts instantly.

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit
* **Quantum Engine:** Qiskit, Qiskit Aer
* **Language:** Python

## ⚙️ How to Run Locally

If you want to run or test this project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/suhasi14/quantum-maze-escape.git](https://github.com/suhasi14/quantum-maze-escape.git)
   cd quantum-maze-escape
