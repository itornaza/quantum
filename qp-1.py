#
# qiskit
#

# Import necessary Qiskit modules
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to the qubit to create a superposition
qc.h(0)

# Measure the qubit into the classical bit
qc.measure(0, 0)

# Simulate the circuit using the QASM simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()

# Get the measurement counts
counts = result.get_counts()

# Print the circuit and results
print("Circuit:")
print(qc)
print("\nMeasurement counts:", counts)

# Visualize the results
plot_histogram(counts)