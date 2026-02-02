import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def add_occupation(skills_graph, node_id, row):
    if (row['Title'], row['Data Value']) not in skills_graph.nodes[node_id]['occupations']:
        skills_graph.nodes[node_id]['occupations'].append((row['Title'], row['Data Value']))

def add_neighbor(skills_graph, group, neighbor_idx, current_node, row):
    neighbor_node = group.iloc[neighbor_idx]['Element ID']
    # we dont' want loops to self
    if current_node == neighbor_node:
        return

    if not skills_graph.has_node(neighbor_node):
        skills_graph.add_node(neighbor_node, label=group.iloc[neighbor_idx]['Element Name'], occupations=[])
        
    add_occupation(skills_graph, neighbor_node, row)

    if not skills_graph.has_edge(current_node, neighbor_node):
        skills_graph.add_edge(current_node, neighbor_node)
        skills_graph[current_node][neighbor_node]["weight"] = 0

    skills_graph[current_node][neighbor_node]["weight"] = skills_graph[current_node][neighbor_node]["weight"] + 1

def build_skills_graph(path_to_skills):
    df = pd.read_excel(path_to_skills)

    # only use skills with importance greater than 2.5
    filtered_df = df.loc[(df["Scale ID"] == "IM") & (df["Data Value"] > 2.5)].copy()
    filtered_df = filtered_df.reset_index(drop=True)

        # group data by O*NET-SOC Code so we can then iterate over each skill in each occupation
    grouped_df = filtered_df.groupby("O*NET-SOC Code")

    skills_graph = nx.Graph()

    for _, group in grouped_df:
        # one group represents one occupation
        for i, (_, row) in enumerate(group.iterrows()):
            current_node = row["Element ID"]

            if not skills_graph.has_node(current_node):
                skills_graph.add_node(current_node, label=row["Element Name"], occupations=[])

            add_occupation(skills_graph, current_node, row)

            # connect this skill to later skills in the same occupation (positional)
            for neighbor_idx in range(i + 1, len(group)):
                add_neighbor(skills_graph, group, neighbor_idx, current_node, row)

    return skills_graph



skills_graph = build_skills_graph("data/Skills.xlsx")

selected_skill = input("Enter the code of a skill: ").strip()

if not selected_skill:
    raise SystemExit('No skill code entered. Example: 2.B.3.e')

if selected_skill not in skills_graph:
    raise SystemExit(f"Skill code not found: {selected_skill}")

edges = sorted(
    skills_graph.edges(selected_skill, data=True),
    key=lambda edge: edge[2].get("weight", 1),
    reverse=True,
)

selected_label = skills_graph.nodes[selected_skill]["label"]
print(f'\nOften used skills with "{selected_label} ({selected_skill})":')

occupations_selected = skills_graph.nodes[selected_skill]["occupations"]
for _, neighbor_id, _ in edges[:10]:
    neighbor_label = skills_graph.nodes[neighbor_id]["label"]
    occupations = skills_graph.nodes[neighbor_id]["occupations"]

    intersection = sorted(
        list(set(occupations_selected) & set(occupations)),
        reverse=True,
        key=lambda prof: prof[1],
    )

    examples = ", ".join([f"{occup[0]} ({occup[1]})" for occup in intersection[:5]])
    print(f'"{neighbor_label} ({neighbor_id})" e.g. as {examples}')
    print()

