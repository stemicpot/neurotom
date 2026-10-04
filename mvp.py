from flask import Flask, render_template_string
import os

app = Flask(__name__)


class Node:
    def __init__(self, name):
        self.name = name

    def compute(self, state):
        return {
            "node": self.name,
            "input": state,
            "computation": f"{self.name} processed the state"
        }

    def observe(self, computation):
        return {
            "observer": self.name,
            "observed": computation
        }


A = Node("A")
B = Node("B")
C = Node("C")

nodes = [A, B, C]


def run_spiral():

    state = {
        "engram": "tuna",
        "history": []
    }

    steps = []

    for step in range(9):

        current = nodes[step % 3]
        next_node = nodes[(step + 1) % 3]
        witness = nodes[(step + 2) % 3]

        computation = current.compute(state)
        realization = next_node.observe(computation)

        state = {
            "previous": state,
            "computation": computation,
            "realization": realization
        }

        steps.append({
            "step": step + 1,
            "current": current.name,
            "observer": next_node.name,
            "witness": witness.name
        })

    return steps


@app.route("/")
def index():

    steps = run_spiral()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Neurotom MVP</title>

        <style>
            body {
                font-family: monospace;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                background: #111;
                color: #eee;
            }

            h1 {
                color: #00ff88;
            }

            .step {
                padding: 10px;
                margin: 6px 0;
                background: #1c1c1c;
                border-left: 3px solid #00ff88;
            }

            .triangle {
                font-size: 28px;
                text-align: center;
                margin: 30px;
                line-height: 1.8;
            }

            .status {
                color: #00ff88;
            }
        </style>
    </head>

    <body>

        <h1>NEUROTOM</h1>

        <p class="status">
            ● MVP v0.1 — RUNNING
        </p>

        <div class="triangle">
                A
               / \\
              /   \\
             B-----C
        </div>

        <h2>Triangular Infinite Spiral</h2>

        <p>
            Fixed topology:
            <strong>A → B → C → A</strong>
        </p>

        <h2>Execution</h2>

        {% for step in steps %}
        <div class="step">
            Step {{ step.step }}:
            {{ step.current }}
            →
            {{ step.observer }}
            →
            {{ step.witness }}
        </div>
        {% endfor %}

    </body>
    </html>
    """

    return render_template_string(html, steps=steps)


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
