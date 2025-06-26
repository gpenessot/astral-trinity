"""
Tests pour les fonctions d'exemple.
"""

import pandas as pd
import pytest

from src.example import calculate_stats, greet, process_data, safe_divide, with_style


class TestGreet:
    """Tests pour la fonction greet."""

    def test_greet_normal(self):
        """Test avec un nom normal."""
        result = greet("Alice")
        assert result == "Bonjour, Alice !"

    def test_greet_with_spaces(self):
        """Test avec des espaces autour du nom."""
        result = greet("  Bob  ")
        assert result == "Bonjour, Bob !"

    def test_greet_empty_string(self):
        """Test avec une string vide."""
        with pytest.raises(ValueError, match="Le nom ne peut pas être vide"):
            greet("")

    def test_greet_only_spaces(self):
        """Test avec seulement des espaces."""
        with pytest.raises(ValueError, match="Le nom ne peut pas être vide"):
            greet("   ")

    def test_greet_wrong_type(self):
        """Test avec un mauvais type (AttributeError car pas de vérification runtime)."""
        with pytest.raises(AttributeError):
            greet(123)


class TestProcessData:
    """Tests pour la fonction process_data."""

    def test_process_data_normal(self):
        """Test avec un DataFrame normal."""
        df = pd.DataFrame(
            {"A": [1, 2, 3, None], "B": ["x", "y", "z", "w"], "C": [1.1, 2.2, 3.3, 4.4]}
        )

        result = process_data(df)

        assert result["rows"] == 4
        assert result["columns"] == 3
        assert result["missing_values"] == 1
        assert result["numeric_columns"] == 2

    def test_process_data_empty(self):
        """Test avec un DataFrame vide."""
        df = pd.DataFrame()

        result = process_data(df)

        assert result["rows"] == 0
        assert result["columns"] == 0
        assert result["missing_values"] == 0
        assert result["numeric_columns"] == 0

    def test_process_data_wrong_type(self):
        """Test avec un mauvais type (AttributeError car pas de vérification runtime)."""
        with pytest.raises(AttributeError):
            process_data("not a dataframe")


class TestCalculateStats:
    """Tests pour la fonction calculate_stats."""

    def test_calculate_stats_normal(self):
        """Test avec une liste normale."""
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

        result = calculate_stats(numbers)

        assert result["mean"] == 3.0
        assert result["min"] == 1.0
        assert result["max"] == 5.0
        assert result["count"] == 5

    def test_calculate_stats_single_value(self):
        """Test avec une seule valeur."""
        numbers = [42.0]

        result = calculate_stats(numbers)

        assert result["mean"] == 42.0
        assert result["min"] == 42.0
        assert result["max"] == 42.0
        assert result["count"] == 1

    def test_calculate_stats_empty_list(self):
        """Test avec une liste vide."""
        with pytest.raises(ValueError, match="La liste ne peut pas être vide"):
            calculate_stats([])

    def test_calculate_stats_wrong_type(self):
        """Test avec un mauvais type (AttributeError car pas de vérification runtime)."""
        with pytest.raises((TypeError, AttributeError)):
            calculate_stats("not a list")


class TestWithStyle:
    """Tests pour la fonction with_style."""

    def test_with_style_italic(self):
        """Test avec le style italic."""
        result = with_style("Hello world", "world", "italic")
        assert result == "Hello *world*"

    def test_with_style_bold(self):
        """Test avec le style bold."""
        result = with_style("Hello world", "world", "bold")
        assert result == "Hello __world__"

    def test_with_style_underline(self):
        """Test avec le style underline."""
        result = with_style("Hello world", "world", "underline")
        expected = "Hello world\n      -----"
        assert result == expected

    def test_with_style_word_not_found(self):
        """Test quand le mot n'est pas trouvé."""
        result = with_style("Hello world", "python", "italic")
        assert result == "Hello world"  # Pas de changement


class TestSafeDivide:
    """Tests pour la fonction safe_divide."""

    def test_safe_divide_normal(self):
        """Test avec une division normale."""
        result = safe_divide(10, 2)
        assert result == 5.0

    def test_safe_divide_zero(self):
        """Test avec division par zéro."""
        result = safe_divide(10, 0)
        assert result is None

    def test_safe_divide_float(self):
        """Test avec des nombres flottants."""
        result = safe_divide(7.5, 2.5)
        assert result == 3.0

    def test_safe_divide_negative(self):
        """Test avec des nombres négatifs."""
        result = safe_divide(-10, 2)
        assert result == -5.0
