# Error Detection and Correction

## Objective
This project demonstrates two simple error detection techniques:
- Parity Bit
- Checksum

## What is a Parity Bit?
A parity bit is an extra bit added to the data. It helps detect if a single bit changes during transmission.

## What is a Checksum?
A checksum is calculated by adding the ASCII values of all characters in the message. The receiver calculates it again and compares it with the original checksum.

## Which Worked Better?
Both parity and checksum detected the simulated single-bit errors in this project. However, checksum is generally more reliable because it can detect a wider range of errors than a simple parity bit.

## Language Used
Python

## Author
Your Name