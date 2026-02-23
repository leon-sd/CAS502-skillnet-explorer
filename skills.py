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

# Prompt user for skill input
selected_skill = input("Enter a skill: ").strip()

# Prompt user if input is empty
if not selected_skill:
    raise SystemExit('No skill entered. Example: 2.B.3.e or Programming')

# Find partial matches in Element ID
matches = [node for node in skills_graph.nodes if selected_skill.lower() in node.lower()]

# Find partial matches in Element Name
if not matches:
    matches = [
        node for node, data in skills_graph.nodes(data=True)
        if selected_skill.lower() in data["label"].lower()
    ]

if not matches:
    raise SystemExit(f"No skills found matching: {selected_skill}")
# If input partially matches multiple skills, list them for user and prompt re-entry
if len(matches) > 1:
    print("Multiple matches found:")
    for m in matches:
        print(f" - {m}: {skills_graph.nodes[m]['label']}")
    raise SystemExit("Please enter a more specific search term.")

# Exactly one match → use it
selected_skill = matches[0]
print(f"Using skill: {selected_skill} ({skills_graph.nodes[selected_skill]['label']})")

edges = sorted(
    skills_graph.edges(selected_skill, data=True),
    key=lambda edge: edge[2].get("weight", 1),
    reverse=True,
)

# Build CSV rows 
rows = []
selected_label = skills_graph.nodes[selected_skill]["label"]
occupations_selected = skills_graph.nodes[selected_skill]["occupations"]

# Identify number of related skills to display in search
for _, neighbor_id, _ in edges[:10]:
    neighbor_label = skills_graph.nodes[neighbor_id]["label"]
    occupations = skills_graph.nodes[neighbor_id]["occupations"]

    intersection = list(set(occupations_selected) & set(occupations))

    # Deduplicate by occupation title, keeping the highest Data Value
    best_by_title = {}
    for title, value in intersection:
        if (title not in best_by_title) or (value > best_by_title[title]):
            best_by_title[title] = value

    deduped = sorted(best_by_title.items(), key=lambda tv: tv[1], reverse=True)

    # Move search results to CSV shape
    rows.append({
        "Selected Skill": f"{selected_label} ({selected_skill})",
        "Neighbor Skill": f"{neighbor_label} ({neighbor_id})",
        "Top Professions": ", ".join([f"{title} ({value})" for title, value in deduped[:5]]) 
    }) 

# Save as CSV output
df_out = pd.DataFrame(rows)
df_out.to_csv("skill_results.csv", index=False)

print("Results saved to skill_results.csv!")
