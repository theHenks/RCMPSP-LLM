# RCMPSP-LLM
This repository contains the code for my master thesis in the Master in Management Program at the Technical University of Munich with the topic
**LLM-Based Multi-Project Scheduling** in the group of Prof. Kolisch under supervision of Robert Brachmann and Franziska Strobel.

## Thesis topic
This thesis addresses solving the resource-constrained multi-project scheduling problem (RCMPSP) with a Large Language Model (LLM)-based approach. The latter incorporates a multi-agent system, where different agents are responsible for making specific types of decisions such as determining eligible activities, selecting the next activity to be scheduled, and scheduling a selected activity. Each agent utilizes the same LLM to make its decisions, with a system prompt that defines properties such as the agent's role and the context of the problem or decision, along with decision-specific information included in the prompt.
The scope of this thesis is to provide a literature review on the RCMPSP, solution approaches, and multi-agent based LLM scheduling. Afterwards, the thesis involves programming an LLM-based multiagent approach for the RCMPSP and conducting a computational study to compare the LLM-based approach with existing heuristics on existing benchmark instances.
## Thesis outline
- Literature review on the RCMPSP and its solution approaches and on multi-agent LLM-based scheduling.
- Programming a multi-agent LLM-based approach for the RCMPSP.
- Conduct a computational study, where the multi-agent LLM-based approach is compared to existing heuristics on a set of existing benchmark instances.

## Contents of this repository
- All related code for the conducted study including `README.md` based documentations is based under `code/`
- All thesis related documentes including LATEX files can be found under `latex/`



