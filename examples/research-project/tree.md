# Research or Data Project

A project that works with datasets, experiments, notebooks, and reproducible analysis has different information needs from a web application. It must make data provenance, transformation steps, environment, and generated results understandable.

This example uses a Python-style analysis project. Replace the tooling and folder names with the conventions of the actual research environment.

## Example tree

```text
research-project/
├── AGENTS.md                         # Research, data-handling, and reproducibility boundaries
├── README.md                         # Research question, data sources, and reproduction steps
├── pyproject.toml                    # Dependencies and analysis tooling
├── src/
│   └── research_project/
│       ├── ingest.py                 # Reproducible input acquisition
│       ├── clean.py                  # Reusable cleaning and transformation logic
│       ├── analysis.py               # Reusable analytical methods
│       └── visualize.py              # Figure generation
├── tests/
│   ├── test_clean.py                 # Transformation invariants
│   └── test_analysis.py              # Known-answer and edge-case checks
├── notebooks/
│   ├── 01_exploration.ipynb          # Exploratory work, not the only copy of reusable logic
│   └── 02_results.ipynb              # Narrative analysis and interpretation
├── data/
│   ├── README.md                     # Provenance, access, licenses, and storage policy
│   ├── raw/                          # Original inputs; usually external or ignored
│   ├── interim/                      # Intermediate transformations, usually reproducible
│   └── processed/                    # Curated analysis-ready data, with clear provenance
├── experiments/
│   ├── configs/                      # Parameters and experiment definitions
│   └── results/                      # Compact, reproducible result metadata
├── reports/
│   ├── figures/                      # Generated figures intended for reports
│   └── final-report.md               # Published interpretation and conclusions
└── docs/
    ├── methodology.md                # Study design, assumptions, and limitations
    └── decisions/                    # Important methodological or analytical choices
```

## Notes

- **`README.md`** states the research question, how to obtain permitted inputs, how to run the analysis, and where the results are reported.
- **`AGENTS.md`** should state data access limits, privacy restrictions, reproducibility expectations, and the exact environment or commands that work.
- **`src/`** holds reusable code for ingestion, cleaning, analysis, and visualization. If a notebook contains logic that is reused or must be tested, move that logic into importable modules.
- **`notebooks/`** is for exploration and narrative analysis. Notebooks are useful artifacts, but they should not be the only record of an important production pipeline or reusable algorithm.
- **`data/README.md`** records source, license, access method, schema, and transformation provenance. Do not commit sensitive, licensed, or large raw data just to make the tree look self-contained.
- **`raw/`, `interim/`, and `processed/`** are common data stages, not a mandatory taxonomy. Use only stages that reflect real transformations. Large data may live in object storage or a data-versioning system.
- **`experiments/`** is useful when parameters, seeds, model versions, and results need to be compared. A handful of exploratory runs may stay in notebooks.
- **`reports/`** holds outputs intended for readers. Temporary plots and caches should remain generated and reproducible rather than becoming competing source files.
- **`docs/methodology.md`** explains study design and assumptions that cannot be inferred from code. Record important methodological decisions when later work could otherwise reverse them unknowingly.

## Reproducibility is the organizing principle

A reader or agent should be able to identify the input data, the transformations, the environment, the experiment parameters, and the final interpretation. The project does not need a special folder for each concept if its current workflow is simpler.

## Related patterns

- [Growing project](../growing-project/tree.md) for durable decisions.
- [Repeatable workflows](../repeatable-workflows/tree.md) for reproducible analysis or release procedures.
- [Organization scale](../organization-scale/tree.md) when many datasets, pipelines, or teams need central ownership.
