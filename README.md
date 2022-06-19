# saneround

Python package providing sane round() instead of official insane round().

## Quick start

Install this package using pip:

```console
pip install saneround
```

Import `saneround` package as `sr` and use `sr.round(number: Union[int, float], ndigits: int = 0) -> float`:

```python
>>> import saneround as sr
>>> sr.round(0.4)
0.0
>>> sr.round(0.5)
1.0
>>> sr.round(1.4)
1.0
>>> sr.round(1.5)
2.0
>>> sr.round(-0.4)
0.0
>>> sr.round(-0.5)
-1.0
>>> sr.round(-1.4)
-1.0
>>> sr.round(-1.5)
-2.0
>>> sr.round(1234.567, 2)
1234.57
>>> sr.round(1234.576, -2)
1200.0
```

## Comparison with others

There are some similar packages:

- builtin
- round2 (0.0.4)
- math-round (0.0.3.post1)
- math-round-af (1.0.3)

Comparison results are here:

||saneround|builtin|round2|math-round|math-round-af|
|---|---|---|---|---|---|
|round(0.5)|1.0|0|1|1|1.0|
|round(1.5)|2.0|2|2|2|2.0|
|round(-0.5)|-1.0|0|-1|0|-1.0|
|round(-1.5)|-2.0|-2|-2|-1|-2.0|
|round(0.49999999999999994)|0.0|0|0|1|0.0|
|round(1.255, 2)|1.26|1.25|1.25|1.25|1.25|
|round(123456.78, -2)|123500.0|123500.0|nan|123500.0|Error|
|round(0.12345, -1)|0.0|0.0|nan|0.0|Error|
|round(42.0, 308)|42.0|42.0|nan|Error|Error|
|round(0.42, 2**30)|0.42|0.42|nan|(too late)|(too late)|
|round(2.5e20, -20)|3e+20|2e+20|nan|3e+20|Error|
|round(0.5, 23)|0.5|0.5|-1.0717247280990649e-08|0.49999999999999994|0.49999999999999994|

saneround is very robust.
