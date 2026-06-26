import { ethers } from "hardhat";

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying with:", deployer.address);

  // 1. NexusServiceToken
  const NST = await ethers.getContractFactory("NexusServiceToken");
  const nst = await NST.deploy();
  await nst.deployed();
  console.log("NST:", nst.address);

  // 2. ValidatorPool
  const ValidatorPool = await ethers.getContractFactory("ValidatorPool");
  const validatorPool = await ValidatorPool.deploy(nst.address);
  await validatorPool.deployed();
  console.log("ValidatorPool:", validatorPool.address);

  // 3. DeveloperFund
  const DeveloperFund = await ethers.getContractFactory("DeveloperFund");
  const developerFund = await DeveloperFund.deploy(nst.address);
  await developerFund.deployed();
  console.log("DeveloperFund:", developerFund.address);

  // 4. NexusTreasury
  const Treasury = await ethers.getContractFactory("NexusTreasury");
  const treasury = await Treasury.deploy(
    nst.address,
    validatorPool.address,
    developerFund.address
  );
  await treasury.deployed();
  console.log("Treasury:", treasury.address);

  // 5. NexusFeeMarket
  const FeeMarket = await ethers.getContractFactory("NexusFeeMarket");
  const feeMarket = await FeeMarket.deploy(
    nst.address,
    treasury.address,
    validatorPool.address,
    developerFund.address
  );
  await feeMarket.deployed();
  console.log("FeeMarket:", feeMarket.address);

  // 6. Wire minters
  await (await nst.addMinter(treasury.address)).wait();
  await (await nst.addMinter(feeMarket.address)).wait();

  console.log("Nexus system deployed and wired.");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
