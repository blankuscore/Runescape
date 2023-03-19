# Project Botscape

**Version 0.1.5**

The goal of this project is to build and design code in order to automate runescape accounts.
Most code samples focus on starting skills, 

## Contributors
- Greg Martinjak <greg.martinjak@gmail.com>
---

## OSRS Login info:
```diff
#Banned
- email: wehay77196@tagbert.com 
- password: PsnmO91lgILDpqChvwee 

#Active
+ email: wehay@proton.com
+ password: X5796iCpdRcmMch
```
## Explanation of various folders
- Character_Creation - randomizes and creates a character using a list of names and randomized features.  Timed to tick timing of osrs
- Emerald_Rings - crafting rings (emerald) using furnace in Edgeville
- Skilling - 
    - Fishing - fishing for shrimp at south of lumbridge, salmon/trout at barbarian village, lobster at Karamja
    - Mining - mining iron ore at mine north of Al Khazir
    - chopping.py - chopping trees [INCOMPLETE]

## Goals
The goals of the project are to develop methods to 'afk' leveling of all f2p skills from 1-40.  The order of priority are as follows:

High Priority
- Woodcutting
- Fishing 
- Mining

Med Priority
- Attack
- Strength
- Defense
- Magic
- Ranged

Low
- Smithing
- Crafting
- Cooking

Lowest
- Runecrafting
- Firemaking
- Prayer

Once all skills are at level 40, the goal of the project is to utilize money-making methods to generate enough income for a bond.
The income generated shouldn't take more than 1-2 weeks to create and should be sustainable and replicable.  Similarly the mechanisms to generate revenue should not result in a banned account and shouldn't be too fast in such a way that anti-cheating picks up on too much progression too quickly.

The project will not include automating quest points, or game completion.  Only generating a minimum viable f2p account ready for membership.
The project is not designed for scaleability nor to generate a 'bot farm' as this is only for entertainment and educational purposes.

## Next steps:
- Update Emerald_Rings for exception handling and crafting leveling from 1-60
- Update woodcutting for better tree finding algorithm

## License & copyright
None required or utilized