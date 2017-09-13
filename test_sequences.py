#!/usr/bin/env python3
import sequences

def test_fibonacci():
    result = sequences.fibonacci(5)
    correct = [1, 1, 2, 3, 5]
    assert result == correct

def test_fibonacci2():
    result = sequences.fibonacci(5)[-1]
    correct = 5      
#  correct = 434665576869374564356885276750406258025646605173717804024817290895365554179490518904038798400792551692959225930803226347752096896232398733224711616429964409065331879382989696499285164476137795166849228875
    print(result)
    assert result == correct
 

