# MCBE Loot Randomizer Information

The Minecraft: Bedrock Edition Loot Randomizer takes a user-inputted seed and settings and shuffles mob loot tables and/or chest loot tables, depending on the settings. Descriptions of all randomizer settings can be found by hovering over the setting in the application, as well as in this document.

## Table of Contents

1. [**Speedrunning**](#speedrunning)
2. [**Casual**](#casual)
3. [**Options**](#options)
4. [**Hash and Permalink**](#hash-and-permalink)
5. [**Notes**](#notes)

## Speedrunning

There are several speedrunning presets that can be used for speedruns. Below is a detailed description of all speedrunning presets:

- **Speedrun:** This is the standard speedrunning preset. It shuffles all mob loot tables, including bosses. No chest loot tables are shuffled, and no spoiler log is generated. Any Minecraft version can be selected, and this preset allows for both random and set randomizer seed runs.

- **Speedrun w/ Randomized Chest Loot:** This is the same as the standard speedrunning preset above, however all chest loot tables are shuffled. No spoiler log is generated. Any Minecraft version can be selected, and this preset allows for both random and set randomizer seed runs.

- **Speedrun w/ Spoiler Log:** This preset shuffles all mob loot tables, but no chest loot tables are shuffled. A spoiler log will be generated in the behavior pack folder, which can be used during the run in order to see where the loot tables are shuffled, like a scouted seed. If doing a leaderboard run with this preset, be sure to read the leaderboard rules. Any Minecraft version can be selected, and this preset allows for ONLY random randomizer seed runs.

- **Speedrun w/ Spoiler Log & Randomized Chest Loot:** Similarly to the speedrun w/ spoiler log preset above, this preset will shuffle all mob loot tables, however also shuffles all chest loot tables. A spoiler log will be generated in the behavior pack folder, which can be used during the run in order to see where the loot tables are shuffled, like a scouted seed. If doing a leaderboard run with this preset, be sure to read the leaderboard rules. Any Minecraft version can be selected, and this preset allows for ONLY random randomizer seed runs.

If doing a leaderboard run, be sure to read the leaderboard rules for that category prior to doing your run so your run can be verified. Selecting a preset option will automatically check and uncheck all options necessary, and will disable them so you cannot change them, unless you change the preset.

## Casual

If playing casually with randomized loot, you can select the **Custom** preset, which allows you to choose which groups of mobs and chests are randomized. It also gives you the option to generate a spoiler log, which will be generated in the behavior pack folder created when you generate the pack. You can also choose the Minecraft version and the randomizer seed.

## Options

Below are all of the randomizer options:

![GUI Example](/assets/gui_example.png)

**Output Folder:** The output folder is where the behavior pack will be built in. The randomizer should automatically set this to your MCBE behavior pack folder if you have MCBE installed. If the randomizer does not automatically do this, you will need to manually browse for the folder. Pasting the following path into the address bar in the file explorer should give you the proper output folder, although this folder can be set to any valid directory.
` %LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs `

**Seed:** The seed that the randomizer uses to determine how the loot tables are shuffled. This is **not** the same as the Minecraft world seed, this seed is used for specifically the randomizer, for races and set randomizer seed runs in order to have the same shuffled loot. Seed -1 or any non-integer input will result in a random seed.

**Preset:** Used to preset randomizer settings. If you are doing a leaderboard speedrun, this **must** be set to a speedrun preset. The custom preset will allow you to select your own settings for casual playthroughs, since this is not allowed in leaderboard speedruns unless the category specifically allows it. See the [**Speedrunning**](#speedrunning) and the [**Casual**](#casual) sections for more infortmation on presets.

**Minecraft Version:** This is the Minecraft version that you will be playing on with the pack. This is important as it determines which mobs are added to the pool, since newer versions have mobs that older versions do not have. You only have to select the main version, such as 1.16. The minor version (the X in 1.16.X) does not matter when selecting the version.

**Spoiler Log:** If this option is selected, the randomizer will write a .txt file in the directory with the behavior pack, which tells you where all of the loot tables are shuffled. This is not allowed in leaderboard speedruns unless the category specifically allows it. (Speedrun w/ Spoiler Log presets)

**Mob Drops:** All categories of mobs that are checked will be shuffled, and all categories that are unchecked will remain vanilla.

**Chest Loot:** All categories of chests that are checked will be shuffled, and all categories that are unchecked will remain vanilla.

## Hash and Permalink

### Randomizer Hash
The randomizer hash is shown in a popup immediately after generating the seed and in the description of the behavior pack. This is used to confirm that the pack you are using is the one you generated. It is a series of 3 minecraft-related words that is generated using the settings and the seed, so it can be used for verification and to make sure racers are using the same pack. For leaderboard runs, generation of the randomizer pack and the popup with the hash must be shown in the recording to verify that the pack applied during world creation is the same pack that was just generated.

### Randomizer Permalink
Currently, the randomizer permalink is only used to verify that the correct settings are used for leaderboard run verification. This is shown in the popup after generating a seed and in the pack description, which must be shown in the recording, as well as the hash, for run verification.

## Notes

### Loot Table Documentation
All of the randomized loot tables and their respective category can be found in the [loot_table_categories.yaml](https://github.com/Battlecats59/MCBELootRandomizer/blob/master/loot_table_categories.yaml) file in this repository. A detailed documentation will come soon.

### Bugs, Suggestions, and Questions
Report any bugs, suggestions, or questions you have to Battlecats59#2431 on Discord. You can join the [MCBE Discord Server](https://discord.gg/RDq2Sm8xYm) to DM me.
