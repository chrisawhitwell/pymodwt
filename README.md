# pymodwt
Based on the methods presented in Percival and Waldens "Wavelet Methods for Time Series Analysis". This is a (very slightly) modified package (See original: https://gitlab.com/Cimatoribus/wmtsa-python).

Modifications include:
- Changed to work with python 3 and numpy 1.2 (I think that was the version that broke it?)
- Removed cython implementation (much slower but far more portable - especially on windows machines)

Not everything has been changed over or tested. Good luck!
