# Level 3

Level 3 is dominated by a vast maze, and thus there is little to make a flowchart as most rooms in the maze can easily lead to most other rooms.

```mermaid
flowchart TD
    B06[Level 2 Room 06] <---> C1[Room 1]
    A31[Level 1 Room 31] <--> B11[Level 2 Room 11] <--> Maze
    C1 <--> C2[Room 2]
```