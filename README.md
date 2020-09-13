# JazzIt 🎷

Ever wanted your scripts to play music while running/ on erroring out ?

Of course you didn't

But here it is anyway


### What it do ?

With `Jazzit` you can just add a decorator to your functions and jazz it up 

- You can have a elevator music to go along with your long running script
- Let your script play a humiliating music when it errors out    

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

Sip coffee to elevator music while your scripts is running

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


Check out some of the [examples](https://github.com/Sangarshanan/jazzit/examples)


> :warning: **Use wisely**:  Best suited for scripts you run for non-professionally !


### Sum profiling


I did a lil profiling on bin/profiler.py

> Without Music

Time to run : 5.91 sec

```
Line #    Mem usage    Increment   Line Contents
================================================
    27   25.277 MiB   25.277 MiB   @profile
    28                             def run_no_music(limit):
    29   25.277 MiB    0.000 MiB       for num in range(1, limit):
    30   25.277 MiB    0.000 MiB           print(fibonacci(num), num)
```

> With Music

Time to run: 5.826 sec


```
Line #    Mem usage    Increment   Line Contents
================================================
    28   25.070 MiB   25.070 MiB           def wrapped_function(*args):
    29   25.070 MiB    0.000 MiB               track_path = get_track_path(self.track)
    30   25.070 MiB    0.000 MiB               pygame.mixer.music.load(track_path)
    31   25.070 MiB    0.000 MiB               try:
    32   25.070 MiB    0.000 MiB                   pygame.mixer.music.play(loops=-1)
    33   25.070 MiB    0.000 MiB                   original_func(*args)
    34                                         except KeyboardInterrupt:
    35                                             pygame.mixer.music.stop()
    36                                         finally:
    37   25.070 MiB    0.000 MiB                   pygame.mixer.music.stop()
```


### Disclaimer

Default tracks were pulled from https://www.youtube.com/user/gamingsoundfx/

No Copyright Infringement Intended

I might take down these tracks or add more depending on the number of lawsuits I get slapped with
