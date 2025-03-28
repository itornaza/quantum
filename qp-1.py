#
# qiskit
#

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# Create a 1-qubit circuit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Hadamard gate
qc.measure(0, 0)  # Measure

# Get the simulator backend
simulator = Aer.get_backend('qasm_simulator')

# Transpile the circuit for the backend
transpiled_circuit = transpile(qc, simulator)

# Run the circuit
job = simulator.run(transpiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

# Output
print("Circuit:")
print(qc)
print("\nMeasurement counts:", counts)
plot_histogram(counts)

