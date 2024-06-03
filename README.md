# CovertLang

Language made after doing the Hack Club easel tutorial... with a spy theme.

## Language ideas
- Extension: file.covert
- all programs are known as an agency
- variables are suspects
- functions are known as `agent`s 
    - values are returned by `report`
- iteration is structured as a map 
    - `stakeout` with suspects (an input iterable) is passed one at a time to another agent to process
    - each agent has to return a report which is compiled at the end of the iteration
- conditionals are structured as
    - `investigate`, `then`, `fallback` (else)
- Importing modules (this might take a while to implement)
    - Agency `employs` another file or some special cases for standard libraries. I won't deal with importing things straight into the scope everything will have to be accessed with dot notation with the file name