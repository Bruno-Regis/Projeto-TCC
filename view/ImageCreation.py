import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

def create_equation_image(equation: str, output_path: str):
    """Gera uma imagem de uma equação matemática usando Matplotlib."""
    plt.figure(figsize=(6, 1))
    plt.text(0.5, 0.5, f"${equation}$", horizontalalignment='center', verticalalignment='center', fontsize=18)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', dpi=150)
    plt.close()

# Gerando imagens para as equações
create_equation_image(r"\frac{(x - i)^2}{a^2} + \frac{(y - j)^2}{b^2} = 1", "ellipse_eq.png")
create_equation_image(r"\hat{Z}(x) = \frac{\sum_{i=1}^{n} \frac{Z(x_i)}{d_{ij}^p}}{\sum_{i=1}^{n} \frac{1}{d_{ij}^p}}", "idw_eq.png")
