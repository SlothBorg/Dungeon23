# Level 2

```mermaid
flowchart TD
    A29[Level 1 Room 29] <---> B1[Room 1]
    B1 <--> La[Lake]
    A30[Level 1 Room 30] <-- Underwater Tunnel ----> La
    B2[Room 2] <--> La
    B3[Room 3] <--> La
    B4[Room 4] <--> La
    B5[Room 5] <--> La
    B6[Room 6] <--> La
    B7[Room 7] <--> La
    B7 <--> B8[Room 8]
    B8 <--> B9[Room 9]
    B9 <--> B10[Room 10]
    A31[Level 1 Room 31] <--> B11[Room 11] <--> B4
    La <--> B12[Room 12]
    B13[Room 13] <--> B12
    B13 <--> B14[Room 14]
    B12 <--> B14
    La <----> B15[Room 15]
```