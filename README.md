# CLI test
## Setup
* Create the venv: `python3 -m venv env`
* Activate venv: `source env/bin/activate`
* Install dependencies: `pip install -r requirements.txt` 
* Deactivate venv: `deactivate`

## Run tests
* add ability to run tests in `pytest`

## Questions
* what error states are we handling?
    * just `readConsole()` and `writeConsole()` throwing the exceptions listed?
    * what other errors that will need to be handled?
* instructions mention `stationary` response, how to verify `stationary`
    * get 2 sets of coordinates and verify that has not changed?
        * what causes the second set of coordinates to be gathered (wait state?)
* will `readConsole()` receive a set of `x`,`y`,`z` coordinates before the next is sent?
    * aka will not recieve 2 `x` coordinates before the corresponding `y` and `z`
    * will all three coordinates always be sent?
* will the `x`,`y`,`z` coordinates always have valid values?
    * aka all valid float values
    * can they be negative?
* need to handle corrupted data?
    * results invalid, incomplete or mangled
    * missing datapoints
    * results not returning in a timely fasion / never complete
* value in tracking errors seperately?
    * aka `NotConnected` from `readConsole()` logged differently than `writeConsole()`

## Improvements
* handle unknown exceptions
* actually connect to `testConsole` module to gain access to `writeConsole()` and `readConsole()`
* add more tests
    * `writeConsole()` handles invalid input 
    * `readConsole()` returns valid coordinates
    * test repeated calls
    * tests for `log` data points
    * negative tests
        * handle corrupted data
        * incomplete results
* mock out `writeCommand()` and `readConsole()` so test is actually runnable in `pytest`
    * __assumption:__ `pytest` is the preferred testing framework
* capture performance metrics
    * timing data
    * system stats
* standardize function naming, CLI calls are camelCase, python norm is underscore, is there a standard that should be followed?
* add CI run
* add linter


