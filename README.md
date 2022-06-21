# MCBE Loot Randomizer

Loot randomizer for Minecraft: Bedrock Edition. The application takes a user-inputted seed and randomization settings to randomize mob drops and chest loot tables.
Report any bugs to Battlecats59#2431 on Discord. You can join the [MCBE Discord Server](https://discord.gg/RDq2Sm8xYm) to DM me.

## Installation

**As of the latest build, the randomizer is only available on Windows devices.** Linux compatibility is still in progress.

### Running the compiled binary **(RECOMMENDED)**

#### Dev build (May be unstable)
1. To install the most recent dev build, head over to https://nightly.link/Battlecats59/MCBELootRandomizer/workflows/build.yaml/master/dist%20windows-latest.zip and install the latest Windows build.
2. Extract the .exe file and run it.
3. The randomizer should automatically find and select the output folder. If not, browse for the output folder and paste the following file path into the address bar.

` %LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs `

4. Select your options and hit randomize.

#### Latest Release
1. To install the latest release, head over to the [release section](https://github.com/Battlecats59/MCBELootRandomizer/releases) and install the latest release.
2. Extract the .exe file and run it.
3. The randomizer should automatically find and select the output folder. If not, browse for the output folder and paste the following file path into the address bar.

` %LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs `

4. Select your options and hit randomize.

### Running from Source

1. Clone this repository
2. Install Python 3.8 and pip (should come with most python installers)
3. Navigate to the repository directory in a terminal of your choice
4. Run the following command in the terminal

` pip install -r requirements.txt `

5. Run the application using the following command

` python randomizer.py `

OR

` py randomizer.py `


6. You can also build the exe from the source code using the following commands:

` pip install -r requirements_build.txt `

` pyinstaller randomizer.spec `


## Documentation

**Output Folder:** The output folder is where the behavior pack will be built in. The randomizer should automatically set this to your MCBE behavior pack folder if you have MCBE installed. If the randomizer does not automatically do this, you will need to manually browse for the folder. Pasting the following path into the address bar in the file explorer should give you the proper output folder, although this folder can be set to any valid directory.
` %LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs `

**Seed:** The seed that the randomizer uses to determine how the loot tables are shuffled. This is **not** the same as the Minecraft world seed, this seed is used for specifically the randomizer, for races and set randomizer seed runs. Seed -1 or any non-integer input will result in a random seed.

**Preset:** Used to preset randomizer settings. If you are doing a leaderboard speedrun, this **must** be set to a speedrun preset. The custom preset will allow you to select your own settings for casual playthroughs, since this is not allowed in leaderboard speedruns unless the category specifically allows it.

**Spoiler Log:** If this option is selected, the randomizer will write a .txt file in the directory with the behavior pack, which tells you where all of the loot tables are shuffled. This is not allowed in leaderboard speedruns unless the category specifically allows it.

## Loot Table Documentation

All of the randomized loot tables and their respective category can be found in the [loot_table_categories.yaml](https://github.com/Battlecats59/MCBELootRandomizer/blob/master/loot_table_categories.yaml) file in this repository. A detailed documentation will come soon.

## Special Mentions

- Code from [Skyward Sword Randomizer](https://github.com/lepelog/sslib)
- Code from [Wind Waker Randomizer](https://github.com/LagoLunatic/wwrando)
