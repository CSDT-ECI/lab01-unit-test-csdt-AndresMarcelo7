from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_chance_should_get_total():
        #Arrange
        result_dices = [1,2,3,4,5]
        #Act 
        total = Yatzy.chance(result_dices[0],
                             result_dices[1],
                             result_dices[2],
                             result_dices[3],
                             result_dices[4])
        #Assert
        expected = sum(result_dices)
        assert total == expected

def test_yatzy_should_get_fifty():
        #Arrange
        result_dices = [[1,1,1,1,1], [2,2,2,2,2],[3,3,3,3,3]]
        #Act
        for i in range(len(result_dices)):
                total = Yatzy.yatzy(result_dices[i])
                #Assert
                assert total == 50

def test_yatzy_should_get_zero():
        #Arrange
        result_dices = [[1,1,1,1,2], [1,2,2,2,2],[3,3,1,3,3]]
        #Act
        for i in range(len(result_dices)):
                total = Yatzy.yatzy(result_dices[i])
                #Assert
                assert total == 0

def test_ones_should_get_valid_total():
        #Arrange
        result_dices = [[1,1,1,1,1], [2,2,2,2,2], [3,3,3,1,1], [2,2,1,2,2]]
        expected_results = [5,0,2,1]
        #Act
        for i in range(len(result_dices)):
                total = Yatzy.ones(result_dices[i][0],result_dices[i][1],result_dices[i][2],result_dices[i][3],result_dices[i][4])
                #Assert
                assert total == expected_results[i]

def test_twos_should_get_valid_total():
        #Arrange
        result_dices = [[1,1,1,1,1], [2,2,2,2,2], [2,3,3,1,1], [2,2,1,2,2]]
        expected_results = [0,10,2,8]
        #Act
        for i in range(len(result_dices)):
                total = Yatzy.twos(result_dices[i][0],result_dices[i][1],result_dices[i][2],result_dices[i][3],result_dices[i][4])
                #Assert
                assert total == expected_results[i]


def test_threes_should_get_valid_total():
        #Arrange
        result_dices = [[1,1,1,1,1], [2,2,2,2,2], [2,3,3,1,1], [2,2,1,2,2]]
        expected_results = [0,0,6,0]
        #Act
        for i in range(len(result_dices)):
                total = Yatzy.threes(result_dices[i][0],result_dices[i][1],result_dices[i][2],result_dices[i][3],result_dices[i][4])
                #Assert
                assert total == expected_results[i]

def test_four_should_get_valid_total():
        #Arrange
        result_dices = [[1,1,1,1,1], [2,2,2,2,2], [2,4,4,1,1], [2,2,1,2,2]]
        expected_results = [0,0,8,0]
        for i in range(len(result_dices)):
                game = Yatzy(result_dices[i][0],result_dices[i][1],result_dices[i][2],result_dices[i][3],result_dices[i][4])
                #Act
                total = game.fours()
                #Assert
                assert total == expected_results[i]


def test_crazy_change():
        #Arrange
       result_dices = [[1,1,1,1,1], [2,2,2,2,2], [1,2,1,2,1],[2,4,6,2,2]]
       expected_results = [10,30,18,48]
       #Act
       for i in range(len(result_dices)):
                total = Yatzy.crazy_change(result_dices[i])
                #Assert
                assert total == expected_results[i] 


