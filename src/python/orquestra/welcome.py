"""
This module prints a welcome message.
"""

def welcome():
    print("Welcome to Orquestra!")

def test_artifact():

    with open("/app/test_artifact.json", "w") as f:
        f.write('{"star": "wars", "characters": ["yoda", "darth vader", "solo", "r2d2"], "schema": "io-ZapOS-smoke-test-movie-characters"}')