"""
NEUROTOM — MVP
Triangular Infinite Spiral Observation

MVP v0.1

Core idea:
    Fixed triangular topology:
            A
           / \
          /   \
         B-----C

    Coupled computational configuration:
        A → B → C → A

The goal of this MVP is to establish the basic state-transition
mechanism before introducing neural networks, large-scale memory,
or hardware.
"""


class Node:
    def __init__(self, name):
        self.name = name

    def compute(self, state):
        """Process the current computational state."""
        return {
            "node": self.name,
            "input": state,
            "computation": f"{self.name} processed the state"
        }

    def observe(self, computation):
        """Observe the previous node's computational state."""
        return {
            "observer": self.name,
            "observed": computation
        }


# ------------------------------------------------------------
# 1. CREATE THE THREE NODES
# ------------------------------------------------------------

A = Node("A")
B = Node("B")
C = Node("C")

nodes = [A, B, C]


# ------------------------------------------------------------
# 2. INITIAL COMPUTATIONAL STATE
# ------------------------------------------------------------

state = {
    "engram": "tuna",
    "history": []
}


# ------------------------------------------------------------
# 3. TRIANGULAR SPIRAL
# ------------------------------------------------------------

for step in range(9):

    current = nodes[step % 3]
    next_node = nodes[(step + 1) % 3]
    witness = nodes[(step + 2) % 3]

    # Current node performs computation.
    computation = current.compute(state)

    # Next node observes the current computation.
    realization = next_node.observe(computation)

    # The observed/realized state becomes part of the
    # next computational state.
    state = {
        "previous": state,
        "computation": computation,
        "realization": realization
    }

    print(
        f"Step {step + 1}: "
        f"{current.name} → {next_node.name} → {witness.name}"
    )


# ------------------------------------------------------------
# END
# ------------------------------------------------------------

print("\nNeurotom MVP completed.")
