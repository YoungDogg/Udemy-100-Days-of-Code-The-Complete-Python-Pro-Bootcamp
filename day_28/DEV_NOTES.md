# OVERVIEW
- communicating with classes is hard. 
- callback bridged them.
- there are still lot of things to fix and append. Cease from here. Proceed to next project~~~~

# TODO
- [x] separate ui work inside countdown class
  - [x] update_ui at main.py
- [x] start, stop, and reset
  - [x] start
    -[x] how to pass countdown class function to ui?
      - [x] bridging main class as connector
    - [x] how to set scope functions of a class?
      - same as attributes
        - public (default)
        - protected (convention) : a single underscore within its subclass
        - private (name mangling): two underscores only its class
    - [x] if start pressed again, it stops
      - [x] toggle text start to stop
      - [x] stop function worked
        - storing the value inside countdown class  
  - [x] reset
    - [x] if pressed reset, make button stop
- [x] routine: work and break
  - [x] change countdown, pomocycle, and main classes compatible with this routine
    - [x] countdown class
      - [x] divide above with start, stop, and reset into different classes
    - [x] pomocycle      
    - [x] main class - connecting countdown and pomo class
  - [x] when the process finished both start and reset button reset the process
    - [x] when reset pressed, make the routine reset too
    - [x] if press start button, reset and start again
    - [x] works one more than expected. fix this
    - [x] short break counts from 1, fix it to count from 0
    - [x] long break is not working, fix it
  - [x] ui
    - [x] display work and break progress
      - [x] not yet: background, no color; font color: black
      - [x] current: background, red; font color: white
      - [x] done: background, green; font color: white
        - how to check current state? Check by WorkState and TimerState 
          - if its TimerState is changed from RUNNING to STOPPED, regard it has done
        
- [x] refactor
  - [x] enum: UIText, TimerState, WorkState
    - UIText class required `.value` while timer_state didn't. 
      - UIText needs its vlaue while timer_state only checks logical states
- [x] test
  - [x] how to make test class?
  - testing routine with hardcoding is not good. Any good method?
    - made beneath `if __name__ == 'main'`
- [ ] document
  - [ ] following the process
    

