# Game Flow
1. Game starts.
2. A ball comes to either side, player or opponent.
3. If it hits the ball, it bounces back with some angle with speeding up.
4. If the opponent hits the ball, repeat.
5. If missed it, count one up on winner's board.
6. Until either score hits score 10, Repeat the game progress.
7. Show which one won.
# Adjustable Values
- Ball speed when bouncing back
- Speed of AI when chasing ball
- Size of their bars
- Score to reach the game over
  - Asking replay or quit game
# Required Classes
- Bar class 
  - about bar: speed, size, color, ball angle when hit the ball, score  
    - Player(Bar) class
      - adding keybinding
    - Opponent(Bar) class      
      - speed of chasing ball
- Ball
  - speed, size, color, shape
- Collision <- mediator class
  - Ball
    - Bar
      - when hit, run the angle bending method
    - Screen
      - when hit, runt the angle bending method
- GameFlow
  - start the game
  - count score
  - judge game over 
# Question
- Inheritance of Collision and Ball, Player, Opponent, and Screen, A-is-B or A-has-B?
  - They all are related to collisions. How to hand it?
  
