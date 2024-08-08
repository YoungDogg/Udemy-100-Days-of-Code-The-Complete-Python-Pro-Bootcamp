### Game Flow

1. Game starts.
2. A ball is launched towards either the player or the opponent.
3. If the ball is hit by a paddle, it bounces back at an angle and increases in speed.
4. If the opponent hits the ball, the process repeats.
5. If the ball is missed, the opposing player scores a point.
6. Repeat steps 2-5 until either player scores 10 points.
7. Display the winner and prompt for replay or quit.

### Adjustable Values

- Initial ball speed.
- Incremental ball speed increase upon each hit.
- Speed of AI when chasing the ball.
- Size of paddles.
- Winning score (default to 10).
- Prompt for replay or quit game after the game ends.

### Required Classes

#### Paddle Class
- **Attributes**: speed, size, color, score
- **Methods**:
  - `hit_ball(ball)`: Calculate the new angle and speed when the ball is hit.
  - `move()`: Handle the movement of the Paddle.

##### Player Class (inherits from Paddle)
- **Attributes**: key bindings for movement.
- **Methods**:
  - `handle_input()`: Update Paddle position based on player input.

##### Opponent Class (inherits from Paddle)
- **Attributes**: AI speed.
- **Methods**:
  - `chase_ball(ball)`: Update Paddle position to follow the ball.

#### Ball Class
- **Attributes**: speed, size, color, direction.
- **Methods**:
  - `move()`: Update ball position.
  - `check_collision()`: Determine if the ball has hit a Paddle or the screen edges.

#### Collision Class
- **Attributes**: None (stateless utility class).
- **Methods**:
  - `handle_collision(ball, paddle)`: Calculate new ball direction and speed based on the collision.
  - `handle_screen_collision(ball)`: Calculate new ball direction when it hits the screen edges.

#### GameFlow Class
- **Attributes**: player, opponent, ball, score limit.
- **Methods**:
  - `start_game()`: Initialize and start the game loop.
  - `update_score(winner)`: Update the score and check for game over.
  - `check_game_over()`: Determine if the game has ended and display the winner.

### Question on Inheritance and Composition
For the relationship between `Collision`, `Ball`, `Player`, `Opponent`, and `Screen`, you should use composition rather than inheritance. Here's why:

- **Composition over Inheritance**: The `Collision` class should not inherit from other classes because it acts more like a utility or helper class that handles interactions between objects.
- **A-is-B vs. A-has-B**: In your case, `A-has-B` is more appropriate. For example, `GameFlow` has `Ball`, `Player`, and `Opponent` objects, and it uses the `Collision` class to handle their interactions.