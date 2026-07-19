# n8n Atlas Pipeline

The verified local `DAMAVAND_STEEL_N8N_ATLAS_PIPELINE_v1.0` assets are stored in `n8n/` as inactive workflow definitions, versioned configuration, environment placeholders, and documentation.

- [Architecture](ARCHITECTURE.md)
- [Persian installation guide](INSTALLATION_GUIDE_FA.md)
- [Next-version plan](NEXT_VERSION_PLAN.md)

n8n is the Orchestrator only. Repository documents and approved data remain authoritative. Importing workflow JSON does not authorize activation or execution.

The workflows contain OpenAI and GitHub operations plus non-secret configuration placeholders. Static validation confirms that the GitHub `PUT` is immediately protected by the strict LIVE write gate and that DRY_RUN reaches a terminal `dry_run_blocked_write` result. Required context reads now fail closed, structured output must satisfy the canonical schema, and Markdown is rendered only after validation. These controls have not been runtime-tested in n8n; keep every workflow inactive until credentials, least privilege, repository identity, isolated DRY_RUN evidence, failure handling, backup/rollback implications, and separate Founder approvals are confirmed.
