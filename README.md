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

After creating the network, the script will ask the user to input a skill and then create a .csv with the first 10 skills most often used with the entered skill and 5 job types in which both skills are used, e.g.

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

To execute the tool, simply run `python skills.py`. It will run for a few moments and then ask you to input a skill. You can find the codes and titles for each skill in the file `skills-list.csv` (e.g. `2.A.1.a` for "Reading Comprehension"). Once entered, the program will produce a file labeled `skill_results.csv` with a list of 10 skills are that are most often used in combination with the entered skill and the top five professions in which a skill is important for. If the skill input field is left blank, the program will prompt you to input a skill and close. If there is no skill matching the ones listed in `skills-list.csv`, the program will prompt you that no matching skill was found and close. If you entere a skill that partially matches multiple skills from the list (either a partial code match or partial name match), the program will list all of the partially matched values and ask you to input more specificity.

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
