# JazzIt 🎷

Ever wanted your scripts to play music while running/ on erroring out ?

Of course you didn't

But here it is anyway


### Install

```
pip install jazzit
```

### What it do ?

With `Jazzit` you can just add a decorator to your functions and jazz it up 

- You can have a elevator music to go along with your long running script
- Play humiliating music when it errors out to put you in your place

There are default tracks you can use, or you can use your own custom tracks

### How to do it ?

Play Frolic from curb your enthusiasm to keep you in your place

```python
from jazzit import error_track

@error_track("curb_your_enthusiasm.mp3", wait=7)
def run():
    for num in reversed(range(10)):
        print(10/num)

if __name__ == "__main__":
    run()

```

Sip coffee to elevator music while your script is running

```python

from jazzit import waiting_track

def fibonacci(n):
    if n < 0:
        raise Exception("BE POSITIVE !!!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@waiting_track("elevator.mp3")
def run(limit):
    for num in range(1, limit):
        print(fibonacci(num))

if __name__ == "__main__":
    run(1000)
``` 

The in-build tracks are bruh_moment, elevator and curb_your_enthusiasm but you can add your custom tracks 


Check out some of the [examples](https://github.com/Sangarshanan/jazzit/tree/master/examples)


> :warning: **Use wisely**:  Best suited for scripts you run for non-professionally !


### Dependencies

Jazz added with [playsound](https://github.com/TaylorSMarks/playsound)

If you are ubuntu and getting hit with `ModuleNotFoundError: No module named 'gi`

You might need to install Pygobject https://pygobject.readthedocs.io/en/latest/getting_started.html


### Profiling


I did a lil profiling on bin/profiler.py

> Without Music

Time to run : 5.2486350536346436 secs

> With Music

Time to run: 5.270173072814941 secs

Memory profiling `python -m memory_profiler bin/profiler.py`


### Disclaimer

Default tracks were pulled from https://www.youtube.com/user/gamingsoundfx/

No Copyright Infringement Intended

I might take down these tracks or add more depending on the number of lawsuits I get slapped with
