// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDEX {
    function swapExactTokensForTokens(
        uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline
    ) external returns (uint[] memory amounts);
}

contract ArbitrageRouter {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function executeArbitrage(
        address dex1, address dex2,
        address[] calldata pathForward,
        address[] calldata pathBackward,
        uint amountIn,
        uint minProfit
    ) external {
        require(msg.sender == owner, "Only owner");

        IERC20(pathForward[0]).transferFrom(msg.sender, address(this), amountIn);
        IERC20(pathForward[0]).approve(dex1, amountIn);

        uint[] memory out1 = IDEX(dex1).swapExactTokensForTokens(
            amountIn, 1, pathForward, address(this), block.timestamp
        );

        uint amountOut = out1[out1.length - 1];
        IERC20(pathBackward[0]).approve(dex2, amountOut);

        uint[] memory out2 = IDEX(dex2).swapExactTokensForTokens(
            amountOut, 1, pathBackward, msg.sender, block.timestamp
        );

        require(out2[out2.length - 1] >= amountIn + minProfit, "No profit");
    }
}

interface IERC20 {
    function approve(address spender, uint amount) external returns (bool);
    function transferFrom(address from, address to, uint amount) external returns (bool);
}
