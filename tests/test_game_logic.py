from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" with correct direction
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER" in message  # Fixed: was incorrectly "Go HIGHER" before

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" with correct direction
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER" in message  # Fixed: was incorrectly "Go LOWER" before

def test_hint_directions_fixed():
    """Test that the hint directions are correct (the bug that was fixed)."""
    # Too high should suggest going lower
    _, message_high = check_guess(60, 50)
    assert "Go LOWER" in message_high
    assert "Go HIGHER" not in message_high

    # Too low should suggest going higher
    _, message_low = check_guess(40, 50)
    assert "Go HIGHER" in message_low
    assert "Go LOWER" not in message_low
