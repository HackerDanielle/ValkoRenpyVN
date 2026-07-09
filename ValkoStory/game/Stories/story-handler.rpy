init python:
    # This returns a list of all files inside the /game folder
    all_game_files = renpy.list_files()
    story_files = []
    # Example: Filter out only text files inside a specific folder
    # my_custom_files = [f for f in all_game_files if f.startswith("text_folder/") and f.endswith(".txt")]
    for f in all_game_files:
        path = f.split('/')
        if path[0] == "Stories":
            story_files.append(path)
    print(story_files)  # This will print the list of text files found in the /game/text_folder
    # STORY_DIRS = story_files