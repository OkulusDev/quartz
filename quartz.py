#!/usr/bin/env python3
# Quantum Cryptography Example using Qiskit

from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import random_statevector
from qiskit.extensions import Initialize

# Step 1: Generate a random quantum state for Alice
alice_state = random_statevector(2)

# Step 2: Initialize the quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 3: Apply the initialization operation to the first qubit simulating Alice's qubit
init_gate = Initialize(alice_state)
qc.append(init_gate, [0])

# Step 4: Create a Bell pair (entangled qubits)
qc.h(1) # Apply a Hadamard gate to qubit 1
qc.cx(1, 0) # Apply a CNOT gate with control qubit 1 and target qubit 0

# Step 5: Alice sends her qubit to Bob (Simulation of quantum communication)
# In an actual quantum network, qubit 0 would be physically sent to Bob

# Step 6: Measurement of qubits by Bob
qc.barrier() 
qc.cx(1, 0) # Apply another CNOT gate
qc.h(1) # Apply a Hadamard gate again
qc.measure([0, 1], [0, 1]) # Measure both qubits and store the results in the classical bits

# Step 7: Execute the quantum circuit using Qiskit Aer's simulator backend
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1)
result = job.result()
measured_result = result.get_counts(qc)
print(measured_result)

# Final step: Reverse the initialization process (Quantum Teleportation)
teleported_state = init_gate.gates_to_uncompute().inverse()
qc.append(teleported_state, [1])
qc.measure(1, 1)

# Print the quantum circuit for visualization
print(qc)
