"""
Exemple d'utilisation du trio magique : uv + ruff + ty
"""

from typing import Literal

import pandas as pd


def greet(name: str) -> str:
    """
    Fonction simple avec type hints pour démonstration de ty.

    Args:
        name: Le nom à saluer (doit être une string)

    Returns:
        Le message de salutation

    Raises:
        ValueError: Si name est vide après strip()
    """
    name = name.strip()
    if not name:
        raise ValueError("Le nom ne peut pas être vide.")
    return f"Bonjour, {name} !"


def process_data(df: pd.DataFrame) -> dict[str, int]:
    """
    Analyse basique d'un DataFrame avec type hints.

    Args:
        df: DataFrame pandas à analyser

    Returns:
        Dictionnaire avec les statistiques de base
    """
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().sum(),
        "numeric_columns": len(df.select_dtypes(include=["number"]).columns),
    }


def calculate_stats(numbers: list[float]) -> dict[str, float]:
    """
    Calcule des statistiques sur une liste de nombres.

    Args:
        numbers: Liste de nombres à analyser

    Returns:
        Dictionnaire avec mean, min, max

    Raises:
        ValueError: Si la liste est vide
    """
    if not numbers:
        raise ValueError("La liste ne peut pas être vide.")

    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "count": len(numbers),
    }


# Exemple plus avancé avec types Union et Literal pour ty
Style = Literal["italic", "bold", "underline"]


def with_style(line: str, word: str, style: Style) -> str:
    """
    Applique un style à un mot dans une ligne de texte.

    Args:
        line: La ligne de texte
        word: Le mot à styliser
        style: Le style à appliquer

    Returns:
        La ligne avec le style appliqué
    """
    if style == "italic":
        return line.replace(word, f"*{word}*")
    elif style == "bold":
        return line.replace(word, f"__{word}__")
    elif style == "underline":
        position = line.find(word)
        output = line + "\n"
        output += " " * position
        output += "-" * len(word)
        return output
    else:
        # ty devrait détecter que ce cas est impossible avec Literal
        return line


def safe_divide(a: int | float, b: int | float) -> float | None:
    """
    Division sécurisée qui retourne None en cas de division par zéro.

    Args:
        a: Numérateur
        b: Dénominateur

    Returns:
        Le résultat de la division, ou None si division par zéro
    """
    if b == 0:
        return None
    return a / b


def main() -> None:
    """Exemple d'utilisation des fonctions."""
    # Test de la fonction greet
    print(greet("Alice"))

    # Test avec un DataFrame
    df = pd.DataFrame(
        {"A": [1, 2, 3, None], "B": ["x", "y", "z", "w"], "C": [1.1, 2.2, 3.3, 4.4]}
    )

    stats = process_data(df)
    print(f"Statistiques du DataFrame : {stats}")

    # Test avec une liste de nombres
    numbers = [1.5, 2.8, 3.2, 4.1, 5.9]
    calc_stats = calculate_stats(numbers)
    print(f"Statistiques des nombres : {calc_stats}")

    # Test de stylisation
    styled = with_style("ty est un type checker rapide", "rapide", "bold")
    print(f"Texte stylisé : {styled}")

    # Test de division sécurisée
    result = safe_divide(10, 2)
    print(f"10 / 2 = {result}")

    result_zero = safe_divide(10, 0)
    print(f"10 / 0 = {result_zero}")


if __name__ == "__main__":
    main()
