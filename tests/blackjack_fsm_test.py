""" 
File: blackjack_fsm_test.py
Author: Alexander Bulanov
"""

# Global Imports
from enum import Enum
import pytest

# Local Imports #
import lib.blackjack_fsm as bjfsm
import lib.blackjack_game_settings as bjs
import lib.blackjack_game_objects as bjo


class Test_WAITING_Seat_Count_Independent:
    def test_blackjack_state_machine_beginning_state_is_WAITING(self):
        # Test
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        assert test_machine.state == bjfsm.GameState.WAITING

class Test_WAITING_One_Seat_per_Player:
    def test_blackjack_state_machine_transitions_to_STARTING_from_WAITING_after_one_player_starts_game(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        # Test
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        assert test_machine.state == bjfsm.GameState.STARTING

    def test_first_player_Alex_successfully_sits_at_chosen_seat_2(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        # Test
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        assert test_machine.seated_players[2].name == 'Alex'

    def test_first_player_Alex_succesfully_adds_then_removes_seat_2_and_sits_at_different_chosen_seat_4(self, monkeypatch):
        pass

    def test_second_player_Jim_denied_sitting_in_Alex_occupied_seat_2(self, monkeypatch):
        pass

    def test_second_player_Jim_denied_sitting_at_Alex_occupied_seat_2_then_successfully_sits_at_different_chosen_seat_3(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        # Test
        simulated_input_values = ['Alex', '2', 'Jim', '2', '3']
        iterable_simulated_input_values = iter(simulated_input_values)
        simulated_char_values = [b'p', b's']
        iterable_simulated_char_values = iter(simulated_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        assert test_machine.seated_players[2].name == 'Alex'
        assert test_machine.seated_players[3].name == 'Jim'
        assert test_machine.state == bjfsm.GameState.STARTING

    def test_second_player_Jim_tries_to_sit_in_Alex_occupied_seat_2_then_adds_and_removes_seat_3_and_sits_at_different_chosen_seat_4(self, monkeypatch):
        pass

    def test_Alex_Jim_John_correctly_seated_in_seats_2_3_7_respectively(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        # Test
        simulated_input_values = ['Alex', '2', 'Jim', '2', '3', 'John', '7']
        iterable_simulated_input_values = iter(simulated_input_values)
        simulated_char_values = [b'p', b'p', b's']
        iterable_simulated_char_values = iter(simulated_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        assert test_machine.seated_players[2].name == 'Alex'
        assert test_machine.seated_players[3].name == 'Jim'
        assert test_machine.seated_players[7].name == 'John'
        assert test_machine.state == bjfsm.GameState.STARTING
    
    def test_all_seats_assigned_correctly_to_seven_joined_players(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        # Test
        simulated_input_values = ['Alex', '2', 'Jim', '3', 'John', '7', 'Mike', '1', 'Kim', '4', 'Jane', '5', 'Bob']
        iterable_simulated_input_values = iter(simulated_input_values)
        simulated_char_values = [b'p'] * 6
        iterable_simulated_char_values = iter(simulated_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        assert test_machine.seated_players[1].name == 'Mike'
        assert test_machine.seated_players[2].name == 'Alex'
        assert test_machine.seated_players[3].name == 'Jim'
        assert test_machine.seated_players[4].name == 'Kim'
        assert test_machine.seated_players[5].name == 'Jane'
        assert test_machine.seated_players[6].name == 'Bob'
        assert test_machine.seated_players[7].name == 'John'
        assert test_machine.state == bjfsm.GameState.STARTING


class Test_WAITING_Up_to_Two_Seats_per_Player:
    def test_blackjack_state_machine_transitions_to_STARTING_from_WAITING_after_two_players_with_two_seats_each_start_game(self, monkeypatch):
        pass
    
    def test_first_player_Alex_successfully_sits_at_adjacent_seats_2_and_3_with_center_seat_2(self, monkeypatch):
        pass

    def test_first_player_Alex_successfully_sits_at_adjacent_seats_2_and_3_with_center_seat_3(self, monkeypatch):
        pass

    def test_first_player_Alex_denied_sitting_at_non_adjacent_seats_2_and_4(self, monkeypatch):
        pass

    def test_second_player_Jim_cannot_sit_in_Alex_occupied_seats_2_and_3(self, monkeypatch):
        pass

    def test_second_player_Jim_successfully_selects_seats_4_5_after_trying_to_sit_in_Alex_occupied_seats_2_3(self, monkeypatch):
        pass

    def test_second_player_Jim_successfully_selects_adjacent_seats_4_5_after_first_player_Alex_sits_at_seats_2_3(self, monkeypatch):
        pass

    def test_second_player_Jim_successfully_submits_adjacent_seats_4_5_after_Alex_sits_at_seats_2_3(self, monkeypatch):
        pass

    







class Test_WAITING_Up_to_Three_Seats_per_Player:
    pass


class Test_STARTING:
    def test_blackjack_state_machine_transitions_to_SHUFFLING_from_STARTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        assert test_machine.state == bjfsm.GameState.SHUFFLING
    
    def test_only_joined_player_Alex_in_seat_2_set_to_active_in_STARTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        assert test_machine.seated_players[2].name == 'Alex'
        assert test_machine.active_player == test_machine.seated_players[2]

    def test_players_Alex_and_Ahmed_join_table_seats_2_and_1_Ahmed_in_leftmost_seat_set_to_active_in_STARTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_input_values = iter(simulated_input_values)
        simulated_char_values = [b'p', b's']
        iterable_simulated_char_values = iter(simulated_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        assert test_machine.seated_players[1].name == 'Ahmed'
        assert test_machine.seated_players[2].name == 'Alex'
        assert test_machine.active_player == test_machine.seated_players[1]

    def test_only_joined_player_Alex_added_to_known_players_in_STARTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        assert test_machine.seated_players[2].name == 'Alex'
        assert len(test_machine.known_players) == 1
        assert test_machine.seated_players[2] in test_machine.known_players

    def test_both_players_Alex_in_seat_2_and_Ahmed_in_seat_1_added_to_known_players_in_STARTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_input_values = iter(simulated_input_values)
        simulated_char_values = [b'p', b's']
        iterable_simulated_char_values = iter(simulated_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        assert test_machine.seated_players[1].name == 'Ahmed'
        assert test_machine.seated_players[2].name == 'Alex'
        assert len(test_machine.known_players) == 2
        assert test_machine.seated_players[1] in test_machine.known_players
        assert test_machine.seated_players[2] in test_machine.known_players

    def test_with_players_Alex_in_seat_2_Ahmed_in_seat_1_and_Jane_in_seat_5_last_player_occupied_seat_is_set_to_5(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2', 'Ahmed', '1', 'Jane', '5']
        iterable_simulated_input_values = iter(simulated_input_values)
        simulated_char_values = [b'p', b'p', b's']
        iterable_simulated_char_values = iter(simulated_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        assert test_machine.last_occupied_seat == 5

    """
    def test_joined_known_player_not_readded_to_list_of_known_players_in_STARTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        # Test
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        # WRITE TEST TO VERIFY NEW PLAYER OBJECT ISN'T CREATED WHEN PLAYER REJOINS TABLE AFTER LEAVING
        ### Test Code Here ###
    """

class Test_SHUFFLING:
    def test_blackjack_state_machine_transitions_to_BETTING_from_SHUFFLING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        # Test
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        assert test_machine.state == bjfsm.GameState.BETTING

    def test_starting_single_deck_shoe_is_shuffle_cut_and_burned_correctly_at_randomly_chosen_pen_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        ## Shoe Integrity Test ##
        # Verify deck size and pen percentage is in-bounds for a single deck shoe
        assert len(test_machine.shoe) == 1+52*1
        assert test_machine.pen in range(50, 71)
        # Verify cut cards are present and are placed correctly in-bounds for a single deck shoe
        assert 'front_cut_card' in test_machine.shoe[26:37]
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 1 copy of each non-cut card across shoe and discard, for a single deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 1

    def test_starting_eight_deck_shoe_is_shuffle_cut_and_burned_correctly_at_randomly_chosen_pen_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 8
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        ## Shoe Integrity Test ##
        # Verify deck size and pen percentage is in-bounds for an eight-deck shoe
        assert len(test_machine.shoe) == 1+52*8
        assert test_machine.pen in range(70, 91)
        # Verify cut cards are present and are placed correctly in-bounds for an eight-deck shoe
        assert 'front_cut_card' in test_machine.shoe[291:375]
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 8 copies of each non-cut card across shoe and discard, for an eight-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 8

    def test_one_deck_shoe_is_shuffle_cut_and_burned_correctly_at_min_pen_of_50_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        min_cut_percentage_one_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][0]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_one_deck_shoe) # manually executes SHUFFLING /w 50% pen
        ## Shoe Integrity Test ##
        # Verify deck size and minimum (50%) pen percentage for a one-deck shoe
        assert len(test_machine.shoe) == 1+52*1
        assert test_machine.pen == 50
        # Verify cut cards are present and are placed correctly at minimum (50%) pen for a one-deck shoe
        assert test_machine.shoe[26] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 1 copy of each non-cut card across shoe and discard, for a one-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 1

    def test_one_deck_shoe_is_shuffle_cut_and_burned_correctly_at_max_pen_of_70_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        min_cut_percentage_one_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][1]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_one_deck_shoe) # manually execute SHUFFLING /w 70% pen
        ## Shoe Integrity Test ##
        # Verify deck size and maximum (70%) pen percentage for a one-deck shoe
        assert len(test_machine.shoe) == 1+52*1
        assert test_machine.pen == 70
        # Verify cut cards are present and are placed correctly at maximum (70%) pen for a one-deck shoe
        assert test_machine.shoe[36] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 1 copy of each non-cut card across shoe and discard, for a one-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 1

    def test_two_deck_shoe_is_shuffle_cut_and_burned_correctly_at_min_pen_of_55_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 2
        min_cut_percentage_two_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][0]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_two_deck_shoe) # manually execute SHUFFLING /w 55% pen
        ## Shoe Integrity Test ##
        # Verify deck size and minimum (55%) pen percentage for a two-deck shoe
        assert len(test_machine.shoe) == 1+52*2
        assert test_machine.pen == 55
        # Verify cut cards are present and are placed correctly at minimum (55%) pen for a two-deck shoe
        assert test_machine.shoe[57] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 2 copies of each non-cut card across shoe and discard, for a two-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1   
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 2

    def test_two_deck_shoe_is_shuffle_cut_and_burned_correctly_at_max_pen_of_75_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 2
        min_cut_percentage_two_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][1]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_two_deck_shoe) # manually execute SHUFFLING /w 75% pen
        ## Shoe Integrity Test ##
        # Verify deck size and maximum (75%) pen percentage for a two-deck shoe
        assert len(test_machine.shoe) == 1+52*2
        assert test_machine.pen == 75
        # Verify cut cards are present and are placed correctly at maximum (75%) pen for a two-deck shoe
        assert test_machine.shoe[78] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 2 copies of each non-cut card across shoe and discard, for a two-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 2

    def test_four_deck_shoe_is_shuffle_cut_and_burned_correctly_at_min_pen_of_60_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 4
        min_cut_percentage_four_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][0]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_four_deck_shoe) # manually execute SHUFFLING /w 60% pen
        ## Shoe Integrity Test ##
        # Verify deck size and minimum (60%) pen percentage for a four-deck shoe
        assert len(test_machine.shoe) == 1+52*4
        assert test_machine.pen == 60
        # Verify cut cards are present and are placed correctly at minimum (60%) pen for a four-deck shoe
        assert test_machine.shoe[124] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 4 copies of each non-cut card across shoe and discard, for a four-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 4

    def test_four_deck_shoe_is_shuffle_cut_and_burned_correctly_at_max_pen_of_80_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 4
        min_cut_percentage_four_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][1]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_four_deck_shoe) # manually execute SHUFFLING /w 80% pen
        ## Shoe Integrity Test ##
        # Verify deck size and maximum (80%) pen percentage for a four-deck shoe
        assert len(test_machine.shoe) == 1+52*4
        assert test_machine.pen == 80
        # Verify cut cards are present and are placed correctly at maximum (80%) pen for a four-deck shoe
        assert test_machine.shoe[166] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 4 copies of each non-cut card across shoe and discard, for a four-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 4

    def test_six_deck_shoe_is_shuffle_cut_and_burned_correctly_at_min_pen_of_65_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 6
        min_cut_percentage_six_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][0]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_six_deck_shoe) # manually execute SHUFFLING /w 65% pen
        ## Shoe Integrity Test ##
        # Verify deck size and minimum (65%) pen percentage for a six-deck shoe
        assert len(test_machine.shoe) == 1+52*6
        assert test_machine.pen == 65
        # Verify cut cards are present and are placed correctly at minimum (65%) pen for a six-deck shoe
        assert test_machine.shoe[202] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 6 copies of each non-cut card across shoe and discard, for a six-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 6

    def test_six_deck_shoe_is_shuffle_cut_and_burned_correctly_at_max_pen_of_85_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 6
        min_cut_percentage_six_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][1]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_six_deck_shoe) # manually execute SHUFFLING /w 85% pen
        ## Shoe Integrity Test ##
        # Verify deck size and maximum (85%) pen percentage for a six-deck shoe
        assert len(test_machine.shoe) == 1+52*6
        assert test_machine.pen == 85
        # Verify cut cards are present and are placed correctly at maximum (85%) pen for a six-deck shoe
        assert test_machine.shoe[265] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 6 copies of each non-cut card across shoe and discard, for a six-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 6

    def test_eight_deck_shoe_is_shuffle_cut_and_burned_correctly_at_min_pen_of_70_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 8
        min_cut_percentage_eight_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][0]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_eight_deck_shoe) # manually execute SHUFFLING /w 70% pen
        ## Shoe Integrity Test ##
        # Verify deck size and minimum (70%) pen percentage for an eight-deck shoe
        assert len(test_machine.shoe) == 1+52*8
        assert test_machine.pen == 70
        # Verify cut cards are present and are placed correctly at minimum (70%) pen for an eight-deck shoe
        assert test_machine.shoe[291] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 8 copies of each non-cut card across shoe and discard, for an eight-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 8

    def test_eight_deck_shoe_is_shuffle_cut_and_burned_correctly_at_max_pen_of_90_percent_in_SHUFFLING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 8
        min_cut_percentage_eight_deck_shoe = bjs.casino_deck_pen_percentage_bounds[num_of_decks][1]
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.shuffle_cut_and_burn(min_cut_percentage_eight_deck_shoe) # manually execute SHUFFLING /w 90% pen
        ## Shoe Integrity Test ##
        # Verify deck size and maximum (90%) pen percentage for an eight-deck shoe
        assert len(test_machine.shoe) == 1+52*8
        assert test_machine.pen == 90
        # Verify cut cards are present and are placed correctly at maximum (90%) pen for an eight-deck shoe
        assert test_machine.shoe[374] == 'front_cut_card'
        assert test_machine.shoe[-1] == 'back_cut_card'
        # Verify there's 8 copies of each non-cut card across shoe and discard, for an eight-deck shoe
        card_occurrence_counts = dict.fromkeys(bjo.base_deck, 0)
        card_occurrence_counts[test_machine.discard[0]] += 1
        for card in test_machine.shoe:
            if (card != 'front_cut_card') and (card != 'back_cut_card'):
                card_occurrence_counts[card] += 1
        for card in card_occurrence_counts:
            #print(card,"has",card_occurrence_counts[card],"occurrences in the shoe")
            assert card_occurrence_counts[card] == 8

class Test_MAIN_BETTING_Hand_Independent:
    def test_blackjack_state_machine_transitions_to_DEALING_from_BETTING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        # Test
        #simulated_char_inputs = [b'1', b'3', b'4', b'5', b'f']
        simulated_char_inputs = [b'1', b'f', b'n', b'n'] # player Alex in seat 2 makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        assert test_machine.state == bjfsm.GameState.DEALING

class Test_MAIN_BETTING_One_Hand_per_Player:
    def test_one_hand_bet_of_50_in_Whites_by_player_Alex_in_seat_2_handled_correctly(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        # Test
        simulated_player_bet_char_inputs = [b'1']*50 + [b'f', b'n', b'n']
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        player_Alex = test_machine.seated_players[2]
        assert player_Alex.chip_pool_balance == 500-50
        assert player_Alex.chips['White'] == 0

    def test_one_hand_bets_of_5_and_10_in_Reds_by_players_Ahmed_and_Alex_in_seats_1_and_2_handled_correctly(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        # Test
        simulated_player_bet_char_inputs = [b'3', b'f', b'n', b'n', b'3', b'3', b'f', b'n', b'n']
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        player_Ahmed = test_machine.seated_players[1]
        player_Alex = test_machine.seated_players[2]
        assert player_Ahmed.chip_pool_balance == 500-5
        assert player_Alex.chip_pool_balance == 500-10
        assert player_Ahmed.chips['Red'] == 19
        assert player_Alex.chips['Red'] == 18

    def test_one_hand_bets_of_10_30_20_in_Blues_by_players_Ahmed_Alex_Kim_in_seats_1_2_7_handled_correctly(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1', 'Kim', '7']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        # Test
        simulated_player_bet_char_inputs = [b'4']*1 + [b'f', b'n', b'n'] + [b'4']*3 + [b'f', b'n', b'n'] + [b'4']*2 + [b'f', b'n', b'n']
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        player_Ahmed = test_machine.seated_players[1]
        player_Alex = test_machine.seated_players[2]
        player_Kim = test_machine.seated_players[7]
        assert player_Ahmed.chip_pool_balance == 500-10
        assert player_Alex.chip_pool_balance == 500-30
        assert player_Kim.chip_pool_balance == 500-20
        assert player_Ahmed.chips['Blue'] == 14
        assert player_Alex.chips['Blue'] == 12
        assert player_Kim.chips['Blue'] == 13

class Test_MAIN_BETTING_Two_Hands_per_Player:
    def test_two_hand_bet_of_5_and_10_in_Reds_by_player_Alex_in_seats_2_and_3_handled_correctly(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        # Test
        simulated_player_bet_char_inputs = [b'1']*50 + [b'f', b'n', b'n']
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        player_Alex = test_machine.seated_players[2]
        assert player_Alex.chip_pool_balance == 500-50
        assert player_Alex.chips['White'] == 0
        pass

    def test_two_hand_bets_of_5_10_and_15_20_in_Reds_by_players_Ahmed_and_Alex_in_seats_1_2_and_3_4_handled_correctly(self, monkeypatch):
        pass

    def test_two_hand_bets_of_10_20_and_30_40_and_50_60_in_Blues_by_players_Ahmed_Alex_Kim_in_seats_1_2_and_4_5_and_6_7_handled_correctly(self, monkeypatch):
        pass

class Test_MAIN_BETTING_Three_Hands_per_Player:
    def test_three_hand_bet_of_5_10_15_in_Reds_by_player_Alex_in_seats_2_3_4_handled_correctly(self, monkeypatch):
        pass

    def test_three_hand_bets_of_10_20_30_and_40_50_60_in_Blues_by_players_Ahmed_and_Alex_in_seats_1_2_3_and_5_6_7_handled_correctly(self, monkeypatch):
        pass

class Test_SIDE_BETTING_One_Hand_per_Player:
    pass

class Test_SIDE_BETTING_Multiple_Hands_per_Player:
    pass


class Test_DEALING_One_Hand_per_Player:
    def test_blackjack_state_machine_transitions_to_INITIAL_SCORING_from_DEALING(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_player_bet_char_inputs = [b'1', b'f'] # player Alex in seat 2 makes a bet of 1 White chip
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        assert test_machine.state == bjfsm.GameState.INITIAL_SCORING

    def test_player_Alex_in_seat_2_is_dealt_one_hand_correctly(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        playerAlex = test_machine.seated_players[2]
        assert len(playerAlex.hands['center_seat']) == 2
        #assert all(card in bjo.base_deck for card in playerAlex.hands['center_seat'])
        assert playerAlex.hands['center_seat'][0] in bjo.base_deck
        assert playerAlex.hands['center_seat'][1] in bjo.base_deck

    def test_single_hands_dealt_correctly_to_players_Ahmed_and_Alex_in_seats_1_and_2(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_player_bet_char_inputs = [b'1', b'f', b'1', b'f'] # players Alex and Ahmed bet 1 White chip each
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        playerAhmed = test_machine.seated_players[1]
        playerAlex = test_machine.seated_players[2]
        assert len(playerAhmed.hands['center_seat']) == 2
        assert len(playerAlex.hands['center_seat']) == 2
        assert playerAhmed.hands['center_seat'][0] in bjo.base_deck
        assert playerAhmed.hands['center_seat'][1] in bjo.base_deck
        assert playerAlex.hands['center_seat'][0] in bjo.base_deck
        assert playerAlex.hands['center_seat'][1] in bjo.base_deck

    def test_dealers_hand_dealt_correctly_with_one_player_Alex_one_hand_at_the_table(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        playerDealer = test_machine.dealer
        assert playerDealer.hands['left_seat'] == None
        assert playerDealer.hands['right_seat'] == None
        assert len(playerDealer.hands['center_seat']) == 2
        assert playerDealer.hands['center_seat'][0] in bjo.base_deck
        assert playerDealer.hands['center_seat'][1] in bjo.base_deck

    def test_dealers_hand_dealt_correctly_with_two_players_Ahmed_Alex_single_hands_at_the_table(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_player_bet_char_inputs = [b'1', b'f', b'1', b'f'] # players Alex and Ahmed bet 1 White chip each
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        playerDealer = test_machine.dealer
        assert playerDealer.hands['left_seat'] == None
        assert playerDealer.hands['right_seat'] == None
        assert len(playerDealer.hands['center_seat']) == 2
        assert playerDealer.hands['center_seat'][0] in bjo.base_deck
        assert playerDealer.hands['center_seat'][1] in bjo.base_deck

    def test_one_deck_shoe_has_49_cards_left_after_one_player_and_dealer_are_dealt_one_hand_each(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        assert len(test_machine.shoe) == 49

    def test_one_deck_shoe_has_47_cards_left_after_two_players_and_dealer_are_dealt_one_hand_each(self, monkeypatch):
        # Setup
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_player_bet_char_inputs = [b'1', b'f', b'1', b'f'] # players Alex and Ahmed bet 1 White chip each
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        assert len(test_machine.shoe) == 47

    def test_eight_deck_shoe_has_413_cards_left_after_one_player_and_dealer_are_dealt_one_hand_each(self, monkeypatch):
        # Setup
        num_of_decks = 8
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        assert len(test_machine.shoe) == 413

    def test_eight_deck_shoe_has_411_cards_left_after_two_players_and_dealer_are_dealt_one_hand_each(self, monkeypatch):
        # Setup
        num_of_decks = 8
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_player_bet_char_inputs = [b'1', b'f', b'1', b'f'] # players Alex and Ahmed bet 1 White chip each
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Test
        test_machine.step() # executes deal() in DEALING and transitions to INITIAL_SCORING
        assert len(test_machine.shoe) == 411

class Test_DEALING_Multiple_Hands_per_Player:
    def test_player_Alex_in_seats_2_and_3_is_dealt_two_hands_correctly(self, monkeypatch):
        pass

    def test_one_hand_dealt_to_Ahmed_in_seat_1_and_two_hands_dealt_to_Alex_in_seats_2_and_3_correctly(self, monkeypatch):
        pass

    # Add more tests here #


class Test_INITIAL_SCORING_Score_Results:
    # One hand per player tests #
    def test_one_player_Alex_in_seat_2_has_one_hand_KD_QH_dealer_has_JH_9C_both_hands_scored_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'QH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.score_all_hands_in_play() # executes just scoring out of the three methods in INITIAL_SCORING
        assert playerAlex.hand_scores['left_seat'] == None
        assert playerAlex.hand_scores['right_seat'] == None
        assert playerAlex.hand_scores['center_seat'] == 20
        assert playerDealer.hand_scores['left_seat'] == None
        assert playerDealer.hand_scores['right_seat'] == None
        assert playerDealer.hand_scores['center_seat'] == 19

    def test_two_players_Ahmed_with_4S_10S_Alex_with_KD_QH_and_dealer_with_JH_9C_have_all_hands_scored_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f', b'1', b'f'] # Players Ahmed and Alex both make bets of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['4S', '10S'] to player Ahmed in seat 1
        manual_player_hand_one = ['4S', '10S']
        if manual_player_hand_one[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_one[0]))
        if manual_player_hand_one[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_one[1]))
        playerAhmed = test_machine.seated_players[1]
        playerAhmed.hands['center_seat'] = manual_player_hand_one
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand_two = ['KD', 'QH']
        if manual_player_hand_two[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_two[0]))
        if manual_player_hand_two[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_two[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand_two
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING

        assert playerAhmed.hand_scores['left_seat'] == None
        assert playerAhmed.hand_scores['right_seat'] == None
        assert playerAhmed.hand_scores['center_seat'] == 14
        assert playerAlex.hand_scores['left_seat'] == None
        assert playerAlex.hand_scores['right_seat'] == None
        assert playerAlex.hand_scores['center_seat'] == 20
        assert playerDealer.hand_scores['left_seat'] == None
        assert playerDealer.hand_scores['right_seat'] == None
        assert playerDealer.hand_scores['center_seat'] == 19

    # Two hands per player tests #

    # Three hands per player tests #

class Test_INITIAL_SCORING_Tracking_Natural_Blackjacks:
    # One hand per player tests #
    def test_one_player_table_only_player_has_one_blackjack_hand_tracked_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'AH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'AH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.score_all_hands_in_play() # executes just scoring out of the three methods in INITIAL_SCORING
        #print(test_machine.current_round_natural_blackjacks.keys())
        #print(test_machine.current_round_natural_blackjacks.values())
        assert len(test_machine.current_round_natural_blackjacks[playerAlex]) == 1
        assert manual_player_hand in test_machine.current_round_natural_blackjacks[playerAlex]

    def test_two_player_table_each_player_has_one_blackjack_hand_tracked_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_player_bet_char_inputs = [b'1', b'f', b'1', b'f'] # players Alex and Ahmed bet 1 White chip each
        iterable_simulated_player_bet_char_inputs = iter(simulated_player_bet_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_bet_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'AH'] to player Ahmed in seat 1
        first_player_hand = ['KC', 'AS']
        if first_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(first_player_hand[0]))
        if first_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(first_player_hand[1]))
        playerAhmed = test_machine.seated_players[1]
        playerAhmed.hands['center_seat'] = first_player_hand
        # Manually deal a hand of ['KD', 'AH'] to player Alex in seat 2
        second_player_hand = ['KD', 'AH']
        if second_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(second_player_hand[0]))
        if second_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(second_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = second_player_hand
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.score_all_hands_in_play() # executes just scoring out of the three methods in INITIAL_SCORING
        #print(test_machine.current_round_natural_blackjacks.keys())
        #print(test_machine.current_round_natural_blackjacks.values())
        assert len(test_machine.current_round_natural_blackjacks.keys()) == 2
        assert len(test_machine.current_round_natural_blackjacks[playerAhmed]) == 1
        assert first_player_hand in test_machine.current_round_natural_blackjacks[playerAhmed]
        assert len(test_machine.current_round_natural_blackjacks[playerAlex]) == 1
        assert second_player_hand in test_machine.current_round_natural_blackjacks[playerAlex]

    # Two hands per player tests #
    def test_one_player_table_only_player_has_two_blackjack_hands_tracked_correctly(self, monkeypatch):
        pass

    def test_two_player_table_each_player_has_two_hands_with_one_blackjack_hand_each_tracked_correctly(self, monkeypatch):
        pass

    def test_two_player_table_each_player_has_two_blackjack_hands_tracked_correctly(self, monkeypatch):
        pass

    # Three hands per player tests #
    def test_one_player_table_only_player_has_three_blackjack_hands_tracked_correctly(self, monkeypatch):
        pass

    def test_two_player_table_each_player_has_three_hands_with_two_blackjack_hands_tracked_correctly(self, monkeypatch):
        pass

    def test_two_player_table_each_player_has_three_blackjack_hands_tracked_correctly(self, monkeypatch):
        pass

    # Add tests to verify that no natural blackjacks are tracked after INITIAL_SCORING state is exited

"""
def test_11_USD_bet_correctly_transferred_to_dealer_from_player(self):
        # Setup
        test_dealer = bjp.Player.create_casino_dealer()
        test_player = bjp.Player.create_new_player_from_template('Alex', '2')
        empty_bet = dict.fromkeys(bjo.chip_names, 0)
        placed_bet = dict.fromkeys(bjo.chip_names, 0)
        test_player.chips['White'] -= 1
        placed_bet['White'] = 1
        test_player.chips['Red'] -= 2
        placed_bet['Red'] = 2
        test_player.main_bets['center_seat'] = placed_bet # {'White': 1, 'Red': 2} ; all other chip counts set to 0
        test_player.chip_pool_balance -= 11
        test_player.main_bet_amounts['center_seat'] = 11
        # Test
        assert test_player.main_bets['center_seat'] == placed_bet
        assert test_player.main_bet_amounts['center_seat'] == 11

        # Looks convoluted, how to clean up? Can this be cleaned up?
        test_player.main_bet_amounts['center_seat'] = test_player.transfer_bet_chips_to_dealer(test_dealer, test_player.main_bets['center_seat'], 
                                                                                               test_player.main_bet_amounts['center_seat'])
        assert test_player.main_bets['center_seat'] == empty_bet
        assert test_player.main_bet_amounts['center_seat'] == 0
"""



class TestPayouts_6_to_5_Blackjack:
    def test_3_USD_bet_pays_out_4_USD_as_4_White_chips(self):
        pass

    def test_4_USD_bet_pays_out_5_USD_as_1_Red_chip(self):
        pass

    def test_7_USD_bet_pays_out_8_USD_as_1_Red_3_White_chips(self):
        pass

    def test_8_USD_bet_pays_out_10_USD_as_1_Blue_chip(self):
        pass

    def test_11_USD_bet_pays_out_13_USD_as_1_Blue_3_White_chips(self):
        pass

    def test_13_USD_bet_pays_out_16_USD_as_1_Blue_1_Red_1_White_chips(self):
        pass

    def test_17_USD_bet_pays_out_20_USD_as_2_Blue_chips(self):
        pass

    def test_20_USD_bet_pays_out_24_USD_as_2_Blue_1_White_chips(self):
        pass

    def test_21_USD_bet_pays_out_25_USD_as_1_Green_chip(self):
        pass

    def test_42_USD_bet_pays_out_50_USD_as_2_Green_chips(self):
        pass

    def test_45_USD_bet_pays_out_54_USD_as_2_Green_4_White_chips(self):
        pass

    def test_55_USD_bet_pays_out_66_USD_as_2_Green_1_Blue_1_Red_1_White_chips(self):
        pass

    def test_82_USD_bet_pays_out_98_USD_as_3_Green_2_Blue_3_White_chips(self):
        pass

    def test_86_USD_bet_pays_out_103_USD_as_1_Black_3_White_chips(self):
        pass

    def test_99_USD_bet_pays_out_119_USD_as_1_Black_1_Blue_1_Red_4_White_chips(self):
        pass

    def test_120_USD_bet_pays_out_144_USD_as_1_Black_1_Green_1_Blue_1_Red_4_White_chips(self):
        pass


class TestPayouts_3_to_2_Blackjack:
    pass


class Test_INITIAL_SCORING_One_Hand_per_Player_Bet_Outcomes:
    # One player table tests #
    def test_one_player_table_no_blackjacks_transitions_to_PLAYER_PLAYING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'QH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING
        assert test_machine.state == bjfsm.GameState.PLAYER_PLAYING

    def test_one_player_table_only_dealer_has_face_ten_blackjack_player_loss_handled_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip ($1)
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'QH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', 'AC'] to dealer
        manual_dealer_hand = ['JH', 'AC']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING
        assert playerAlex.chip_pool_balance == 499
        assert playerAlex.chips['White'] == 49
        assert playerDealer.chip_pool_balance == 6643501
        assert playerDealer.chips['White'] == 1001
        assert test_machine.state == bjfsm.GameState.BETTING

    def test_one_player_table_only_dealer_has_face_ace_blackjack_player_loss_handled_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip ($1)
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'QH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['AC', 'JH'] to dealer
        manual_dealer_hand = ['AC', 'JH']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING
        assert playerAlex.chip_pool_balance == 499
        assert playerAlex.chips['White'] == 49
        assert playerDealer.chip_pool_balance == 6643501
        assert playerDealer.chips['White'] == 1001
        assert test_machine.state == bjfsm.GameState.BETTING

    def test_one_player_table_only_player_has_blackjack_player_win_handled_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'AH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'AH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING
        assert playerAlex.chip_pool_balance == 502
        assert playerAlex.chips['White'] == 52
        assert playerDealer.chip_pool_balance == 6643498
        assert playerDealer.chips['White'] == 998
        assert test_machine.state == bjfsm.GameState.BETTING
        




    def test_one_player_table_both_dealer_and_player_blackjack_case_scored_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'AH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'AH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', 'AC'] to dealer
        manual_dealer_hand = ['JH', 'AC']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING

        assert playerAlex.hand_scores['left_seat'] == None
        assert playerAlex.hand_scores['right_seat'] == None
        assert playerAlex.hand_scores['center_seat'] == 21
        assert playerDealer.hand_scores['left_seat'] == None
        assert playerDealer.hand_scores['right_seat'] == None
        assert playerDealer.hand_scores['center_seat'] == 21

    # Two player table tests #
    def test_two_player_table_nobody_has_blackjack_case_scored_correctly(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f', b'1', b'f'] # Players Ahmed and Alex both make bets of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['4S', '10S'] to player Ahmed in seat 1
        manual_player_hand_one = ['4S', '10S']
        if manual_player_hand_one[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_one[0]))
        if manual_player_hand_one[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_one[1]))
        playerAhmed = test_machine.seated_players[1]
        playerAhmed.hands['center_seat'] = manual_player_hand_one
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand_two = ['KD', 'QH']
        if manual_player_hand_two[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_two[0]))
        if manual_player_hand_two[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_two[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand_two
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING

        assert playerAhmed.hand_scores['left_seat'] == None
        assert playerAhmed.hand_scores['right_seat'] == None
        assert playerAhmed.hand_scores['center_seat'] == 14
        assert playerAlex.hand_scores['left_seat'] == None
        assert playerAlex.hand_scores['right_seat'] == None
        assert playerAlex.hand_scores['center_seat'] == 20
        assert playerDealer.hand_scores['left_seat'] == None
        assert playerDealer.hand_scores['right_seat'] == None
        assert playerDealer.hand_scores['center_seat'] == 19

    def test_two_player_table_only_one_player_has_blackjack_case_scored_correctly(self, monkeypatch):
        pass

    def test_two_player_table_only_both_players_have_blackjack_case_scored_correctly(self, monkeypatch):
        pass

    def test_two_player_table_no_players_have_blackjack_dealer_has_blackjack_case_scored_correctly(self, monkeypatch):
        pass

    def test_two_player_table_only_one_player_has_blackjack_dealer_has_blackjack_case_scored_correctly(self, monkeypatch):
        pass

    def test_two_player_table_both_players_have_blackjack_dealer_has_blackjack_case_scored_correctly(self, monkeypatch):
        pass


class Test_INITIAL_SCORING_Multiple_Hands_per_Player_Bet_Outcomes:
    # One player table tests #


    # Two player table tests #
    pass


class Test_INITIAL_SCORING_One_Hand_per_Player_State_Transitions:
    def test_one_player_table_no_blackjacks_has_state_machine_transition_to_PLAYER_PLAYING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_input_values = ['Alex', '2']
        iterable_simulated_input_values = iter(simulated_input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: b's')
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f'] # Player Alex makes a bet of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand = ['KD', 'QH']
        if manual_player_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[0]))
        if manual_player_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING
        assert test_machine.state == bjfsm.GameState.PLAYER_PLAYING

    def test_one_player_table_only_dealer_has_blackjack_has_state_machine_to_BETTING(self, monkeypatch):
        pass

    def test_two_player_table_no_blackjacks_has_state_machine_transition_to_PLAYER_PLAYING(self, monkeypatch):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        simulated_player_init_input_values = ['Alex', '2', 'Ahmed', '1']
        iterable_simulated_player_init_input_values = iter(simulated_player_init_input_values)
        simulated_player_init_char_values = [b'p', b's']
        iterable_simulated_player_init_char_values = iter(simulated_player_init_char_values)
        monkeypatch.setattr('builtins.input', lambda _: next(iterable_simulated_player_init_input_values))
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_player_init_char_values))
        test_machine.step() # executes wait_for_players_to_join() in WAITING and transitions to STARTING
        test_machine.step() # executes start_game() in STARTING and transitions to SHUFFLING
        test_machine.step() # executes shuffle_cut_and_burn() in SHUFFLING and transitions to BETTING
        simulated_char_inputs = [b'1', b'f', b'1', b'f'] # Players Ahmed and Alex both make bets of 1 White chip
        iterable_simulated_char_inputs = iter(simulated_char_inputs)
        monkeypatch.setattr('msvcrt.getch', lambda: next(iterable_simulated_char_inputs))
        test_machine.step() # executes get_all_players_bets() in BETTING and transitions to DEALING
        # Manually deal a hand of ['4S', '10S'] to player Ahmed in seat 1
        manual_player_hand_one = ['4S', '10S']
        if manual_player_hand_one[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_one[0]))
        if manual_player_hand_one[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_one[1]))
        playerAhmed = test_machine.seated_players[1]
        playerAhmed.hands['center_seat'] = manual_player_hand_one
        # Manually deal a hand of ['KD', 'QH'] to player Alex in seat 2
        manual_player_hand_two = ['KD', 'QH']
        if manual_player_hand_two[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_two[0]))
        if manual_player_hand_two[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_player_hand_two[1]))
        playerAlex = test_machine.seated_players[2]
        playerAlex.hands['center_seat'] = manual_player_hand_two
        # Manually deal a hand of ['JH', '9C'] to dealer
        manual_dealer_hand = ['JH', '9C']
        if manual_dealer_hand[0] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[0]))
        if manual_dealer_hand[1] in test_machine.discard:
            test_machine.discard.pop()
            test_machine.discard.extend(test_machine.shoe.pop(0))
        else:
            test_machine.shoe.pop(test_machine.shoe.index(manual_dealer_hand[1]))
        playerDealer = test_machine.dealer
        playerDealer.hands['center_seat'] = manual_dealer_hand
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING) # manually transition to INITIAL_SCORING
        ## Test ##
        test_machine.step() # executes score_all_hands_in_play() and blackjack handling methods in INITIAL_SCORING

        assert test_machine.state == bjfsm.GameState.PLAYER_PLAYING


class Test_INITIAL_SCORING_Multiple_Hands_per_Player_State_Transitions:
    pass



class TestNaturalBlackjacks_INITIAL_SCORING:
    def test_dealer_face_up_card_ace_has_blackjack_first_player_with_blackjack_hand_pushes_correctly_single_deck(self):
        ## Setup ##
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        test_machine.step() # executes start_game() in STARTING
        # Manually execute shuffle_cut_and_burn(), burning '8H'
        test_machine.shuffle_cut_and_burn(None)
        test_machine.shoe.extend(test_machine.discard)
        test_machine.discard.clear()
        test_machine.discard.extend([test_machine.shoe.pop(test_machine.shoe.index('8H'))])
        assert ('8H' not in test_machine.shoe) and ('8H' in test_machine.discard)
        # Manually assign a bet of '2 White' with value of $2 to first player
        first_player = test_machine.joined_players[0]
        first_player_bet_string = '2 White, 1 Blue'
        alternate_bet_string = '112'


        first_player.add_primary_bet(player_hand, first_player_bet_string)



        first_player.current_primary_bets.append(first_player_bet_string.split(', '))
        first_player.current_primary_bet_values.append(2*1 + 1*5)
        first_player.White -= 2
        first_player.Blue -= 1
        # Manually deal a blackjack hand to first player
        player_hand = ['QD', 'AH']
        test_machine.shoe.pop(test_machine.shoe.index('QD'))
        test_machine.shoe.pop(test_machine.shoe.index('AH'))
        first_player.current_hands.append(player_hand)
        # Manually deal a blackjack hand to dealer
        dealer_hand = ['AS', 'KC']
        test_machine.shoe.pop(test_machine.shoe.index('AS'))
        test_machine.shoe.pop(test_machine.shoe.index('KC'))
        test_machine.dealer.current_hands.append(dealer_hand)
        # DEBUG - print dealer and player stats #
        test_machine.dealer.print_player_stats()
        first_player.print_player_stats()
        # Transition to INITIAL_SCORING and execute all methods within
        test_machine.transition(bjfsm.GameState.INITIAL_SCORING)
        test_machine.step()
        ## Test ##
        assert test_machine.state == bjfsm.GameState.BETTING
        assert first_player.White == 50
        assert first_player.Blue == 20
        assert len(test_machine.shoe) == 49

    def test_first_player_with_blackjack_regular_blackjack_is_handled_correctly_against_dealer_blackjack(self):
        pass

    def test_first_player_with_regular_hand_loses_correctly_against_dealer_blackjack(self):
        pass

    def test_first_player_with_two_regular_hands_loses_correctly_against_dealer_blackjack(self):
        pass

    def test_first_player_with_regular_hand_keeps_playing_after_checking_dealer_has_no_blackjack(self):
        pass

    def test_first_player_with_blackjack_wins_after_checking_dealer_has_no_blackjack(self):
        pass

    def test_first_player_with_regular_blackjack_hands_wins_just_second_after_checking_dealer_has_no_blackjack(self):
        pass

    def test_card_count_is_correct_for_single_deck_shoe_after_checking_for_dealer_blackjack_with_two_blackjacks(self):
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        test_machine.step() # executes start_game() in STARTING
        test_machine.step() # executes shuffle_cut_and_burn(None) in SHUFFLING
        # Manually deal player blackjack hand
        player_hand = ['QD', 'AH']
        first_player = test_machine.joined_players[0]
        first_player.current_hands.append(player_hand)
        #print(first_player.current_hands[0])
        # Manually remove dealt player's blackjack hand cards from shoe
        if 'QD' in test_machine.discard:
            pass
        else:
            test_machine.shoe.remove('QD')
        if 'AH' in test_machine.discard:
            pass
        else:
            test_machine.shoe.remove('AH')
        # Manually deal blackjack hand to dealer
        dealer_hand = ['AS', 'KC']
        test_machine.dealer.current_hands.append(dealer_hand)
        print(test_machine.dealer.current_hands[0])
        # Remove manually dealt dealer's blackjack hand cards from shoe
        if 'AS' in test_machine.discard:
            pass
        else:
            test_machine.shoe.remove('AS')
        if 'KC' in test_machine.discard:
            pass
        else:
            test_machine.shoe.remove('KC')
        # Manually transition to SCORING
        test_machine.transition(bjfsm.GameState.SCORING)
        test_machine.step() # scores all players' hands, checks for and handles dealer and player blackjacks in SCORING
        # Verify card count between shoe and discard is correct for a single deck after checking for dealer blackjack
        assert (len(test_machine.shoe) + len(test_machine.discard)) == 54

    def test_card_count_is_correct_for_single_deck_shoe_after_SCORING(self):
        pass


class TestMiscellaneous:
    def test_invalid_state_transition_handled(self):
        BadState = Enum('BadState', ['InvalidState'])
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        test_machine.transition(BadState.InvalidState)
        with pytest.raises(NameError):
            test_machine.step()


class TestReshuffling:
    def test_single_deck_shoe_not_reshuffled_at_or_before_min_pen_bound_of_fifty_percent(self, monkeypatch):
        # Shuffle single-deck shoe at 50% pen ('front_cut_card' is at index 26)
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        test_machine.step() # executes start_game() in STARTING, assigning active player
        test_machine.shuffle_cut_and_burn(50)
        test_machine.transition(bjfsm.GameState.DEALING)
        # Step through the state machine enough times to deal 13 hands (26 cards)
        for x in range (0, 13):
            test_machine.step() # executes deal() in GameState.DEALING
            test_machine.step() # executes score_hand() in GameState.SCORING
            if test_machine.state == bjfsm.GameState.DEALING:
                pass
            elif test_machine.state == bjfsm.GameState.PLAYER_PLAYING:
                monkeypatch.setattr('builtins.input', lambda _: 'stand')
                test_machine.step() # executes play() in GameState.PLAYING /w supplied user input of 'stand'
        # Check that next card to be dealt is 'front_cut_card' and we haven't reshuffled yet
        assert test_machine.shoe[0] == 'front_cut_card'
        assert len(test_machine.shoe) == 27
        assert test_machine.state == bjfsm.GameState.DEALING
    
    def test_single_deck_shoe_is_reshuffled_only_after_min_pen_bound_of_fifty_percent(self, monkeypatch):
        # Shuffle single-deck shoe at 50% pen ('front_cut_card' is at index 26)
        num_of_decks = 1
        test_machine = bjfsm.BlackjackStateMachine(num_of_decks)
        test_machine.shuffle_cut_and_burn(50)
        test_machine.transition(bjfsm.GameState.DEALING)
        # Step through the state machine enough times to deal 14 hands (28 cards)
        for x in range (0, 14):
            test_machine.step() # executes deal() in GameState.DEALING
            test_machine.step() # executes score_hand() in GameState.SCORING
            if test_machine.state == bjfsm.GameState.DEALING:
                pass
            elif test_machine.state == bjfsm.GameState.PLAYING:
                monkeypatch.setattr('builtins.input', lambda _: 'stand')
                test_machine.step() # executes play() in GameState.PLAYING /w supplied user input of 'stand'
        # Verify state machine is reshuffling at round end after dealing 28 cards
        assert test_machine.state == bjfsm.GameState.SHUFFLING