from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  result = 7
  # Act
  score = blackjack_score(hand)
  assert score == result
  

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = ["Jack", "Queen"]
  result = 20
  score = blackjack_score(hand)
  
  assert score == result

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = ["Ace", 7, 2]
  result = 20
  score = blackjack_score(hand)
  
  assert score == result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = [10, 10, "Ace"]
  result = 21
  score = blackjack_score(hand)
  
  assert score == result

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = [14, 2]
  result = "Invalid"
  score = blackjack_score(hand)
  
  assert score == result 


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [3, 2, 4, 5, 6, 7]
  result = "Invalid"
  score = blackjack_score(hand)
  
  assert score == result 

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = ["Jack", 9, 5]
  result = "Bust"
  score = blackjack_score(hand)
  
  assert score == result 

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ["Ace", "Ace", "King"]
  result = 12
  score = blackjack_score(hand)
  
  assert score == result 

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  hand = ["Ace", "Ace", "Ace", "Ace"]
  result = 14
  score = blackjack_score(hand)
  
  assert score == result 