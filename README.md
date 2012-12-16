checklist
=========

A tool for executing interactive checklists. Define a checklist with special command operators and let the tool execute the list. I use this in the morning to go through my routines at work and I suspect it might be useful for others.

For examples see the file example.chk.

Commands
--------

Commands contain an operator and a description, separated by a space.

These operators are available:

* \* The description is printed.
* ? The description is printed and should be answered with y or n. All following lines that match the answer are printed. Execution will continue on the first character that is not y or n.
