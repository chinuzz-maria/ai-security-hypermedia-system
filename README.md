# AI Security Hypermedia System

A knowledge graph system for AI Security 
education using OrientDB and graph algorithms.

## Features
- 14 AI Security topic nodes
- 13 weighted edges (3 edge types)
- BFS + DFS + Shortest Path + Bidirectional
- 42-question manual quiz
- Auto-generated quiz from OrientDB
- Graph visualization via OrientDB Studio
- True hypermedia: text + video + papers
- 14-option interactive menu

## Tech Stack
- Python 3.14
- OrientDB 3.2.49
- REST API port 2480
- Libraries: requests, collections, time

## How to Run
1. Start OrientDB: bin\server.bat
2. Run: python main.py
3. Choose from 14 menu options

## Graph Structure
Nodes: 14
- Attacks  : FGSM, PGD, Black-Box, IDSGAN, DDoS
- Defenses : Adversarial Training, 
             Preprocessing Defense,
             Defensive Distillation
- Tools    : GAN, DNN, SVM, MLP
- Datasets : NSL-KDD, CICIDS2017

Edges: 13 weighted
- mitigated_by  : 5 edges (0.75-0.95)
- uses          : 3 edges (0.78-0.92)
- benchmarked_on: 5 edges (0.76-0.88)

## Algorithms
- BFS           : O(V+E) = O(22)
- DFS           : O(V+E) = O(22)
- Shortest Path : BFS + path tracking
- Bidirectional : Both directions

## Research Papers
8 papers from IEEE, MDPI, ACM, Elsevier
All linked as hypermedia in OrientDB nodes
