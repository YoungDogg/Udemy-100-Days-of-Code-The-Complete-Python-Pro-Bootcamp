# Guess US States
# Rules
- Convert the guess to Title case
- Check if the guess is among the 50 states
- Write correct guesses onto the map
- Use a loop to allow the user to keep guessing 
- Record the correct guesses in a list
- Keep track of the score

# what will require
- [x] Check if the guess is among the 50 states
  - [x] the array of 50 states
- [x] Write correct guesses onto the map
  - [x] get state place coordinate considering click margin
    - [x] get the coordinate of game window
    - [x] compare with the coordinate data list
      - [x] get coordinate data list
      - [x] make condition comparing the coordinates of clicking and the data list 
      - [x] get corresponding state name 
    - [x] input popup
      - [ ] handle the error (optional)
        - [ ] if click no
  - [x] condition comparing input and the state list
    - [x] make the condition
    - [x] make the score
      - [x] UI
        - [ ] highest score
      - [x] file
  - [ ] Refactor
    - [ ] Divide into classes
      ~~- [ ] screen~~
      - [ ] data
      - [ ] condition
      - [ ] score