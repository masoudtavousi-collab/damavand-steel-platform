# n8n Atlas Pipeline

The verified local `DAMAVAND_STEEL_N8N_ATLAS_PIPELINE_v1.0` assets are stored in `n8n/` as inactive workflow definitions, versioned configuration, environment placeholders, and documentation.

- [Architecture](ARCHITECTURE.md)
- [Persian installation guide](INSTALLATION_GUIDE_FA.md)
- [Next-version plan](NEXT_VERSION_PLAN.md)

n8n is the Orchestrator only. Repository documents and approved data remain authoritative. Importing workflow JSON does not authorize activation or execution.

The workflows contain OpenAI and GitHub operations, configuration placeholders, and a `dry_run` value that is not currently enforced before the GitHub PUT node. Keep every workflow inactive until a separately approved review confirms credentials, least privilege, dry-run enforcement, external-write gates, human approval, failure handling, backup/rollback implications, and an isolated test target.
