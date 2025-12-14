
from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def sigma_k(k, mu):
    return mu - (1 - k**2)**2

@app.route("/", methods=["GET", "POST"])
def index():
    mu = float(request.form.get("mu", 0.5))
    k = np.linspace(0, 2.5, 400)
    sigma = sigma_k(k, mu)

    plt.figure()
    plt.plot(k, sigma)
    plt.axhline(0, linestyle="--")
    plt.xlabel("k")
    plt.ylabel("σ(k)")
    plt.title(f"Análise de Estabilidade (μ = {mu})")
    img_path = os.path.join("static", "plot.png")
    plt.savefig(img_path)
    plt.close()

    return render_template("index.html", mu=mu)

if __name__ == "__main__":
    app.run(debug=True)
