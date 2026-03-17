"""Focused tests for the safe Nexus telemetry monitor."""

from nexus.anomaly_detector import (
    GPUReading,
    MLWeights,
    detect_anomalies,
    invoke_ml_predictive_repair,
)
from nexus.telemetry_monitor import (
    collect_gpu_telemetry,
    parse_gpu_csv,
    render_dashboard,
)


def test_predictive_detector_flags_threshold_crossing():
    weights = MLWeights(threshold=140.5, sensitivity=0.05)

    assert invoke_ml_predictive_repair(140.0, 20.0, weights=weights)
    assert not invoke_ml_predictive_repair(100.0, 20.0, weights=weights)


def test_detect_anomalies_includes_power_and_fan_reasons():
    readings = [
        GPUReading(
            index="0",
            power_draw=145.0,
            temperature=70.0,
            fan_speed=0,
            model="5090 Ti",
        )
    ]

    result = detect_anomalies(readings)[0]

    assert result.anomaly_predicted is True
    assert "predictive-threshold" in result.reasons
    assert "power-over-soft-limit" in result.reasons
    assert "fan-reported-zero" in result.reasons


def test_parse_gpu_csv_handles_missing_or_malformed_values():
    readings = parse_gpu_csv(
        [
            "0, 139.5, 55, 44, NVIDIA GeForce RTX 5090",
            "1, [N/A], Not Supported, [N/A], NVIDIA GeForce RTX 5090 Ti",
            "bad,line",
        ]
    )

    assert readings[0].power_draw == 139.5
    assert readings[0].temperature == 55.0
    assert readings[1].power_draw is None
    assert readings[1].temperature is None
    assert readings[2].index == "unknown"


def test_collect_gpu_telemetry_falls_back_cleanly_when_command_missing():
    def failing_runner(_command):
        raise FileNotFoundError("nvidia-smi missing")

    snapshot = collect_gpu_telemetry(command_runner=failing_runner)

    assert snapshot.gpus == []
    assert snapshot.telemetry_source == "unavailable"
    assert snapshot.warnings


def test_render_dashboard_marks_nominal_and_warning_states():
    def stub_runner(command):
        if command[:1] == ["nvidia-smi"]:
            return "0, 120, 50, 40, NVIDIA GeForce RTX 5090"
        return "eth0    UP"

    snapshot = collect_gpu_telemetry(command_runner=stub_runner)
    output = render_dashboard(snapshot)

    assert "ML-ENHANCED BOT" in output
    assert "UUC: STABLE" in output
    assert "eth0" in output
    assert "Bit-Level Topology v20" in output


def test_render_dashboard_marks_predicted_anomalies_as_lock():
    output = render_dashboard(
        collect_gpu_telemetry(
            command_runner=lambda command: (
                "0, 145, 70, 0, NVIDIA GeForce RTX 5090 Ti"
                if command[:1] == ["nvidia-smi"]
                else "eth0    UP"
            )
        )
    )

    assert "UUC: LOCK" in output
    assert "predictive-threshold" in output
