#create a dictionary
official_languages = {
    "Italy": "Italian",
    "France": "French",
    "Georgia": "Georgian",
    "China": "Mandarin",
}

#access 
print(official_languages.get("France"))
print(official_languages["China"])
# you can't access a key by it's value without creating a function to do it
print(official_languages)
#add
official_languages["Thailand"] = "Thai"