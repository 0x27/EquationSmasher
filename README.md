# EquationSmasher
NSA EquationGroup C&C Hunter using the Shodan API

Ala [The Italian Job](https://github.com/0x27/TheItalianJob) with regards to HackingTeam, this one hunts down NSA "Equation Group" C&C servers. All of them are dead now, NSA pulled them down after getting 0wn3d 4nd 3xp0z3d and all that, but they *were* valid on 2015-02-23. Below is a paste of some C&C servers identified. I am uploading it now for historical reasons, and also because, well, the "Italian Job" is now public after Phineas rekt HT.

This work would not be possible without the inputs of various security researchers, especially [that magnificent bastard March (the rootkit wizard)](https://twitter.com/_ta0)

Dump of DDoS numbers Enumerated back in Febuary.
```
87.255.34.242
66.175.120.181
80.77.4.3
209.59.37.180
87.255.34.242
66.175.120.181
80.77.4.3
209.59.37.180
85.112.21.213
87.255.34.242
66.175.120.181
80.77.4.3
209.59.37.180
85.112.1.83
85.112.21.213
87.255.34.242
66.175.120.181
80.77.4.3
209.59.37.180
85.112.1.83
85.112.21.213
87.255.34.242
66.175.120.181
80.77.4.3
209.59.37.180
85.112.1.83
```

Again, you will need a [Shodan](https://shodan.io) API key and the Shodan python module.
```
$ pip install shodan # this installs the shodan module :)
```

Basically how all this works is, these scumbags C&C servers behave "wierdly" and send strange headers, which are easy to identify. No matter how "legit looking" they try be, we will always be able to locate them :)

Remember, those who would spy on us, try fuck with us, and generally be scumbags: Mess with the best, die like the rest. There are more of us than you, and we will not take your fuckery lightly <3

Licence: WTFPL
