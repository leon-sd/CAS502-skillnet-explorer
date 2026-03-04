# Skillnet Explorer

## Project info

**Team members**
- Emmanuel S Dumaguing (GitHub: leon-sd)
- Kyle Gitchell (GitHub: kagitche)
- Course: CAS502

**Project description**
SkillNet Explorer is a small command-line tool for exploring how skills co-occur across occupations. Using O*NET skill importance data, it builds a weighted network where nodes are skills and edges indicate how often two skills appear together within the same occupation above a threshold. Given a skill code, the tool returns the top co-occurring (“neighbor”) skills ranked by edge weight and provides example occupations as evidence for each pairing.


**Branching / PR workflow**
- Default branch: `main`
- For Module 3 setup and small fixes, we are committing directly to `main` to keep the workflow simple.
- If we make larger changes (new features), we will create a feature branch and open a Pull Request before merging back to `main`.


**Project planning docs**
- Challenges: `Challenges.txt`
- Communication plan: `Communications_Plan.txt`

## What the code does

This script will read the skills in `data/Skills.xlsx` (which is pretty much a list of types of jobs and what skills each job requires) and create a weighted graph from it. Each skill is identified by an "Element ID" of the form `Number.Letter.Number.letter` (e.g. `2.A.1.a`). The script will create a node for each skill id and if two skills are used in the same job type, the nodes will be connected. The more often two skills are used together for a job type, the greater the weight on the edge between those two nodes. The resulting network looks something like that (darker and thicker edges have more weight):
![Network Image](img/networkjpg.jpg)

After creating the network, the script will ask the user to input a skill and then print the first 10 skills most often used with the entered skill and 5 job types in which both skills are used, e.g.

| Selected Skill |	Neighbor Skill |	Top Professions |
| --- | --- | --- |
| Mathematics (2.A.1.e) |	Active Listening (2.A.1.b)	| Allergists and Immunologists (4.5), Neuropsychologists (4.5), Preventive Medicine Physicians (4.38), School Psychologists (4.38), Urologists (4.38) |
| Mathematics (2.A.1.e)	| Critical Thinking (2.A.2.a)	| Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |
| Mathematics (2.A.1.e)	| Speaking (2.A.1.d) |	Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Allergists and Immunologists (4.5), Neuropsychologists (4.5), Preventive Medicine Physicians (4.38) |
| Mathematics (2.A.1.e)	| Monitoring (2.A.2.d) |	Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |
| Mathematics (2.A.1.e)	| Reading Comprehension (2.A.1.a)	| Allergists and Immunologists (4.5), Neuropsychologists (4.5), Preventive Medicine Physicians (4.38), Biochemists and Biophysicists (4.38), Health Informatics Specialists (4.38)
| Mathematics (2.A.1.e)	| Coordination (2.B.1.b)	| Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |
| Mathematics (2.A.1.e)	| Judgment and Decision Making (2.B.4.e)	| Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |
| Mathematics (2.A.1.e)	| Time Management (2.B.5.a)	| Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |
| Mathematics (2.A.1.e)	| Complex Problem Solving (2.B.2.i)	| Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |
| Mathematics (2.A.1.e)	| Social Perceptiveness (2.B.1.a)	| Mathematicians (5.0), Statisticians (4.88), Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary (4.75), Social Work Teachers, Postsecondary (4.62), Biostatisticians (4.62) |


## Set up

To set up the project, clone the repository. At a minimum You need the following packages installed:
- pandas
- openpyxl
- networkx
- matplotlib

A complete list of software used and their versions can be found in `requirements.txt`.

## How to run the code

To execute the tool, run:

`python skills.py`

The program will load the O*NET skills data and then prompt you to enter a skill. You can enter either a full skill code (for example `2.A.1.a`) or a partial skill/code search term. The script then prints the top related skills and example occupations directly to the console.

Behavior notes:
- If the input is blank, the program exits with an error message.
- If no skill matches the input, the program exits with an error message.
- If multiple partial matches are found, the program lists the matches and asks the user to be more specific.

The skill codes and titles can be found in `skills-list.csv`.

## Running tests

To run the unit tests for the project, use:

`python -m unittest test_skills.py`

If the tests pass, Python will report that 3 tests ran successfully and display `OK`.
## Contributing

If you would like to contribute, please fork the repository and make your changes in your own copy. For larger changes, create a feature branch and clearly describe what problem your change is solving. Please keep changes small, readable, and documented, and update any relevant documentation if your change affects setup or usage.

## Bug Reporting, Feature Requests, and Updates

This repository is a part of a project for CAS502 CAS Computation at ASU Spring 2026. We will not be providing additional updates to the repository beyond the end point of this project at the end of the course. If you find bugs or want to add new features or updates then please do so by creating a fork and making those changes within your own repository.

## Repository content

The following files are part of this repository:

- `skills.py`  
The code for this program.
- `skills-list.csv`  
CSV file with a list of skills and their codes.
- `data`  
This folder contains a number of data files. The files have been downloaded from [O*NET Resource Center](https://www.onetcenter.org/database.html), version 29.1 ([license](https://creativecommons.org/licenses/by/4.0/)). The file currently used in the code is `Skills.xlsx`. Additionally, there are two files in this folder:
  - `Occupation Data.xlsx`: Descriptions for each occupation.
  - `TechnologySkills.xlsx`: A list of technological skills for each occupation.
- `.gitignore`
- `Challenges.txt`
Potential challenges our project team would face in this project.
- `Communications_Plan.txt`
The communications plan for our project team.
- `LICENSE`
The license and usage allowability.
- `README.md`
This informational document about the program.
- `requirements.txt`
The list of all software and versions used to build this code.
