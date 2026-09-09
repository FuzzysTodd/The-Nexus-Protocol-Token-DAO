# Solidity API

## IERC721A

_Interface of ERC721A._

### Contract
IERC721A : Azuki-ERC721A-ERC721ABurnable/IERC721A.sol

Interface of ERC721A.

 --- 
### Functions:
### totalSupply

```solidity
function totalSupply() external view returns (uint256)
```

_Returns the total number of tokens in existence.
Burned tokens will reduce the count.
To get the total number of tokens minted, please see {_totalMinted}._

### supportsInterface

```solidity
function supportsInterface(bytes4 interfaceId) external view returns (bool)
```

_Returns true if this contract implements the interface defined by
`interfaceId`. See the corresponding
[EIP section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified)
to learn more about how these ids are created.

This function call must use less than 30000 gas._

### balanceOf

```solidity
function balanceOf(address owner) external view returns (uint256 balance)
```

_Returns the number of tokens in `owner`'s account._

### ownerOf

```solidity
function ownerOf(uint256 tokenId) external view returns (address owner)
```

_Returns the owner of the `tokenId` token.

Requirements:

- `tokenId` must exist._

### safeTransferFrom

```solidity
function safeTransferFrom(address from, address to, uint256 tokenId, bytes data) external payable
```

_Safely transfers `tokenId` token from `from` to `to`,
checking first that contract recipients are aware of the ERC721 protocol
to prevent tokens from being forever locked.

Requirements:

- `from` cannot be the zero address.
- `to` cannot be the zero address.
- `tokenId` token must exist and be owned by `from`.
- If the caller is not `from`, it must be have been allowed to move
this token by either {approve} or {setApprovalForAll}.
- If `to` refers to a smart contract, it must implement
{IERC721Receiver-onERC721Received}, which is called upon a safe transfer.

Emits a {Transfer} event._

### safeTransferFrom

```solidity
function safeTransferFrom(address from, address to, uint256 tokenId) external payable
```

_Equivalent to `safeTransferFrom(from, to, tokenId, '')`._

### transferFrom

```solidity
function transferFrom(address from, address to, uint256 tokenId) external payable
```

_Transfers `tokenId` from `from` to `to`.

WARNING: Usage of this method is discouraged, use {safeTransferFrom}
whenever possible.

Requirements:

- `from` cannot be the zero address.
- `to` cannot be the zero address.
- `tokenId` token must be owned by `from`.
- If the caller is not `from`, it must be approved to move this token
by either {approve} or {setApprovalForAll}.

Emits a {Transfer} event._

### approve

```solidity
function approve(address to, uint256 tokenId) external payable
```

_Gives permission to `to` to transfer `tokenId` token to another account.
The approval is cleared when the token is transferred.

Only a single account can be approved at a time, so approving the
zero address clears previous approvals.

Requirements:

- The caller must own the token or be an approved operator.
- `tokenId` must exist.

Emits an {Approval} event._

### setApprovalForAll

```solidity
function setApprovalForAll(address operator, bool _approved) external
```

_Approve or remove `operator` as an operator for the caller.
Operators can call {transferFrom} or {safeTransferFrom}
for any token owned by the caller.

Requirements:

- The `operator` cannot be the caller.

Emits an {ApprovalForAll} event._

### getApproved

```solidity
function getApproved(uint256 tokenId) external view returns (address operator)
```

_Returns the account approved for `tokenId` token.

Requirements:

- `tokenId` must exist._

### isApprovedForAll

```solidity
function isApprovedForAll(address owner, address operator) external view returns (bool)
```

_Returns if the `operator` is allowed to manage all of the assets of `owner`.

See {setApprovalForAll}._

### name

```solidity
function name() external view returns (string)
```

_Returns the token collection name._

### symbol

```solidity
function symbol() external view returns (string)
```

_Returns the token collection symbol._

### tokenURI

```solidity
function tokenURI(uint256 tokenId) external view returns (string)
```

_Returns the Uniform Resource Identifier (URI) for `tokenId` token._

 --- 
### Events:
### Transfer

```solidity
event Transfer(address from, address to, uint256 tokenId)
```

_Emitted when `tokenId` token is transferred from `from` to `to`._

### Approval

```solidity
event Approval(address owner, address approved, uint256 tokenId)
```

_Emitted when `owner` enables `approved` to manage the `tokenId` token._

### ApprovalForAll

```solidity
event ApprovalForAll(address owner, address operator, bool approved)
```

_Emitted when `owner` enables or disables
(`approved`) `operator` to manage all of its assets._

### ConsecutiveTransfer

```solidity
event ConsecutiveTransfer(uint256 fromTokenId, uint256 toTokenId, address from, address to)
```

_Emitted when tokens in `fromTokenId` to `toTokenId`
(inclusive) is transferred from `from` to `to`, as defined in the
[ERC2309](https://eips.ethereum.org/EIPS/eip-2309) standard.

See {_mintERC2309} for more details._

