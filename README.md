# Metal Detecting Rover
An metal-detecting rover developed with mentorship and technical guidance from engineers at BAE Systems. Uses a Raspberry Pi Robo Pico board with integrated motor drivers and MicroPython to control the motors and sensor.


I worked in a team of 4 students between October 2024 and July 2025 to build a prototype rover capable of navigating through a 5x5 grid and detecting buried copper using a metal detector sensor. As part of the software side of the team, my role was to control the motors and ensure that the rover stops when metal is detected and notifies the user. 

The project's purpose at a larger scale would be remote automated landmine detection in hazardous areas to reduce the risk of direct human involvement, but currently this project is a proof of concept. Copper was selected as the representative metal due to its presence in some landmine components. The project was conducted in an educational environment using small copper samples.

## Technical Challenges and Solutions

### Motor Control

One of the main technical challenges was achieving reliable rover movement due to difficulties with the original motor controllers on a Raspberry Pi 5.

We addressed this by transitioning to a Robo Pico board, whose integrated motor drivers simplified programming and improved movement control.

### Metal Detection and User Notification

A key achievement was successfully programming the rover to stop and notify the user when metal was detected. This functionality required several days of testing, debugging and refinement.

## Project Presentation

The rover was presented at the Chelmsford Science and Engineering Society (CSES) TEXPO Competition at Anglia Ruskin University.

Our team demonstrated the project and discussed its design, functionality and potential improvements with judges, receiving valuable technical feedback.

## Future Improvements

- Improved navigation: Making it completely autonomous through the use of sensors that allow for the rover to detect and navigate past obstacles
- More reliable metal detection: Due to our limited budget, our metal sensor can only detect copper reliably up to a very small depth. If we had a greater budget, we could buy a more sophisticated sensor.
- Build a proper user interface to display notifications from the rover
- Add a camera module and GPS sensors so that the rover could take a picture of the "landmine" and send it back to the user.

## Rover Prototype and Demonstration

<p align="center">
  <img src="https://github.com/user-attachments/assets/0aa3a518-e7d4-4ce7-9c4a-ee43ae543c1f" width="500" alt="Rover Image">
</p>

<div align="center">
  <video src="https://github.com/user-attachments/assets/e6146a1a-5dd8-4d6c-a9eb-96dbaad2ed56" width="300" controls></video>
</div>



