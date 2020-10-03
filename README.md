# JazzIt 🎷

[![Open All Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sangarshanan/jazzit/blob/master/notebook.ipynb)
[![License](https://img.shields.io/pypi/l/jazzit.svg)](https://github.com/Sangarshanan/jazzit/blob/master/LICENSE)
[![DeepSource](https://deepsource.io/gh/Sangarshanan/jazzit.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Sangarshanan/jazzit/?ref=repository-badge)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/sangarshanan1998@gmail.com)

Ever wanted your scripts to play music while running/ on erroring out?

Of course you didn't

But here it is anyway


### Install

```
pip install jazzit
```

### What it do?

With `Jazzit` you can just add a decorator to your functions and jazz it up 

- You can have a elevator music to go along with your long running script
- Play humiliating music when it errors out to put you in your place

There are default tracks you can use, or you can use your own custom tracks

### How to do it?

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
        raise Exception("BE POSITIVE!!!")
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

To satisfy your WHAT !!! IT WORKED !!! moments


```python
from jazzit import success_track

@success_track("anime-wow.mp3")
def add(a,b):
    print(a+b)

if __name__ == "__main__":
    add(12, 42)
```

The in-build tracks are bruh_moment, elevator and curb_your_enthusiasm but you can add your custom tracks and urls

Check out some of the [examples](https://github.com/Sangarshanan/jazzit/tree/master/examples)


### Jupyter Notebook 

Check out the colab link above or the example [notebook](https://github.com/Sangarshanan/jazzit/blob/master/notebook.ipynb)

### Use Jupyter Magic:

Load inside a Jupyter notebook

``` python
%load_ext jazzit
```

Running away from the PEP8 police 🚲🚓

```python
%%waiting_track -t elevator.mp3

def fibonacci(n):
    if n < 0:
        raise Exception("BE POSITIVE!!!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for num in range(1, 35):
    print(fibonacci(num))
```

For those BRUH moments in your life

```python
%%error_track -t bruh.mp3 -w 3

for num in reversed(range(10)):
    print(10/num)
```

It worked !!!

```python
%%success -t anime-wow.mp3 -w 3

for num in range(10):
    print(num ** 2)
```

There are two arguments in play here 

`-t` or `--track` that needs the sound track (Can be a file path, url, inbuilt tracks)

`-w` or `--wait` (Optional, default is 3 seconds) Wait for x seconds before cutting the music 


### Dependencies

Jazz added with [playsound](https://github.com/TaylorSMarks/playsound)

If you getting hit with `ModuleNotFound` errors while running jazzit

You might need to install Pygobject https://pygobject.readthedocs.io/en/latest/getting_started.html


> :warning: **Use wisely**:  Best suited for scripts you run non-professionally!


### Profiling

TL;DR It is definitely slower with music

I did a lil profiling on bin/profiler.py

> Without Music

Time to run : 5.2486350536346436 secs

> With Music

Time to run: 5.270173072814941 secs

Memory profiling `python -m memory_profiler bin/profiler.py`

### Social 

Hacker News: https://news.ycombinator.com/item?id=24485447

Twitter: https://twitter.com/sangarshanan/status/1305933704007573504

[amrrs](https://github.com/amrrs) put together a video https://youtu.be/qkyQfIjvPmM :)


### Disclaimer

Default tracks were pulled from royalty-free stock audio sites (They are mostly gaming and meme sound effects)

