# UI
- UI class should be formatted as the following image.
- `def __init__`
  - it only initializes attributes not assigning.
  - it has `def set_up()`
- `def set_up()`
  - it has all the `set_somthing()` like `set_root() set_card()`
  - including methods
    - `_set_root()`
    - `_set_card()`
    - `_set_v_button()`
    - `_set_x_button()`
- root --or canvas
  - The default window size is dynamical.
  - As I learned in tkinter and ttkinter, row and column grid is good. If there are better method, feel free to use it.
- card
  - The displayed card is clickable. If it's clicked it shows the different language with different color.
  - the card flip method
    ```
      def flip_card(self)
        # display other side of the card showing different background color. show different language(card['korean'])
     ```
  

- button
  - ✅ button
    - it sends that the check button clicked.
  - ❌ button
    - it sends that the x button clicked.
  - their command should have call method
    ```
        def v_btn_command(self):
        if self._v_btn_command:
            self._v_btn_command()
    ```
- class generating rule
  - All the methods should follow scope like `_set_canvas() self._window = None`
    - all attributes and methods are private as default. If it's public, then I'll notice it. 
  - Docstrings
    - class explains its features with attributes and methods 
    - methods has docstrings too.
  - test case
    - All classes have `if __name__ == "__main__":` for its test case. 
    - test every method.
- result
  - all printed result code should be enclosed with `` for better paste