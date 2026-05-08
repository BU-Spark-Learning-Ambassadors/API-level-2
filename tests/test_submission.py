import os
import subprocess

SCRIPT_NAME = "pokedex.py"

def read_code():
    with open(SCRIPT_NAME, "r") as f:
        return f.read()

def test_script_exists():
    assert os.path.exists(SCRIPT_NAME), "pokedex.py is missing"

def test_no_blanks_left():
    code = read_code()
    assert "____" not in code, "There are unfinished blanks in the code"

def test_uses_requests():
    code = read_code()

    assert "requests.get" in code, "You should use requests.get()"
    assert "status_code" in code, "You should check response.status_code"
    assert ".json()" in code, "You should parse the API response using .json()"

def test_program_runs():
    result = subprocess.run(
        ["python", SCRIPT_NAME],
        input="pikachu\n",
        capture_output=True,
        text=True,
        timeout=20
    )

    assert result.returncode == 0, f"Program crashed:\n{result.stderr}"

def test_output_contains_pokemon_data():
    result = subprocess.run(
        ["python", SCRIPT_NAME],
        input="pikachu\n",
        capture_output=True,
        text=True,
        timeout=20
    )

    output = result.stdout.lower()

    assert "pikachu" in output, "Output should contain the Pokémon name"