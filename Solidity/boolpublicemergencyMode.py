modifier notEmergency() {
    require(!emergencyMode, "DAO in emergency mode");
    _;
}
