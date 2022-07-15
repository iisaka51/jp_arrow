# jp_arrow.
Conver date/datetime from/to Japanese date/datetime.

This module highly depend on "arrow".

## Install

`pip install jp_arrow`

## How to use

```python
In [1]: import jp_arrow

In [2]: jp_arrow.utcnow().format('EEYYYYMMDD', locale='ja')
Out[2]: '令和04年0715日'

In [3]:
```



