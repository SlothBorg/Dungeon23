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
    B6 <----> C1[Level 3 Room 01]
    B7[Room 7] <--> La
    B7 <--> B8[Room 8]
    B8 <--> B9[Room 9]
    B9 <--> B10[Room 10]
    A31[Level 1 Room 31] <--> B11[Room 11] <--> B4
    A31[Level 1 Room 31] <--> B11[Room 11] <---> C1
    La <--> B12[Room 12]
    B13[Room 13] <--> B12
    B13 <--> B14[Room 14]
    B12 <--> B14
    La <----> B15[Room 15]
    B15 <--> B16[Room 16]
    B16 <--> B17[Room 17]
    B16 <--> B18[Room 18]
    B17 <--> B18
    B16 <--> B19[Room 19]
    B18 <--> B19
    B16 <--> B20[Room 20]
    B18 <--> B20
    B16 <--> B21[Room 21]
    B17 <--> B21
    B18 <--> B21
    B21 <--> B22[Room 22]
    B22 <--> B23[Room 23]
    B23 <--> B24[Room 24]
    B24 <--> B25[Room 25]
    B24 <--> B26[Room 26]
    B25 <--> B26
    B23 <--> B27[Room 27]
    B27 <--> La
```