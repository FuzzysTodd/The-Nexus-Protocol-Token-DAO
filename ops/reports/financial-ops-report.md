# Financial Ops Automation Report

- Generated at: 2026-04-06T18:26:17+00:00
- Files scanned: 3726
- Pre-error findings: 65
- Withdrawal signals: 2026
- Placement signals: 2826
- Approval gate: required for any fund movement or treasury action

## Bot Status

- Pre-Error Remediation Bot: ready
- Withdrawal Placement Scanner: ready
- Success Documentation Reporter: ready

## Top Findings

- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/access/Ownable.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC20/ERC20.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC20/IERC20.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC721/ERC721.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC721/IERC721.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol: Suspicious filename pattern can make automation and review harder.
- [low] ERC20-NFT-Sale-with-Distributed-Royalties(copy)(copy)/@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol: Suspicious filename pattern can make automation and review harder.

## Recommended Actions

- Review the pre-error queue and clear malformed or duplicate repository-owned files first.
- Use the Withdrawal Placement Scanner findings to rank payout and treasury code for human review.
- Treat Ethereum and Base connectivity assumptions as separate operational checks before extending automation.
