import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_south_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH

def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.WEST

def test_north_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.NORTH

def test_illegal_move(robot): #south
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()
def test_illegal_move1(robot): # West
    robot.turn();
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move2(robot): # North
    for i in range (0,9):
        robot.move()
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move3(robot): #East
    robot.turn()
    for i in range (0,9):
        robot.move()
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2

def test_move_south(robot):
    robot.move()
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1

def test_move_west(robot):
    robot.turn()
    robot.move()
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_without_history1(robot): # after making a move
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_without_history2(robot): #after a turn
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_without_history3(robot): #after multiple moves
    robot.move()
    robot.turn()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_track_without_history3(robot): #after multiple moves are back tracked
    robot.move()
    robot.turn()
    robot.move()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

