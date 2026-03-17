"""Safe, read-only Nexus telemetry monitor utilities."""

from .anomaly_detector import (
    DetectionResult,
    GPUReading,
    MLWeights,
    TelemetrySnapshot,
    detect_anomalies,
    invoke_ml_predictive_repair,
)

__all__ = [
    "DetectionResult",
    "GPUReading",
    "MLWeights",
    "TelemetrySnapshot",
    "detect_anomalies",
    "invoke_ml_predictive_repair",
    "BranchSummary",
    "RepoAssessmentSummary",
    "collect_repo_assessment",
    "render_repo_assessment",
]


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
