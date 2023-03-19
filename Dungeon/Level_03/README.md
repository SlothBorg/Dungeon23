# Level 3

Level 3 is dominated by a vast maze, and thus there is little to make a flowchart as most rooms in the maze can easily lead to most other rooms.

## Connections to other levels:

```mermaid
flowchart TD
    B06[Level 2 Room 06] <---> C1[Room 1]
    A31[Level 1 Room 31] <--> B11[Level 2 Room 11] <--> Maze
```

## Maze "layout"

```mermaid
flowchart TD
    C1[Room 1] <--> Blood[Blood maze section] <--> C31[Room 31]
    C1[Room 1] <--> Darkness[Darkness maze section] <--> C31
    C1[Room 1] <--> Inferno[Inferno maze section] <--> C31
```

## Blood section
```mermaid
flowchart TD
    Blood[Blood maze section] <-->C2[Room 02]
    Blood <--> C3[Room 03]
    Blood <--> C4[Room 04]
    Blood <--> C5[Room 05] <--> C6[Room 06] <-- secret door --> Blood
    Blood <--> C7[Room 07]
    Blood <--> C8[Room 08]
    Blood <--> C9[Room 09]
    Blood <--> C10[Room 10]
    Blood <--> C11[Room 11]
    Blood <--> C12[Room 12]

```

## Darkness section
```mermaid
flowchart TD
    Blood[Blood maze section] <-->C13[Room 13]
    Blood <--> C14[Room 14]
    Blood <--> C15[Room 15]
    Blood <--> C16[Room 16]
    Blood <--> C17[Room 17]
    Blood <--> C18[Room 18]

```