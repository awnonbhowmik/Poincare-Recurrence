# Poincare Recurrence
The Poincare Recurrence Theorem states that, provided a certain level of entropy is introduced into a restricted, bounded and ordered system - the system eventually reaches a state that is close to or exactly equal to the original state, in some large but finite time.

We demonstrate this phenomenon with a simple shuffle game. Suppose that we have two urns A and B.
# The Algorithm
  - urn A contains n elements, urn B is empty
  - pick some elements at random and put into urn B
  - call a random number x within (0,n)
  - if x is in urn A, switch to urn B and if x is in urn B, switch to urn A
  - stop the program once urn B is empty that is, the system has returned to its original state
  - count the steps in doing so

# Programming Language
  This algorithm has been implemented twice, once with C++ and the other with Python 3.xx

# Note to users
  Please do not use a large value to start. Even an input of 5 might take some time to execute and provide output. This code is solely dependent on whether the randomizer only picks the elements that are present in urn2 - otherwise it will keep running indefinitely. Your system temperature might rise.
