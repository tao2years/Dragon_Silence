# BILI-011 / 014 / 016：现代毒伤逐帧复核

Captured: 2026-10-22

Method: Bilibili public `x/player/pagelist` and `x/player/playurl` endpoints returned the public 720P streams. Result, hero, gear and timeline frames were reviewed locally. Video binaries and extracted frames are temporary and are not committed.

## BILI-014：S9四阶段双蛇毒伤

Source: https://www.bilibili.com/video/BV1CzpB6zEmi/

- cid: `42718986425`; duration 106.2 seconds.
- Challenge phase IV, level 100, result time `06:42`.
- Team: `瑟潘忒弥斯 + 图奇 + 斯赖特 + 混沌之子 + 蕾塔`.
- Inspiration visible: 蛇女4、图奇5、混沌之子1、蕾塔4；斯赖特卡面未显示红色激励标记。
- Two attempts: `7,687,763,566 + 14,261,200,415 = 21,948,963,981`.

Frame-verified stats:

| Hero | Key visible stats | Narrated build note |
|---|---|---|
| 瑟潘忒弥斯 | attack +4917, mastery +528, accuracy +60, haste +12 | conventional damage build; creator says it is still ~30 accuracy short |
| 图奇 | attack +2575, mastery +82, accuracy +281, resistance +45 | lower gear can combine Whirlwind and Inferno; creator says ideal accuracy above 400 for this setup |
| 斯赖特 | attack +1679, mastery +304, accuracy +182, resistance +50, haste +13 | Dragonblood + Darknight; equipment quality limited attack |
| 混沌之子 | HP +82155, accuracy +270, resistance +157, haste +11 | Angel Alliance; Puppet set/New Moon red gear; HP main; creator calls for 240+ accuracy without the bypass-resistance talent |
| 蕾塔 | HP +87858, defense +1111, accuracy +264, resistance +107, haste +14 | defense/HP shell; creator notes armor-break stability is imperfect |

Timeline:

- 蛇女 default / 18.0s
- 图奇 14.5 / 18.0s
- 斯赖特 14.2 / 18.0s
- 混沌之子 11.5 / 18.0s
- 蕾塔 14.0 / 18.0s
- Narration adds that certain 蕾塔 inspiration timing can require pushing the two rat units to roughly 14.6/14.7 seconds.

This video directly resolves the community nickname “毒鸡” as `蕾塔`: the profile frame is labelled 蕾塔 and uses the same portrait as the earlier embedded “毒鸡” team.

## BILI-016：S9王冠上路毒伤双版本

Source: https://www.bilibili.com/video/BV1nxnP6eEr3/

- cid: `42899866025`; duration 186.9 seconds.
- Boss shown: Crown upper lane, ice element guardians.

### 无子夜 / 图奇版

- Team: `瑟潘忒弥斯 + 斯赖特 + 混沌之子 + 塞崔迪娅（城主） + 图奇`.
- Score: `3,846,756,755`.
- Inspiration visible: 蛇女1、混沌之子1、图奇2；斯赖特/城主卡面未显示红色标记。
- Public code from the author comment: `S9261020QU7AO4B3`.
- Timeline: 蛇女10.0/18, 斯赖特11.7/18, 混沌之子default/18, 城主11.5/18, 图奇11.8/18.

### 有子夜版

- Team: `子夜 + 瑟潘忒弥斯 + 斯赖特 + 混沌之子 + 塞崔迪娅（城主）`.
- Score: `3,350,462,211`.
- Public code from the author comment: `S9261020QU5B7BX2`.
- Timeline: 子夜11.7/18, 蛇女10.0/18, 斯赖特11.6/18, 混沌之子default/default, 城主11.5/18.

The same account and boss therefore provide a cleaner comparison than unrelated tier lists: the creator's no-Midnight/Twitch version scored about 14.8% higher in this recorded run. It is still one run per setup, not a universal ranking.

## BILI-011：S8 0激励蛇女、无斯赖特

Source: https://www.bilibili.com/video/BV1RKuL6dEc3/

- cid: `40731345158`; duration 181.7 seconds.
- Challenge phase IV, result time `07:24`.
- Team: `图奇 + 瑟潘忒弥斯 + 塞崔迪娅（城主） + 金面具生存辅助（姓名未在帧中显示） + 蕾塔`.
- Inspiration visible: 图奇2、蛇女0、城主4、金面具辅助2、蕾塔1.
- Two attempts: `893,242,066 + 15,598,953,740 = 16,492,195,806`.
- This directly verifies a zero-inspiration Serpentemis team without Sleight.

Selected visible build notes:

- 城主: accuracy +224, resistance +74, haste +36; overlay says sharing + Whirlwind + Ancient + Darknight, accuracy 200+, then defense; talent 3-2.
- 蛇女: attack +3565, mastery +442, accuracy +96, resistance +98; overlay says mastery/attack main and one accuracy right-side piece; talent 1-1-2-1.
- 图奇: attack +2096, mastery +64, accuracy +261, haste +19; overlay says sharing + inheritance + two-piece attack speed, accuracy 200+, then defense; talent 1-1-2-1.
- 蕾塔: HP +61287, defense +1238, accuracy +127, haste +72; overlay says accuracy 120+, more attack speed if possible, then HP/defense; talent 3-2-3-2, or 2-2-3-2 at zero inspiration.

## Decision impact for 370

1. “No Sleight means Serpentemis cannot function” is now contradicted by a complete S8 result, not just a title or database team.
2. Midnight is optional in the current modern core. In BILI-016, the Twitch version outscored the Midnight version on the same recorded boss/account.
3. Reta is a real endgame poison support/damage slot, but the S9 phase-IV result used inspiration 4 and a very durable build. It should not be treated as a free low-investment substitute.
4. The 300-pull priority remains engine first: Serpentemis + stable poison application + survival. Sleight/Midnight/Reta are account- and boss-dependent ceiling pieces.

## Limits

- None of the videos identifies server 368/369/370.
- Results are cross-season, account-specific and cannot be converted into 370 damage promises.
- The unnamed gold-mask support in BILI-011 needs client/team-code verification before assigning an official name.
- Public team codes still need import in 370 to verify cross-server parsing.
