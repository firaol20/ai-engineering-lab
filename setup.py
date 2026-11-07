
from pathlib import Path
import json

ROOT = Path(__file__).parent

QUARTERS = [
    ("quarter-1-foundations", "Software Engineering for AI", 1, 13),
    ("quarter-2-rag", "Data Engineering, RAG and Retrieval", 14, 26),
    ("quarter-3-agents", "AI Agents and Workflow Automation", 27, 39),
    ("quarter-4-production", "Production AI Engineering", 40, 52),
]

WEEKS = [
    (1, "CLI AI Assistant", "Build a terminal assistant with conversation history."),
    (2, "Prompt Testing Playground", "Compare prompt versions using the same test inputs."),
    (3, "LLM REST API", "Expose an LLM through a validated FastAPI service."),
    (4, "AI Service Containerization", "Package an AI API using Docker."),
    (5, "API Authentication and Usage Limits", "Implement API keys, quotas and rate limiting."),
    (6, "Background AI Job Processor", "Process slow AI tasks asynchronously."),
    (7, "LLM Cost Calculator", "Track tokens and estimate AI application costs."),
    (8, "Structured Information Extractor", "Convert unstructured text into validated JSON."),
    (9, "Multi-Provider LLM Gateway", "Route requests across multiple AI providers."),
    (10, "AI Response Caching Experiment", "Compare exact-match and semantic caching."),
    (11, "Prompt Versioning System", "Track prompt changes and compare versions."),
    (12, "AI Evaluation Benchmark", "Build a repeatable AI evaluation framework."),
    (13, "AI Application CI Pipeline", "Automate testing with GitHub Actions."),

    (14, "PDF Intelligence Engine", "Ingest and search information in PDF documents."),
    (15, "Vector Database Shootout", "Benchmark different vector databases."),
    (16, "Smart Document Chunking", "Compare document chunking strategies."),
    (17, "Hybrid Search Engine", "Combine keyword and vector search."),
    (18, "Reranking Experiment", "Improve retrieval relevance using reranking."),
    (19, "Citation-Based RAG", "Generate answers with verifiable citations."),
    (20, "Multi-Document Knowledge Assistant", "Answer questions across multiple documents."),
    (21, "RAG Evaluation Lab", "Measure retrieval and answer quality."),
    (22, "Incremental Document Ingestion", "Update document indexes efficiently."),
    (23, "Tables and Images in Documents", "Extract information from tables and scanned pages."),
    (24, "Natural Language to SQL", "Convert questions into safe read-only SQL."),
    (25, "Codebase Q&A Assistant", "Answer developer questions using source code."),
    (26, "Conversational RAG Memory", "Retrieve useful context across conversations."),

    (27, "Function Calling Assistant", "Let an LLM call controlled application functions."),
    (28, "ReAct Agent Experiment", "Compare direct answers with tool-using agents."),
    (29, "LangGraph Workflow", "Build stateful multi-step AI workflows."),
    (30, "Research and Report Agent", "Research topics and produce cited reports."),
    (31, "Agent Guardrails", "Restrict agent tools and validate inputs."),
    (32, "Agent Evaluation Benchmark", "Measure agent task completion."),
    (33, "Human Approval Workflow", "Require human approval before consequential actions."),
    (34, "Multi-Agent Collaboration Experiment", "Compare single-agent and multi-agent systems."),
    (35, "Agentic RAG", "Build agents that retrieve additional evidence."),
    (36, "Browser Automation Assistant", "Automate controlled browser tasks."),
    (37, "Long-Term Agent Memory", "Store and retrieve information across tasks."),
    (38, "Workflow vs Agent Benchmark", "Compare deterministic workflows with agents."),
    (39, "Agent Observability Dashboard", "Monitor agent execution and failures."),

    (40, "Full-Stack AI Application", "Build a complete AI-powered application."),
    (41, "Multi-Tenant AI SaaS", "Serve multiple organizations securely."),
    (42, "Fine-Tuning vs Prompting", "Compare fine-tuning and prompt engineering."),
    (43, "Local LLM Deployment", "Run an AI model locally."),
    (44, "Model Routing and Fallbacks", "Route requests based on cost and quality."),
    (45, "AI Safety and Security Layer", "Implement layered AI safety checks."),
    (46, "AI Load Testing", "Measure AI service performance under load."),
    (47, "Prompt Injection Security Lab", "Test and defend against prompt injection."),
    (48, "Capstone Problem Discovery and Architecture", "Identify a real problem and design its solution."),
    (49, "Capstone Core Backend and AI", "Build the capstone backend and AI workflows."),
    (50, "Capstone Frontend and Integration", "Build and integrate the user interface."),
    (51, "Capstone Deployment and Evaluation", "Deploy and evaluate the capstone."),
    (52, "Portfolio and Open Source Week", "Polish projects and contribute to open source."),
]


def slugify(title):
    return "".join(
        c.lower() if c.isalnum() else "-"
        for c in title
    ).strip("-").replace("--", "-")


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def create_root():
    write_file(ROOT / "README.md", """
# AI Engineering Lab

A 52-week experiment-driven AI Engineering portfolio.

## Roadmap

| Quarter | Focus | Weeks |
|---|---|---|
| Q1 | Software Engineering for AI | 01–13 |
| Q2 | RAG and Retrieval | 14–26 |
| Q3 | AI Agents | 27–39 |
| Q4 | Production AI Engineering | 40–52 |

## Weekly workflow

1. Understand the problem.
2. Write a hypothesis.
3. Build a working experiment.
4. Compare approaches.
5. Run tests and collect measurements.
6. Document failures and conclusions.

## Quality standards

- Clear problem statement.
- Reproducible setup instructions.
- Working implementation.
- Tests and evaluation.
- Measured results.
- Documented limitations.

Never commit API keys, passwords, or private data.
""")

    write_file(ROOT / ".gitignore", """
__pycache__/
*.py[cod]
.venv/
venv/
.env
.env.*
!.env.example
.pytest_cache/
.vscode/
.idea/
dist/
build/
data/private/
datasets/private/
artifacts/
outputs/
*.sqlite3
*.db
""")

    write_file(ROOT / "docs" / "experiment-template.md", """
# Experiment title

**Status:** Not started

## Problem
What real problem are you solving?

## Intended users
Who needs this solution?

## Hypothesis
What do you expect to happen?

## Approaches
What alternatives will you compare?

## Architecture
Explain the system components.

## Implementation
Describe what you built.

## Evaluation
What metrics will you measure?

| Metric | Method | Result |
|---|---|---|
| Accuracy | | |
| Latency | | |
| Cost | | |
| Reliability | | |

## Failure cases
What did not work?

## Conclusion
What did you learn?

## Next steps
- [ ]
""")

    write_file(ROOT / "docs" / "evaluation-template.md", """
# Evaluation Report

- Experiment:
- Date:
- Model/provider:
- Dataset:
- Hardware:

## Method
Explain how the experiment was evaluated.

## Results

| Approach | Quality | Latency | Cost |
|---|---|---|---|
| Baseline | | | |
| Alternative | | | |

## Failure analysis

## Conclusion

## Reproduction instructions
""")


def create_quarters():
    for folder, title, start, end in QUARTERS:
        selected = [w for w in WEEKS if start <= w[0] <= end]

        lines = [
            f"# {title}",
            "",
            f"**Weeks {start:02d}–{end:02d}**",
            "",
            "## Experiments",
            "",
        ]

        for number, name, problem in selected:
            slug = slugify(name)
            lines.append(
                f"- [ ] [Week {number:02d}: {name}]"
                f"(week-{number:02d}-{slug}/README.md)"
            )

        write_file(ROOT / folder / "README.md", "\n".join(lines))

        for number, name, problem in selected:
            slug = slugify(name)
            path = ROOT / folder / f"week-{number:02d}-{slug}" / "README.md"

            content = f"""
# Week {number:02d} — {name}

**Status:** Not started

## Problem

{problem}

## Intended user

Who would benefit from this solution?

## Hypothesis

What do you expect to happen?

## Learning objectives

- Understand the underlying concepts.
- Build a working experiment.
- Compare different approaches.
- Measure performance and quality.
- Document failures.

## Implementation plan

1. Research the problem.
2. Define the baseline.
3. Implement the experiment.
4. Write tests.
5. Collect results.
6. Document conclusions.

## Evaluation

| Metric | Method | Result |
|---|---|---|
| Quality | | |
| Latency | | |
| Cost | | |

## Results

_To be completed after implementation._

## Failure cases

_To be documented._

## Conclusion

_What did you learn?_

## Next steps

- [ ]
"""
            write_file(path, content)


def main():
    create_root()
    create_quarters()

    manifest = {
        "name": "AI Engineering Lab",
        "total_weeks": len(WEEKS),
        "weeks": [
            {
                "week": n,
                "title": title,
                "problem": problem,
            }
            for n, title, problem in WEEKS
        ],
    }

    write_file(
        ROOT / "roadmap.json",
        json.dumps(manifest, indent=2)
    )

    print("AI Engineering Lab created successfully!")
    print(f"Experiments: {len(WEEKS)}")
    print(f"Location: {ROOT}")


if __name__ == "__main__":
    main()
