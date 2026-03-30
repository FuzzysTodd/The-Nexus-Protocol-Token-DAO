"""Safe, read-only Nexus telemetry monitor utilities."""

from .anomaly_detector import (
    DetectionResult,
    GPUReading,
    MLWeights,
    TelemetrySnapshot,
    detect_anomalies,
    invoke_ml_predictive_repair,
)
from .monsterball import (
    MONSTERBALL_WEIGHTS,
    MatchSnapshot,
    PlayerStats,
    PredictionResult,
    PredictorWeights,
    predict,
    predict_player,
    rank_players,
    render_match_report,
)
from .super_logical import (
    LOGICAL_CAPACITY,
    MONSTERBALL_SUPER_WEIGHTS,
    TOKEN_SUPER_WEIGHTS,
    UNIVERSAL_SUPER_WEIGHTS,
    LogicalReading,
    SuperLogicalResult,
    SuperLogicalWeights,
    compose_super_predict,
    render_super_logical_report,
    super_predict,
)
from .algebra3 import (
    ALGEBRA3_VERSION,
    BEHAVIOR_PROFILES,
    MONSTERBALL_A3_WEIGHTS,
    HUMAN_RESPONSE_A3_WEIGHTS,
    TOKEN_A3_WEIGHTS,
    UNIVERSAL_A3_WEIGHTS,
    Algebra3Result,
    Algebra3Weights,
    BehaviorProfile,
    apply_algebra3,
    match_behavior,
    render_algebra3_report,
)
from .nexus_token_supremacy import (
    NGTT_STATS,
    SupremacyVerdict,
    analyze_ngtt_supremacy,
    render_supremacy_report,
)
from .signal_repair import (
    EXCHANGE_SIGNAL_RANGES,
    PARTICLE_COUNT,
    DegradedSignal,
    SignalRepairResult,
    generate_particles,
    repair_signal,
    render_repair_report,
)
from .atmosphere import (
    IDEAL_SNAPSHOT,
    PARTICLE_CATALOGUE,
    AtmosphericReading,
    ParticleFluxReading,
    PlanetaryHealthResult,
    PlanetarySnapshot,
    SolarReading,
    analyze_planetary_health,
    render_planetary_report,
)
from .family_renaissance import (
    GENERATION_GEN_X,
    GENERATION_GEN_Z,
    HEALTHY_FAMILY_BASELINE,
    SOCIETAL_STRESSORS,
    FamilyProfile,
    FamilyRenaissanceResult,
    RepairAction,
    analyze_both_generations,
    analyze_family_crisis,
    render_renaissance_report,
)

__all__ = [
    # anomaly_detector
    "DetectionResult",
    "GPUReading",
    "MLWeights",
    "TelemetrySnapshot",
    "detect_anomalies",
    "invoke_ml_predictive_repair",



def __getattr__(name):
    if name in {
        "BranchSummary",
        "RepoAssessmentSummary",
        "collect_repo_assessment",
        "render_repo_assessment",
    }:
        from .repo_assessment import (
            BranchSummary,
            RepoAssessmentSummary,
            collect_repo_assessment,
            render_repo_assessment,
        )

        exports = {
            "BranchSummary": BranchSummary,
            "RepoAssessmentSummary": RepoAssessmentSummary,
            "collect_repo_assessment": collect_repo_assessment,
            "render_repo_assessment": render_repo_assessment,
        }
        return exports[name]
    raise AttributeError(f"module 'nexus' has no attribute {name!r}")
