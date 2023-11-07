# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")
print(band)
print(band2)
print(type(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all key
print(band.keys())

# list all values
print(band.values())

# list of keyvalues,pair as tuple
print(band.items())

# verify a keyexists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
# band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drum"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete and clear
band["drum"] = "Bonham"
del band["drum"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band  # create a reference
# print("Bad copy!.")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)
print("Good copy")

# or use the dict()constructor function
band3 = dict(band)
print("Good copy")
print(band3)

# Nested Dicionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if values in a set
print(2 in nums)

# But you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)
# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
# you can use update with lists,tuple and dictionaries too

# Merge two sets to create a new set
ones = {1, 2, 3}
two = {5, 6, 7}

mynewset = ones.union(two)
print(mynewset)
# Keep only duplicate
ones = {1, 2, 3}
two = {2, 3, 4}
ones.intersection_update(two)
print(ones)

# Keep only except
ones = {1, 2, 3}
two = {2, 3, 4}
ones.symmetric_difference_update(two)
print(ones)
