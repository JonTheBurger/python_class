# Homework 2: Speeding Ticket
In this assignment you will be creating a program to create speeding tickets. You should first gather all of the
information you need from the user to create the ticket, then print the full ticket to the screen. Your parking 
ticket will need the following information:

1. First Name
2. Last Name
3. Age
4. License Plate Number
5. Base Fine

- If the driver was driving 5 or fewer miles over the speed limit, there is no fine.
- If the driver was driving over 5 but less than 20 miles over the speed limit, they must pay $20 for every 5 miles 
they drove over the speed limit.
- If the driver was driving 20 miles or more over the speed limit, they must pay $50 for every 5 miles they drove over 
the speed limit.
- For these 2 cases, you may decide whether or not the fine is applied all or nothing per 5 mile increments, or 
continuously applied over all speeds over the limit.
- If the driver was in a construction zone, this base fine is doubled.
- If the driver is under 21, they must pay an additional $30 under age fee.
- If the driver was intoxicated, the entire fine will be doubled.

Your program's output may look something like this:

```bash
SPEEDING TICKET GENERATOR
Last Name:
Povirk
First Name:
Jon
Age:
22
License Plate Number:
EGX-5493
Speed Limit:
30
Actual Speed:
40
In Construction Zone? (y/n)
y
Intoxicated? (y/n)
n

TICKET:
Jon Povirk
Age 22
License Plate Number: EGX-5493
Fine: $80
```
