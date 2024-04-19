## Time-Series Forecasting with Prophet

This repository is for a hands-on presentation focused on using prophet for time series analysis. It covers:
- a **high-level overview of time series analysis**
- an **illustration of Facebook's python** package called prophet by using AirPassengers data, modeling the number of passengers flying to Austrailia in the 1960s.
- an **application of prophet in the public sector** (predicting rat activity in NYC neighborhoods)

For more information about this work and a step-by-step guide, see the ipynb file [prophet_session.ipynb](/prophet_session.ipynb). Thanks!

If you'd like to learn more about my approach or have questions on the methods, please feel free to reach out to me directly at [claire.k.boyd@gmail.com](mailto:claire.k.boyd@gmail.com).



*Implementation notes:*

If you want to convert / update the `.ipynb` into `.slides.html`, you can do so using the [`jupyter nbconvert`](https://github.com/jupyter/nbconvert) module, issuing the following command within your project directory:

```bash
jupyter nbconvert prophet_session.ipynb --to slides --post serve
```