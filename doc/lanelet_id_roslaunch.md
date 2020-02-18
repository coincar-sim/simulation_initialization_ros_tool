# Lanelet IDs in roslaunch

## Problem
`xmlrpclib.py` as used by `roslaunch` does not support type `long`:

```xml
<arg name="lanelet_id_goal" value="12345678910111213" />
```
results in an error.

## Workaround
We use the following workaround:
- (optionally) add the substring `long` to the lanelet id in launchfiles, making it a string, e.g.
```xml
<arg name="lanelet_id_goal" value="12345678910111213long" />
<!-- or -->
<arg name="lanelet_id_goal" value="1234long" />
<!-- or -->
<arg name="lanelet_id_goal" value="1234" />
```
- remove this substring if present when parsing lanelet ids (as string) from the parameter server and convert to long subsequently
