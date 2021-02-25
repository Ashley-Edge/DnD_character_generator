![D&D logo](https://db4sgowjqfwig.cloudfront.net/game_systems/251/assets/357032/DnD5E_Large.png?1407685841)
# Simple Character Generator

This repository forms my DevOps Core Practical Project Specification individual project. At its core, I will be creating an application that generates a random race, class and weapon to help you start your journey in Dungeons & Dragons. I am required to create a service-orientated architecture for my application, this application must be composed of at least 4 services that work together.

The requirements set for the project are below:

- A Kanban board
- An Application fully integrated into GitHub, built through Jenkins and deployed to a GCP virtual machine
- Use Webhooks so that Jenkins recreates and redeploys the changed application from GitHub
- The project must follow the Service-oriented architecture of at least 4 services that work together
- The project must be deployed using Docker and Docker Swarm
- Create an Ansible Playbook that will provide the environment that your application needs to run
- The project must make use of NGINX (reverse proxy) to make your application accessible to the user

You should consider the concept of MVP (Minimum Viable Product) as you plan your project, complete all the requirements before you add extra functionality that is not specified above.

## Planning
I used a Trello board to plan and keep on top of my tasks. I used simple to-do, doing and done lists. I can set myself tasks in the to-do list, remember what I am working on in the doing list (so I can juggle a few tasks at once) and once I have finished a task I will drag it into the done list. [Click here is see it](https://trello.com/b/yaZs4MWM/dd-character-generator)

My initial Trello board layout to get me started. More tasks will be added to the to-do list as required
![Initial Trello board](https://trello-attachments.s3.amazonaws.com/602d3594eb14c72fafa7733c/602fea0f92ff805d8db0d4d4/a73aa479e027544251dc59aba9caf679/Trello_start_point.png)

## Architecture

I am are required to create a service-orientated architecture for my application, this application must be composed of at least 4 services that work together. Service 1 will be my app's core service. Service 1 will render my Jinja2/HTML templates I need to interact with my application, it will also be responsible for communicating with the other 3 services, and finally for persisting my character data in an SQL database. Service 2 and 3 will both create a random Race and Class respectively for the D&D character, grabbed from the official D&D Player's Handbook. Service 4 will create a weapon for your character to fight with, this weapon will be based upon the results from service 2 and 3 using some pre-defined rules. For the purpose of this project, I will be keeping my application simple in order to hit the MVP in time for the deadline. For services 2, 3 and 4 I am required to create 2 different implementations, I must be able to demonstrate swapping these implementations out for each other seamlessly, without disrupting my user's experience. I will talk about this later on in this README.md file.

My service-orientated architecture plan
![service-orientated architecture diagram](https://trello-attachments.s3.amazonaws.com/602d3594eb14c72fafa7733c/60315b4627b35b4d8fdbc918/e69a347f558248f398c84848cc20f915/services.png)

## Service1

Service 1 basically performs a **GET** request on services 2 and 3, and a **POST** request on service 4. It talks with the other services(2, 3 & 4) to gain the data needed from a MySQL database. Service 1 then uses that information to display it to the user through my HTML/Jinja2 index.html file. Below is plan and result of my app.  The current generated character will be presented followed by a new character button that will essentially refresh the page.

![HTML](https://trello-attachments.s3.amazonaws.com/602d3594eb14c72fafa7733c/602fed8a01141c2618582185/ad9dd739bf1a6ebe3cf1d9e51ae51c60/html_plan_%26_result.png)

## Database table

I will be using MySQL to house and generate my D&D characters. Service 1 will determine the characters race, service 3 will determine the characters class and service 4 will combine the results from service 2 and 3 and generate a weapon.

![database table](https://trello-attachments.s3.amazonaws.com/602d3594eb14c72fafa7733c/602fe59f98cc114b9881c1d5/6faa609d7cce40ba514acdd5194d0dcd/ERD.png)

## Acknowledgements

I would like to thank all my trainers (Ben Hesketh, Jay Grindrod, Nathan Forester Peter Rhodes and Raji Kolluru) for their teaching and support. I would also like to thank my classmates for their help, support and motivation, as well as the community of stack overflow. I would also like to state that I in no way own the Races, Classes and Weapons mentioned in this application. All information (Logo's included) belong to Dungeons & Dragons and sourced from their "Player's Handbook" 5th edition. If you have stumbled upon this app, liked it and wish to use it yourself, feel free. If you have any notes for improvements I would love to hear from you.

