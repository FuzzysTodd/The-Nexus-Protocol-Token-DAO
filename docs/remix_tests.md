# Solidity API

## Assert

### Contract
Assert : .deps/remix-tests/remix_tests.sol

 --- 
### Functions:
### ok

```solidity
function ok(bool a, string message) public returns (bool result)
```

### equal

```solidity
function equal(uint256 a, uint256 b, string message) public returns (bool result)
```

### equal

```solidity
function equal(int256 a, int256 b, string message) public returns (bool result)
```

### equal

```solidity
function equal(bool a, bool b, string message) public returns (bool result)
```

### equal

```solidity
function equal(address a, address b, string message) public returns (bool result)
```

### equal

```solidity
function equal(bytes32 a, bytes32 b, string message) public returns (bool result)
```

### equal

```solidity
function equal(string a, string b, string message) public returns (bool result)
```

### notEqual

```solidity
function notEqual(uint256 a, uint256 b, string message) public returns (bool result)
```

### notEqual

```solidity
function notEqual(int256 a, int256 b, string message) public returns (bool result)
```

### notEqual

```solidity
function notEqual(bool a, bool b, string message) public returns (bool result)
```

### notEqual

```solidity
function notEqual(address a, address b, string message) public returns (bool result)
```

### notEqual

```solidity
function notEqual(bytes32 a, bytes32 b, string message) public returns (bool result)
```

### notEqual

```solidity
function notEqual(string a, string b, string message) public returns (bool result)
```

### greaterThan

```solidity
function greaterThan(uint256 a, uint256 b, string message) public returns (bool result)
```

### greaterThan

```solidity
function greaterThan(int256 a, int256 b, string message) public returns (bool result)
```

### greaterThan

```solidity
function greaterThan(uint256 a, int256 b, string message) public returns (bool result)
```

### greaterThan

```solidity
function greaterThan(int256 a, uint256 b, string message) public returns (bool result)
```

### lesserThan

```solidity
function lesserThan(uint256 a, uint256 b, string message) public returns (bool result)
```

### lesserThan

```solidity
function lesserThan(int256 a, int256 b, string message) public returns (bool result)
```

### lesserThan

```solidity
function lesserThan(uint256 a, int256 b, string message) public returns (bool result)
```

### lesserThan

```solidity
function lesserThan(int256 a, uint256 b, string message) public returns (bool result)
```

 --- 
### Events:
### AssertionEvent

```solidity
event AssertionEvent(bool passed, string message, string methodName)
```

### AssertionEventUint

```solidity
event AssertionEventUint(bool passed, string message, string methodName, uint256 returned, uint256 expected)
```

### AssertionEventInt

```solidity
event AssertionEventInt(bool passed, string message, string methodName, int256 returned, int256 expected)
```

### AssertionEventBool

```solidity
event AssertionEventBool(bool passed, string message, string methodName, bool returned, bool expected)
```

### AssertionEventAddress

```solidity
event AssertionEventAddress(bool passed, string message, string methodName, address returned, address expected)
```

### AssertionEventBytes32

```solidity
event AssertionEventBytes32(bool passed, string message, string methodName, bytes32 returned, bytes32 expected)
```

### AssertionEventString

```solidity
event AssertionEventString(bool passed, string message, string methodName, string returned, string expected)
```

### AssertionEventUintInt

```solidity
event AssertionEventUintInt(bool passed, string message, string methodName, uint256 returned, int256 expected)
```

### AssertionEventIntUint

```solidity
event AssertionEventIntUint(bool passed, string message, string methodName, int256 returned, uint256 expected)
```

