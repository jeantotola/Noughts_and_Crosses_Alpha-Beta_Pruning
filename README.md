# Noughts and Crosses with Alpha-Beta Pruning

A high-performance Noughts and Crosses AI implemented in Python using the Minimax algorithm optimized with Alpha-Beta pruning.

## Features
- **Minimax Algorithm**: Ensures the AI plays optimally.
- **Alpha-Beta Pruning**: Reduces the number of nodes evaluated in the search tree, making the decision process significantly faster.

## How it Works
The AI explores the game tree to find the move that maximizes its chances of winning while assuming the opponent plays optimally. 
- **Alpha**: Represents the minimum score the maximizing player is assured of.
- **Beta**: Represents the maximum score the minimizing player is assured of.

When *alpha >= beta*, the algorithm "prunes" the remaining branches of the search tre, as they cannot influence the final decision.