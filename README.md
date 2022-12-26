# STAI
### What does it do?
 - Provides a way to train models and manipulate data at the same time using methods like
    - hyperthreading
    - time slicing
    - action queues
 - Simplistic UI that allows for easy manipulation
### Limitations
  - the max amount of threads possible at one time is equal to:
    - n = amount of cores in cpu
    - * 2 if { hyper threading exists on device }
  - Working on a way to bypass GIL safely
