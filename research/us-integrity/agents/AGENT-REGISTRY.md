# Specialist agent registry

Date: 2026-10-29. 24 sector specialists plus 8 cross-cutting reviewers. These are tool-independent role contracts, not deployed model processes. No specific ChatGPT model has been selected or attached by these files.

| Agent | Type | Contract |
|---|---|---|
| `agent-healthcare-dme` | sector specialist | [DME and medical supplies](agent-healthcare-dme.md) |
| `agent-healthcare-home-hospice` | sector specialist | [Home health and hospice](agent-healthcare-home-hospice.md) |
| `agent-healthcare-pharma-labs` | sector specialist | [Pharmaceuticals, PBMs and laboratories](agent-healthcare-pharma-labs.md) |
| `agent-healthcare-managed-care` | sector specialist | [Medicare Advantage and Medicaid managed care](agent-healthcare-managed-care.md) |
| `agent-veterans-health-benefits` | sector specialist | [Veterans healthcare and benefits](agent-veterans-health-benefits.md) |
| `agent-defense-parts` | sector specialist | [Defence parts, aerospace and manufacturing](agent-defense-parts.md) |
| `agent-defense-logistics-services` | sector specialist | [Defence logistics, overseas support and services](agent-defense-logistics-services.md) |
| `agent-construction-infrastructure` | sector specialist | [Construction, transport and infrastructure](agent-construction-infrastructure.md) |
| `agent-it-cyber-services` | sector specialist | [IT, cyber, cloud and professional services](agent-it-cyber-services.md) |
| `agent-small-business-setasides` | sector specialist | [Small business, set-asides and procurement eligibility](agent-small-business-setasides.md) |
| `agent-pandemic-relief` | sector specialist | [PPP, EIDL and pandemic business relief](agent-pandemic-relief.md) |
| `agent-unemployment-labour` | sector specialist | [Unemployment insurance and labour programmes](agent-unemployment-labour.md) |
| `agent-research-education-grants` | sector specialist | [Research, education and grant programmes](agent-research-education-grants.md) |
| `agent-housing-disaster` | sector specialist | [Housing, FEMA and disaster recovery](agent-housing-disaster.md) |
| `agent-agriculture-nutrition` | sector specialist | [Agriculture, SNAP, meals and childcare-related grants](agent-agriculture-nutrition.md) |
| `agent-energy-environment` | sector specialist | [Energy, environment and clean-technology funding](agent-energy-environment.md) |
| `agent-tax-customs-trade` | sector specialist | [Tax, customs, tariffs and international trade](agent-tax-customs-trade.md) |
| `agent-finance-digital-assets` | sector specialist | [Financial misconduct and digital assets touching federal funds](agent-finance-digital-assets.md) |
| `agent-defense-systems` | sector specialist | [Defence weapons, aircraft and major systems](agent-defense-systems.md) |
| `agent-foreign-aid` | sector specialist | [Foreign assistance and overseas procurement](agent-foreign-aid.md) |
| `agent-childcare-social` | sector specialist | [Childcare, TANF and social services](agent-childcare-social.md) |
| `agent-pensions-benefits` | sector specialist | [Social Security, federal pensions and personnel](agent-pensions-benefits.md) |
| `agent-justice-detention` | sector specialist | [Justice, detention, corrections and homeland services](agent-justice-detention.md) |
| `agent-tribal-local` | sector specialist | [Tribal, state and local pass-through funding](agent-tribal-local.md) |
| `agent-coordinator` | cross cutting | [Research coordinator](agent-coordinator.md) |
| `agent-entity-resolution` | cross cutting | [Entity and ownership resolver](agent-entity-resolution.md) |
| `agent-provenance-curator` | cross cutting | [Provenance and source curator](agent-provenance-curator.md) |
| `agent-falsification-reviewer` | cross cutting | [Independent falsification reviewer](agent-falsification-reviewer.md) |
| `agent-financial-methods` | cross cutting | [Financial and statistical methods reviewer](agent-financial-methods.md) |
| `agent-legal-route-reviewer` | cross cutting | [Reward-route and procedural-status researcher](agent-legal-route-reviewer.md) |
| `agent-privacy-publication` | cross cutting | [Privacy and publication reviewer](agent-privacy-publication.md) |
| `agent-quality-evaluator` | cross cutting | [Research quality and regression evaluator](agent-quality-evaluator.md) |

The machine-readable registry is [agents.json](agents.json). A runner must preserve each contract's read-only capabilities, source tiers, output schema, resource quota and escalation rules. Shared supervisor and independent reviewers apply to every sector; sector specialists cannot self-approve novel named allegations.

Start by selecting one bounded task from [tasks.json](../architecture/tasks.json), read [SYSTEM-DESIGN.md](../architecture/SYSTEM-DESIGN.md), then use [RESEARCH-RESULT-TEMPLATE.md](RESEARCH-RESULT-TEMPLATE.md). The [second-model handoff](SECOND-MODEL-HANDOFF.md) supports a separate session without pretending an inter-chat connection exists.

## Coverage map

All 27 catalogue scopes map to a responsible specialist in [coverage-map.json](coverage-map.json). Some specialists cover closely related scopes, such as housing/disaster or tax/customs, while the mapping preserves each scope separately. This assignment map is not evidence that an agent has executed a sector audit.

| Sector scope | Responsible specialist |
|---|---|
| Defence weapons, aircraft and major systems | `agent-defense-systems` |
| Military spares, commodities and medical procurement | `agent-defense-parts` |
| Medicare durable medical equipment and medical supplies | `agent-healthcare-dme` |
| Home health, hospice, nursing and inpatient care | `agent-healthcare-home-hospice` |
| Pharmaceuticals, PBMs, labs and telehealth | `agent-healthcare-pharma-labs` |
| Medicaid, autism and special services | `agent-healthcare-managed-care` |
| Veterans healthcare, benefits and VA purchasing | `agent-veterans-health-benefits` |
| Infrastructure, transport and public works | `agent-construction-infrastructure` |
| IT, cybersecurity, consulting and staffing | `agent-it-cyber-services` |
| Small-business set-asides and certification | `agent-small-business-setasides` |
| Military and civilian logistics, fuel and transport | `agent-defense-logistics-services` |
| Foreign assistance and overseas procurement | `agent-foreign-aid` |
| Research grants and university/nonprofit funding | `agent-research-education-grants` |
| Education, student aid and training programmes | `agent-research-education-grants` |
| PPP, EIDL and business relief | `agent-pandemic-relief` |
| Unemployment insurance and labour benefits | `agent-unemployment-labour` |
| FEMA, disaster recovery and emergency programmes | `agent-housing-disaster` |
| Housing, rental assistance and development | `agent-housing-disaster` |
| Agriculture, SNAP, nutrition and farm support | `agent-agriculture-nutrition` |
| Childcare, TANF and social services | `agent-childcare-social` |
| Energy grants, environmental projects and credits | `agent-energy-environment` |
| Tax administration and tax-credit claims | `agent-tax-customs-trade` |
| Customs, tariffs, imports and trade remedies | `agent-tax-customs-trade` |
| Financial programmes, securities and commodities | `agent-finance-digital-assets` |
| Social Security, federal pensions and personnel | `agent-pensions-benefits` |
| Justice, detention, corrections and homeland services | `agent-justice-detention` |
| Tribal, state and local pass-through funding | `agent-tribal-local` |
