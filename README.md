# simulation_initialization_ros_tool
Initialization of all parts of the simulation framework. **Launchfiles only!**



## Installation
* this package is part of the simulation framework
* see simulation_management_ros_tool for installation and more details

## Usage
* launch the file `launch/_whole_framework.launch`

#### Launchfile Overview

```
simulation_initialization_ros_tool
    │
    ├── simulation_management_ros_tool *
    │   │
    │   ├── time_mgmt
    │   ├── localization_mgmt
    │   └── object_initialization
    │
    └── objects
        │
        ├── vehicle1
        │   ├── perception *
        │   ├── prediction *
        │   ├── planning *
        │   └── communication *
        │
        └── vehicle2
            ├── perception *
            ├── prediction *
            ├── planning *
            └── communication *
            
* = repositories (so they must include a launchfile which has to be called)
all other launchfiles inside here
```
* initialization launches the simulation management and the objects
* simulation management launches the single management nodes
* the objects launch their 4 modules
* each of the modules launch their nodes

#### Vehicle Initialization
* vehicles are initialized by a path and an initial velocity

## License
This package is distributed under the 3-Clause BSD License, see [LICENSE](LICENSE).
