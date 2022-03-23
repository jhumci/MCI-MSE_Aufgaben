## Project background

### Purpose of project

Ambitious athletes should be provided with precise and reliable performance data. This should enable the athletes to further enhance their performance. 

### Scope of project

Athletes will provide the system with data recorded by an ergometer. The generated data from the test procedure consists of a three-minute performance test with a fixed performance goal. Heartrate and performance over time are thereby recorded and stored separately.

### Other background information

...

## Perspectives
### Who will use the system?

Athletes will use the system to assess their performance through a standardised performance testing procedure. Diagnosticians will use the system to process the athletes data. That includes manually defining the scope of the testing procedure as well as visualizing the athletes data and storing it in the right location.

### Who can provide input about the system?

Athletes are providing the ergometer with input. The system then interprets the input from the ergometer and redirects them to a defined interface. Diagnosticians will have the ability to manipulate the framework conditions thus influencing the process of visualizing and storing the athletes data.


## Project Objectives
### Known business rules

none

### System information and/or diagrams

Example of recorded ECG data
![](ekg_example.png)

The heart rate must be determined from this.

### Assumptions and dependencies

The system does have external dependencies from the ergometer as well as from the diagnostician.
The diagnostician has to initiate the test procedure via the command line as there is no user interface yet.
The ergometer has to provide the system with data.

#### What information is included in the data?

The data includes the ecg-data from all three subjects, aswell as the power-data of each of them. With that data you can calculate important results.

#### How is the data resolved in time and how long are the performance tests?

### Design and implementation constraints

- Until a user interface is established the system is operated via the command line. 
- Athlete data includes their name, a technical ID as well as their date of birth. 
- The plots and the processed data are to be stored together.
- Successful and aborted attempts are to be stored in separate folders.

## Risks



## Known future enhancements

Implementing a user interface.

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

...
